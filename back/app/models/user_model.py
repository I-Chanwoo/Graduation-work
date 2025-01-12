# 유저 model & 스키마
from beanie import Document
from pydantic import BaseModel, EmailStr

class User(Document):
    
    id : EmailStr
    username: str
    password: str
    gender: str
    
    class Settings:
        collection = "users"
    
