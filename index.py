# IMPORT STATEMENTS 
from fastapi import FastAPI
from routes.student import student_router

# CREATE APP 

app = FastAPI()

# ROUTES HERE

app.include_router(student_router)