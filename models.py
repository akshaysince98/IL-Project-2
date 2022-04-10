from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from database import Base
from sqlalchemy.orm import relationship

class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True)
    
    name = Column(String(50), nullable=False)
    students = relationship('Student', backref='courses')

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)

    course_id = Column(Integer, ForeignKey('course.id'))
    courses = relationship('Course', backref='students')