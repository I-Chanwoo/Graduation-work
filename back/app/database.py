# back/app/database.py
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = (
    "mongodb+srv://chanuel0110:qU1Ixpg9sefH1Ysh@jobadream.8qscb.mongodb.net/"
    "?retryWrites=true&w=majority&appName=Jobadream"
)

client = AsyncIOMotorClient(MONGO_URL)
db = client["Jobadream"]             
users_collection = db["users"]
