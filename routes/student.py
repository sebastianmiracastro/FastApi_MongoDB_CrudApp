# IMPORT STATEMENTS
from fastapi import APIRouter
from models.student import Student
from config.database import connection
from schemas.student import studentEntity, listOfStudentEntity
from bson import ObjectId

student_router = APIRouter()


# GETTING ALL STUDENTS
@student_router.get('/students')
async def find_all_students():
    return listOfStudentEntity(connection.local.student.find())

# CREATE NEW STUDENT
@student_router.post('/students')
async def create_student(student: Student):
    connection.local.student.insert_one(dict(student))
    return listOfStudentEntity(connection.local.student.find())

# GET ONE STUDENT
@student_router.get('/students/{studentId}')
async def find_student(studentId):
    return studentEntity(connection.local.student.find_one({"_id": ObjectId(studentId)}))

# UPDATE A STUDENT
@student_router.put('/students/{studentId}')
async def update_student(studentId, student: Student):
    # FIND THE STUDENT AND THAN UPDATE WITH NEW STUDENT DATA
    connection.local.student.find_one_and_update(
        {"_id": ObjectId(studentId)},
        {"$set": dict(student)}
    )

    return studentEntity(connection.local.student.find_one({"_id": ObjectId(studentId)}))

# DELETE A STUDENT
@student_router.delete('/students/{studentId}')
async def delete_student(studentId):
    # FIND THE ESTUDENT AND DELETE IT
    return studentEntity(connection.local.student.find_one_and_delete({"_id": ObjectId(studentId)}))