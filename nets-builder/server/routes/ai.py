"""
AI Runtime Tutor Endpoints.

Called by the homework playback frontend during student sessions.
All stateless. Request/response JSON, no SSE.
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, Any

from ..services import tutor

router = APIRouter(tags=["ai-tutor"])


# --- Request models ---

class CheckAnswerRequest(BaseModel):
    question: str
    student_answer: str
    expected_answers: list[str]
    subject: str
    grade: int
    tier: str = "MEDIUM"
    context: Optional[str] = None


class BossTurnRequest(BaseModel):
    boss_question: str
    student_answer: str
    expected_answers: list[str]
    damage_value: int = Field(ge=0, le=50)
    hp_remaining: int = Field(ge=0)
    attempt_number: int = Field(ge=1)
    subject: str
    grade: int


class ReflectionRequest(BaseModel):
    homework_title: str
    homework_summary: str
    student_reflection: str
    performance: dict[str, Any]
    subject: str
    grade: int


class TutorRequest(BaseModel):
    phase: str
    question: str
    student_input: str
    subject: str
    grade: int
    context: Optional[str] = None


# --- Endpoints ---

def _wrap_errors(fn):
    """Decorator to convert tutor exceptions to 500 errors with consistent shape."""
    async def wrapper(*args, **kwargs):
        try:
            return await fn(*args, **kwargs)
        except FileNotFoundError as e:
            raise HTTPException(500, detail={"error": str(e), "code": "PROMPT_MISSING"})
        except Exception as e:
            raise HTTPException(500, detail={"error": str(e), "code": "AI_ERROR"})
    wrapper.__name__ = fn.__name__
    return wrapper


@router.post("/ai/check-answer")
@_wrap_errors
async def check_answer(req: CheckAnswerRequest):
    return await tutor.check_answer(
        question=req.question,
        student_answer=req.student_answer,
        expected_answers=req.expected_answers,
        subject=req.subject,
        grade=req.grade,
        tier=req.tier,
        context=req.context,
    )


@router.post("/ai/boss-turn")
@_wrap_errors
async def boss_turn(req: BossTurnRequest):
    return await tutor.boss_turn(
        boss_question=req.boss_question,
        student_answer=req.student_answer,
        expected_answers=req.expected_answers,
        damage_value=req.damage_value,
        hp_remaining=req.hp_remaining,
        attempt_number=req.attempt_number,
        subject=req.subject,
        grade=req.grade,
    )


@router.post("/ai/reflection")
@_wrap_errors
async def reflection(req: ReflectionRequest):
    return await tutor.reflection_feedback(
        homework_title=req.homework_title,
        homework_summary=req.homework_summary,
        student_reflection=req.student_reflection,
        performance=req.performance,
        subject=req.subject,
        grade=req.grade,
    )


@router.post("/ai/tutor")
@_wrap_errors
async def tutor_help(req: TutorRequest):
    return await tutor.tutor_help(
        phase=req.phase,
        question=req.question,
        student_input=req.student_input,
        subject=req.subject,
        grade=req.grade,
        context=req.context,
    )
