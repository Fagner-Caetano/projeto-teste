from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    """Retorna uma mensagem de boas-vindas."""
    return {"message": "Hello World"}