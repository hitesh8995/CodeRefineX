import os
import json
import subprocess
import requests
from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv

# --- CONFIGURATION ---
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key or "gsk_placeholder")

app = FastAPI(title="CodeRefine X Ultimate")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- MODELS ---
class RequestModel(BaseModel):
    code: str
    language: str
    stdin: str = ""
    mode: str = "standard"

class AnalysisResponse(BaseModel):
    summary: str
    quality_score: dict
    issues: List[dict]
    rewritten_code: str
    dry_run: str
    teacher_tips: List[str]

# --- HELPERS ---
def get_ai_analysis(code, language, mode):
    # STRICT PROMPT FOR ZERO-ERROR CODE
    prompt = (
        f"Act as a Senior {language} Compiler. Task: Fix and Optimize this code. "
        "Return strictly valid JSON. Double quotes only. "
        "Structure: {"
        "\"summary\": \"Technical summary of changes\", "
        "\"quality_score\": {\"maintainability\": 0-100, \"security\": 0-100, \"overall\": 0-100}, "
        "\"issues\": [{\"severity\": \"Critical|High|Medium|Low\", \"line\": 1, \"type\": \"Bug|Security\", \"message\": \"What is wrong\", \"fix\": \"Hint\"}], "
        "\"rewritten_code\": \"The COMPLETE, FIXED code. Must be 100% bug-free. Must handle edge cases. Must compile. Add clean comments explaining logic. Format with proper indentation, line breaks, and structure. NO MARKDOWN.\", "
        "\"dry_run\": \"Step-by-step execution walk-through. Use \\n for newlines.\", "
        "\"teacher_tips\": [\"Concept 1\", \"Concept 2\"]"
        "}"
    )
    try:
        completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a strict code rectifier. You fix bugs. You do not explain basic concepts in the code section."},
                {"role": "user", "content": f"{prompt}\n\nCODE:\n{code}"}
            ],
            model="llama-3.3-70b-versatile", temperature=0.1, response_format={"type": "json_object"}
        )
        return json.loads(completion.choices[0].message.content)
    except Exception:
        return {"summary": "Error", "issues": [], "rewritten_code": code, "dry_run": "N/A", "teacher_tips": [], "quality_score": {"overall": 0}}

# --- ENDPOINTS ---
@app.post("/api/execute")
async def execute(req: RequestModel):
    lang_map = {"Python": "python", "Java": "java", "JavaScript": "javascript", "C++": "c++"}
    runtime = lang_map.get(req.language, "python")
    payload = {"language": runtime, "version": "*" if runtime != "c++" else "10.2.0", "files": [{"content": req.code}], "stdin": req.stdin}
    try:
        res = requests.post("https://emkc.org/api/v2/piston/execute", json=payload)
        return res.json().get("run", {})
    except:
        return {"stderr": "Compiler Connection Failed"}

@app.post("/api/analyze", response_model=AnalysisResponse)
async def analyze(req: RequestModel):
    data = get_ai_analysis(req.code, req.language, req.mode)
    return AnalysisResponse(
        summary=str(data.get("summary", "")),
        quality_score=data.get("quality_score", {"overall": 0}),
        issues=data.get("issues", []),
        rewritten_code=str(data.get("rewritten_code", "")),
        dry_run=str(data.get("dry_run", "No dry run available.")),
        teacher_tips=data.get("teacher_tips", [])
    )

# --- SERVE FRONTEND ---
@app.get("/")
async def serve_spa():
    return FileResponse(os.path.join(os.path.dirname(__file__), "static", "index.html"))

app.mount("/static", StaticFiles(directory=os.path.join(os.path.dirname(__file__), "static")), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)