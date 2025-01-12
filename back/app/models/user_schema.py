from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    id : str
    username: str
    password: str
    gender: str

class UserResponse(BaseModel):
    id: str
    
    # hw
    class Config:
        orm_mode = True