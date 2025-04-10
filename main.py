from fastapi import FastAPI

app = FastAPI()

# Link de acesso no navegador - http://127.0.0.1:8000
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Link de acesso no navegador - http://127.0.0.1:8000/teste1
@app.get("/teste1")
async def root():
    return {"Funcinou"}

