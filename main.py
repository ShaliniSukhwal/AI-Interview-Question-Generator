from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from google import genai
import os

# Load environment variables
load_dotenv()

# Gemini Client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

app = FastAPI(
    title="AI Interview Question Generator",
    description="Generate AI-powered interview questions using Google Gemini.",
    version="1.0.0"
)


# -------------------------
# Models
# -------------------------
class InterviewRequest(BaseModel):
    role: str = Field(..., example="UI UX Designer")
    company: str = Field(..., example="Google")
    experience: str = Field(..., example="5 Years")
    difficulty: str = Field(..., example="Intermediate")
    question_count: int = Field(..., ge=1, le=20, example=10)
    question_type: str = Field(..., example="Technical")

# -------------------------
# Routes
# -------------------------

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Interview Generator API"
    }


@app.get("/health")
def health():
    return {
        "status": "Running"
    }


@app.post("/generate")
def generate_questions(data: InterviewRequest):

    prompt = f"""
You are a senior interviewer at {data.company}.

Generate exactly {data.question_count} interview questions.

Candidate Details:

Role: {data.role}
Experience: {data.experience}
Difficulty: {data.difficulty}
Question Type: {data.question_type}

Rules:

- Return only interview questions.
- No introduction.
- No explanation.
- No answers.
- Number each question.
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        questions = [
    q.strip()
    for q in response.text.split("\n")
    if q.strip()
]
        return {
                "success": True,
                "company": data.company,
                "role": data.role,
                "experience": data.experience,
                "difficulty": data.difficulty,
                "question_type": data.question_type,
                "total_questions": len(questions),
                "questions": questions
            }
    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )