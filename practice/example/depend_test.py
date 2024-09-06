from fastapi import FastAPI, Depends, Query

app = FastAPI()

def user_dep(name: str = Query(...), gender: str = Query(...)):
    return {"name": name, "gender": gender}

@app.get("/user")
def get_user(user: dict = Depends(user_dep)):
    return user