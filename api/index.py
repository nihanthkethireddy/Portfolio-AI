from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"ok": True, "stack": "python-on-vercel"}

@app.get("/health")
def health():
    return {"status": "ok"}
