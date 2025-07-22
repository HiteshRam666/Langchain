from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = "Hitesh"
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt = 0, lt = 10, default=5, description="A decimal Value representing the cgpa of the student")
    

new_student = {"age": 30, 'email': "hiteshram321@gmail.com"}

student = Student(**new_student)
print(student.name)
print(student.age)
print(student.email)
print(student.cgpa)