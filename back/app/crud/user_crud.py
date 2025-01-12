from app.database import users_collection
from app.crud.security import hash_password
from back.app.models.user_model import UserCreate
from typing import Optional

# Read (Username으로 유저 찾기)
async def get_user_by_username(username: str) -> Optional[dict]:
    """
    username을 키로 users_collection에서 유저 1명 찾기
    """
    user = await users_collection.find_one({"username": username})
    return user

# Create (새 유저 생성)
async def create_user(user_data: UserCreate) -> dict:
    """
    새 유저 생성 (비번 해싱 포함)
    user_data: UserCreate 모델 (username, password, gender 등)
    """
    hashed_pw = hash_password(user_data.password)
    new_user = {
        "username": user_data.username,
        "password": hashed_pw,
        "gender": user_data.gender,
        # user_data에 email(=id) 등이 있다면 추가 가능
    }
    result = await users_collection.insert_one(new_user)
    # insert가 끝난 뒤, DB에서 다시 찾아서 반환 (ObjectId → dict)
    created_user = await users_collection.find_one({"_id": result.inserted_id})
    return created_user

# Update (비번 등 특정 필드 수정) - 예시
async def update_user(username: str, update_data: dict) -> Optional[dict]:
    """
    username 기준으로, update_data로 전달된 필드를 수정
    예: {"password": "새비번"} → 새 비번으로 업데이트
    """
    # 업데이트 시 비밀번호 해싱이 필요하다면, 여기서 처리
    if "password" in update_data:
        update_data["password"] = hash_password(update_data["password"])
    
    await users_collection.update_one(
        {"username": username},
        {"$set": update_data}
    )
    updated_user = await users_collection.find_one({"username": username})
    return updated_user

# Delete (유저 삭제) - 예시
async def delete_user(username: str) -> bool:
    """
    username 기준으로 유저 삭제
    반환값: True(삭제 성공), False(삭제 실패)
    """
    result = await users_collection.delete_one({"username": username})
    return result.deleted_count == 