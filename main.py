from statistics import mode
from urllib import request, response
from fastapi import FastAPI, Depends, status, Response
import schemas
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)

def getDB(): 
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Response": "Hello"}


@app.post("/student", status_code=status.HTTP_201_CREATED)
def create_student(request: schemas.Student, db: Session = Depends(getDB)):
    new_student = models.Student(first_name=request.first_name, last_name=request.last_name)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


@app.get("/student/{student_id}", status_code=status.HTTP_200_OK)
def read_student(student_id: int, response: Response, db: Session = Depends(getDB)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student:
        return student
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return { "error" : "Student not found" }


@app.patch("/student/{student_id}", status_code=status.HTTP_200_OK)
def update_student(student_id: int, request: schemas.Student, db: Session = Depends(getDB)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student:
        student.first_name = request.first_name
        student.last_name = request.last_name
        db.commit()
        return student
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return { "error" : "Student not found" }


@app.delete("/student/{student_id}", status_code=status.HTTP_200_OK)
def delete_student(student_id: int, db: Session = Depends(getDB)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student:
        db.delete(student)
        db.commit()
        return { "message" : "Student deleted" }
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return { "error" : "Student not found" }


@app.post("/course", status_code=status.HTTP_201_CREATED)
def create_course(request: schemas.Course, db: Session = Depends(getDB)):
    new_course = models.Course(name=request.name)
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course


@app.get("/course/{course_id}", status_code=status.HTTP_200_OK)
def read_course(course_id: int, response: Response, db: Session = Depends(getDB)):
    course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if course:
        return course
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return { "error" : "Course not found" }


@app.patch("/course/{course_id}", status_code=status.HTTP_200_OK)
def update_course(course_id: int, request: schemas.Course, db: Session = Depends(getDB)):
    course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if course:
        course.name = request.name
        db.commit()
        return course
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return { "error" : "Course not found" }


@app.delete("/course/{course_id}", status_code=status.HTTP_200_OK)
def delete_course(course_id: int, db: Session = Depends(getDB)):
    course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if course:
        db.delete(course)
        db.commit()
        return { "message" : "Course deleted" }
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return { "error" : "Course not found" }