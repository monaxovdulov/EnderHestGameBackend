from fastapi import FastAPI, Depends, HTTPException, status

users = {
    'test': '123qwerty'
}

chest = [
    {'test': 'hello world'}
]

app = FastAPI()

def authenticate_user(username: str, password: str):
    if username in users and users[username] == password:
        return True
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

@app.post('/register')
def register(username: str, password: str):
    if username in users:
        return {"message": f"User {username} already exists."}
    users[username] = password
    return {"message": f"User {username} registered successfully."}

@app.post('/login')
def login(username: str, password: str):
    if authenticate_user(username, password):
        return {"message": "Logged in successfully."}

@app.post("/chest/add")
def add_item_to_chest(item: str, username: str, password: str):
    authenticate_user(username, password)
    chest.append({username: item})
    return {"message": f"{item} from {username} added to the chest."}

@app.get("/chest")
def get_chest_contents(username: str, password: str):
    authenticate_user(username, password)
    return {"chest_contents": chest}

@app.delete("/chest/remove/{item_index}")
def remove_item_from_chest(item_index: int, username: str, password: str):
    authenticate_user(username, password)
    if 0 <= item_index < len(chest):
        removed_item = chest.pop(item_index)
        return {"message": f"Removed {removed_item} from the chest."}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

@app.put("/chest/change/{old_item}/{new_item}")
def change_item_in_chest(old_item: str, new_item: str, username: str, password: str):
    authenticate_user(username, password)
    for item in chest:
        if item.get(username) == old_item:
            item[username] = new_item
            return {"message": f"{old_item} changed to {new_item}"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Old item not found")
