from bson import ObjectId
from database import user_collection

def create_user(user: dict):
    result = user_collection.insert_one(user)
    return str(result.inserted_id)

def read_user_by_id(user_id: str):
    user = user_collection.find_one({"_id": ObjectId(user_id)})
    if user:
        return {
            "id": str(user["_id"]),
            "username": user["username"],
            "password": user["password"]
        }
    return None

def update_username(user_id: str, new_username: str):
    result = user_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": {"username": new_username}}
    )
    return result.modified_count > 0

def delete_user(user_id: str):
    result = user_collection.delete_one({"_id": ObjectId(user_id)})
    return result.deleted_count > 0

def list_users_by_ids(user_ids: list):
    object_ids = [ObjectId(uid) for uid in user_ids]
    cursor = user_collection.find({"_id": {"$in": object_ids}})
    users = []
    for user in cursor:
        users.append({
            "id": str(user["_id"]),
            "username": user["username"],
            "password": user["password"]
        })
    return users
