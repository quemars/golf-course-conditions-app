from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Golf Course Conditions API is running"}

from app.database import cursor, conn
from fastapi import Body

@app.post("/round")
def add_round(data: dict = Body(...)):
    cursor.execute(
        "INSERT INTO rounds (course, greens, fairways, pace, notes) VALUES (?, ?, ?, ?, ?)",
        (
            data["course"],
            data["greens"],
            data["fairways"],
            data["pace"],
            data["notes"],
        ),
    )
    conn.commit()

    return {"message": "Round added"}
@app.get("/rounds")
def get_rounds():
    cursor.execute("SELECT * FROM rounds ORDER BY id DESC")
    rows = cursor.fetchall()

    result = []

    for r in rows:
        avg = round((r[2] + r[3] + r[4]) / 3, 1)

        result.append({
            "id": r[0],
            "course": r[1],
            "greens": r[2],
            "fairways": r[3],
            "pace": r[4],
            "notes": r[5],
            "score": avg
        })

    return result
