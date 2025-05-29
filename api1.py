from fastapi import FastAPI, HTTPException
from model import Student, UpdateStudentName
import apidb

app = FastAPI()

@app.on_event("startup")
def startup_event():
    apidb.create_table()

@app.post("/students")
def create_student(student: Student):
    try:
        apidb.insert_student(student.student_id, student.student_name, student.student_age, student.student_branch)
        return {"message": "Student added successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/students")
def get_students():
    students = apidb.fetch_all_students()
    return [
        {
            "student_id": s[0],
            "student_name": s[1],
            "student_age": s[2],
            "student_branch": s[3]
        } for s in students
    ]

@app.put("/students/{student_id}/name")
def update_student(student_id: int, update: UpdateStudentName):
    updated = apidb.update_student_name(student_id, update.student_name)
    if updated == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student name updated successfully"}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    deleted = apidb.delete_student(student_id)
    if deleted == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}
