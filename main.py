from fastapi import FastAPI, HTTPException
from schemas import (
    User, UpdateUser, UserResponse,
    MessageResponse, CreateResponse,
    UserListInput, UserListResponse
)
import crud

app = FastAPI()

@app.post("/create", response_model=CreateResponse)
def create(user: User):
    user_id = crud.create_user(user.model_dump())
    return {"message": "User created", "id": user_id}

@app.get("/read/{user_id}", response_model=UserResponse)
def read(user_id: str):
    user = crud.read_user_by_id(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")

@app.put("/update/{user_id}", response_model=MessageResponse)
def update(user_id: str, update_data: UpdateUser):
    success = crud.update_username(user_id, update_data.username)
    if success:
        return {"message": "Username updated"}
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/delete/{user_id}", response_model=MessageResponse)
def delete(user_id: str):
    success = crud.delete_user(user_id)
    if success:
        return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/list", response_model=UserListResponse)
def list_users(input_data: UserListInput):
    users = crud.list_users_by_ids(input_data.ids)
    return {"users": users}
