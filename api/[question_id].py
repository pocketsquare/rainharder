from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/api/{question_id}")
async def read_question(question_id: int):
    return {"question_id": question_id}

handler = Mangum(app)
