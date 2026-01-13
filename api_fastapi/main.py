from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def exibir():
    return {f'API FUNCIONANDO CORRETAMENTE ! '}


