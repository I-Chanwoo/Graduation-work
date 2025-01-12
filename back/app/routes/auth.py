from fastapi import APIRouter, HTTPException, Depends
from app.crud.security import hash_password, verify_password
from app.crud.user_crud import get_user_by_username, create_user
from back.app.models.user_model import UserCreate, UserResponse

from passlib.context import CryptContext

router = APIRouter(prefix="/auth", tags=["auth"])



# 회원가입
@router.post("/register")
async def register(user: UserCreate):
    # 1) username 중복확인
    existing_user = await get_user_by_username(user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    # 2) 새 유저 생성 (비밀번호 해싱 포함)
    new_user = await create_user(user)

    return {"message": "User registered successfully", "user": new_user}


# 로그인
@router.post("/login")
async def login(user: UserCreate):
    # 1) DB에서 username으로 유저 찾기
    stored_user = await get_user_by_username(user.username)
    if not stored_user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    # 2) 비밀번호 검증
    if not verify_password(user.password, stored_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return {"message": f"Welcome {user.username}"}


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)