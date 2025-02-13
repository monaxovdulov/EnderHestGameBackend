from fastapi import FastAPI

chest=[

]
app = FastAPI()


@app.post("/chest/add")
def add_item_to_chest(item_name: str):
    chest.append(item_name)
    return {"message": f"{item_name} added to the chest."}


@app.get("/chest")
def get_chest_contents():
    return {"chest_contents": chest}


@app.delete("/chest/remove/{item_name}")
def remove_item_from_chest(item_name: str):
    if item_name in chest:
        chest.remove(item_name)
        return {"message": f"{item_name} removed from the chest."}

    return {"message": f"{item_name} not found in the chest."}

@app.put("/chest/change/{old_item_name}/{new_item_name}")
def change_item_in_chest(old_item_name: str, new_item_name: str):
    if old_item_name in chest:
        chest[chest.index(old_item_name)] = new_item_name
        return {"message": f"{old_item_name} changed to {new_item_name} in the chest."}

    return {"message": f"{old_item_name} not found in the chest."}

