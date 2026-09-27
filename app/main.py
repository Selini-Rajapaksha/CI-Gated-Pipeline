from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "CI Pipeline Demo"}


@app.get("/health")
def health():
    return {"status": "ok"}