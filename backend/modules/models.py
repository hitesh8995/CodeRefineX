from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class ReviewRequest(BaseModel):
    code: str
    language: str = "Python"
    mode: str = "standard"  # Options: standard, performance, security, clean, comments

# --- Quality Dashboard (Radar Chart Data) ---
class QualityScore(BaseModel):
    maintainability: int  # 0-100
    security: int         # 0-100
    performance: int      # 0-100
    readability: int      # 0-100
    overall: int          # Average

# --- Performance Simulator Data ---
class ComplexityData(BaseModel):
    cyclomatic_complexity: int
    complexity_rank: str  # A, B, C, D, F
    description: str      # "Low Risk", "High Risk"

# --- Unified Issue Model (Heatmap Data) ---
class Issue(BaseModel):
    severity: str         # Critical, High, Medium, Low
    confidence: int       # 0-100
    category: str         # Security, Performance, Style, Logic
    description: str
    line_number: Optional[str]
    source: str           # "AI", "Bandit", "Flake8", "Radon"
    suggestion: Optional[str]

# --- The Mega Response ---
class AdvancedReviewResponse(BaseModel):
    summary: str
    teacher_tips: List[str]       # "Did you know?" style tips
    quality_score: QualityScore   # Radar chart numbers
    complexity: ComplexityData    # Performance simulator
    issues: List[Issue]           # Heatmap data
    rewritten_code: str
    generated_test_cases: Optional[str] = None # For Test Gen feature