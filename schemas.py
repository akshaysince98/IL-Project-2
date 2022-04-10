from typing import List, Optional
from pydantic import BaseModel

class Course(BaseModel):
    name: str

class Student(BaseModel):
    first_name: str
    last_name: str