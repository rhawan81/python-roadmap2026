from fastapi import FastAPI,HTTPException
from pydantic import BaseModel ,Field,validator
usuarios_cadastrados = []

class UsuarioCreate(BaseModel):
    nome: str = Field(...,min_length = 1 , strip_whitespace=True) # usado para fazer validaçoes  e metadados do campo os tres pontos no começo , e essa string precisa ter pelo menos 1 caractere significa que o campo é obrigatorio 
    idade:int = Field(..., gt = 0) # mesma coisa se aplica para este campo onde se a idade for negativa a API ira retornar um erro 
    ## caso o usuario digite um nome vazio  a api ira retornar erro 

    
class UsuarioOut(BaseModel):
    id: int
    nome: str
    idade : int

app = FastAPI()

@app.get("/")
def exibir():
    return {"status": "ok", "message":"API funcionando corretamente"}
@app.post('/users', response_model=UsuarioOut, status_code=201)
def cadastrar_user(dados: UsuarioCreate):
    novo_usuario = {'id': 
        len(usuarios_cadastrados) + 1 , 
        "nome": dados.nome , 
        'idade':dados.idade}
    usuarios_cadastrados.append(novo_usuario)
    return novo_usuario



@app.get('/users', response_model=list[UsuarioOut])
def mostrar_cadastros():
   return usuarios_cadastrados
    
@app.delete("/users/{id}", status_code=204)
def deletar_user(id:int):
    for p, item in enumerate(usuarios_cadastrados):
        if item['id'] == id:
            usuarios_cadastrados.pop(p)
            return 
    raise HTTPException(status_code = 404 , detail= "Usuario nao foi encontrado")
