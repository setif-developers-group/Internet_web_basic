from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
from fastapi.middleware.cors import CORSMiddleware



con = sqlite3.connect("feedback.db")
cur = con.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    rating INTEGER NOT NULL,
    best_feature TEXT NOT NULL,
    feedback TEXT NOT NULL,
    improvements TEXT NOT NULL,
    next_workshop TEXT NOT NULL
)
''')

con.commit()
class Feedback(BaseModel):
    rating: int
    best_feature: str
    feedback: str
    improvements: str
    next_workshop: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # allow all origins
    allow_credentials=True,
    allow_methods=["*"],      # allow all HTTP methods
    allow_headers=["*"],      # allow all headers
)


@app.post("/submit_feedback/")
async def submit_feedback(feedback: Feedback):

    cur.execute('''INSERT INTO feedback (rating, best_feature, feedback, improvements, next_workshop)
                   VALUES (?, ?, ?, ?, ?)''',
                (feedback.rating, feedback.best_feature, feedback.feedback,
                 feedback.improvements, feedback.next_workshop))
    con.commit()
    return {"message": "Feedback submitted successfully"}