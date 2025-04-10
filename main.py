from fastapi import FastAPI

app = FastAPI()

# Link de acesso no navegador - http://127.0.0.1:8000
@app.get("/")
async def root():
    return {"message": "Hello World"}



