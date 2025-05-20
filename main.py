from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware  # <-- Add this explicitly
from database import database
from schemas import Question

app = FastAPI()

# Explicitly add this CORS middleware exactly as shown:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # your Svelte frontend origin explicitly
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/questions/{question_id}", response_model=Question)
async def get_question(question_id: int):
    question = await database.fetch_one("SELECT * FROM questions WHERE id = :id", {"id": question_id})
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    left_entries = await database.fetch_all(
        "SELECT * FROM left_entries WHERE question_id = :question_id",
        {"question_id": question_id}
    )

    right_entries = await database.fetch_all(
        "SELECT * FROM right_entries WHERE question_id = :question_id",
        {"question_id": question_id}
    )

    left_entries_dicts = [dict(le) for le in left_entries]
    right_entries_dicts = [dict(re) for re in right_entries]

    return Question(
        id=question["id"],
        prompt=question["prompt"],
        left_entries=left_entries_dicts,
        right_entries=right_entries_dicts
    )
