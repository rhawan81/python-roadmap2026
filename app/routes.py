from fastapi import APIRouter, HTTPException
from schemas import UsuarioCreate, UsuarioOut
import services

router = APIRouter()

@router.post("/users", response_model=UsuarioOut, status_code=201)
def cadastrar_user(dados: UsuarioCreate):
    return services.cadastrar_user(dados.nome, dados.idade)

@router.get("/users", response_model=list[UsuarioOut])
def mostrar_cadastros():
    return services.mostrar_cadastros()

@router.delete("/users/{user_id}", status_code=204)
def deletar_user(user_id: int):
    ok = services.deletar_user(user_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Usuario nao encontrado")
    return
