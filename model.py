from pydantic import BaseModel

class Student(BaseModel):
    student_id: int
    student_name: str
    student_age: int
    student_branch: str

class UpdateStudentName(BaseModel):
    student_name: str
