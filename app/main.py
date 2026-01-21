from fastapi import FastAPI
from routes import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def healthcheck():
    return {"status": "ok", "message": "API funcionando corretamente"}
