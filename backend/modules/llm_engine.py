import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def get_ai_review(code: str, language: str, mode: str):
    
    # 1. Select Persona based on Mode
    persona = "You are an expert Senior Software Architect."
    focus = "General bugs and style."
    
    if mode == "security":
        persona = "You are a Cyber Security Expert (CISSP)."
        focus = "OWASP Top 10, Injection attacks, and memory safety."
    elif mode == "performance":
        persona = "You are a High-Frequency Trading System Engineer."
        focus = "Time complexity (Big O), memory leaks, and algorithmic efficiency."
    elif mode == "teacher":
        persona = "You are a patient CS Professor."
        focus = "Explaining concepts simply, teaching best practices, and creating learning tips."

    # 2. The JSON Schema for Output
    # This forces the AI to fill our "Dashboard" data
    system_prompt = (
        f"{persona} Review this {language} code focusing on: {focus}. "
        "You MUST return valid JSON matching this structure exactly:\n"
        "{\n"
        "  'summary': 'Executive summary...',\n"
        "  'teacher_tips': ['Tip 1', 'Tip 2'],\n"
        "  'quality_score': {'maintainability': 0-100, 'security': 0-100, 'performance': 0-100, 'readability': 0-100, 'overall': 0-100},\n"
        "  'issues': [{ 'severity': 'Critical|High|Medium', 'confidence': 0-100, 'category': 'Logic|Security|Perf', 'description': '...', 'line_number': '1', 'suggestion': '...' }],\n"
        "  'rewritten_code': '...',\n"
        "  'generated_test_cases': '... (Only if applicable)'\n"
        "}\n"
        "Do NOT use markdown blocks. Return raw JSON."
    )

    try:
        completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": code}
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.2,
            response_format={"type": "json_object"}
        )
        return json.loads(completion.choices[0].message.content)
    except Exception as e:
        return {"error": str(e)}