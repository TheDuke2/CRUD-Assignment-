from fastapi import FastAPI
from uuid import UUID

app = FastAPI()

students = {}

student_data = {
    "id": 0,
    "name": "",
    "age": int,
    "sex": "",
    "height": float
}


@app.get("/")
def home():
    return {"message": "Welcome to the Student Portal"}


@app.get("/students")
def get_students():
    return students


@app.post("/students")
def create_students(name: str, age: int, sex: str, height: float):

    new_student = student_data.copy()
    new_student["id"] = str(UUID(int=len(students) + 1))
    new_student["name"] = name
    new_student["age"] = age
    new_student["sex"] = sex
    new_student["height"] = height

    students[new_student["id"]] = new_student

    return {"message": "New student added successfully", "data": new_student}


@app.get("/students/{id}")
def get_single_students(id: str):
    student = students.get(id)
    if not student:
        return {"message": "Not a Student"}

    return student


@app.put("/students/{id}")
def update_students(id: str, name: str, age: int, sex: str, height: float):
    student = students.get(id)
    if not student:
        return {"message": "Not a Student"}

    student["name"] = name
    student["age"] = age
    student["sex"] = sex
    student["height"] = height

    return {"message": "Student updated successfully", "data": student}


@app.delete("/students/{id}")
def delete_students(id: str):
    student = students.get(id)
    if not student:
        return {"message": "Not a Student"}

    del student[id]

    return {"message": "Student deleted successfully"}
