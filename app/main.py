from fastapi import FastAPI

app = FastAPI(title="DevSecOps Demo App")

@app.get("/")
def read_root():
    return {"message": "Hello DevSecOps"}

@app.get("/user/{username}")
def read_user(username: str):
    return {"user": username}
