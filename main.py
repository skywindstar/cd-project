from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"hello,world"}

@app.get("/employees")
def get_imployees(name):
    return{f"{name}님, 환영합니다!"}