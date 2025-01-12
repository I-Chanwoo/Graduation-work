import sys
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import auth
from app.routes.auth import router as auth_router

# ModuleNotFoundError 방지 (PYTHONPATH 추가)
sys.path.append(str(Path(__file__).resolve().parent.parent))


app = FastAPI()

# CORS 설정, react 서버 접근 허용용
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
#app.include_router(search.router)
#app.include_router(products.router)
app.include_router(auth.router)
app.include_router(auth_router)