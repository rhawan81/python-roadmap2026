from fastapi import FastAPI
from pydantic import BaseModel
usuarios_cadastrados = []

class Usuario(BaseModel):
    nome: str
    idade:int
    

app = FastAPI()

@app.get("/")
def exibir():
    return {f'API FUNCIONANDO CORRETAMENTE ! '}
@app.post('/usuario')
def cadastrar_user(dados: Usuario):
    novo_usuario = {'id': len(usuarios_cadastrados) + 1 , "nome": dados.nome , 'idade':dados.idade}
    usuarios_cadastrados.append(novo_usuario)
    return {'Mensagem': 'Usuario Criado com sucesso', 'Usuario:': novo_usuario}



@app.get('/users_cadastrados')
def mostrar_cadastros():
    return {'Mensagem:' 'Usuarios cadastrados': usuarios_cadastrados}
    
    
@app.delete("/deletar_user/{id}")
def deletar_user(id:int):
    for p in usuarios_cadastrados:
        if p['id'] == id:
            usuarios_cadastrados.pop(p)
            return {'mensagem': 'Usuario  removido com sucesso'}
    return {'mensagem': 'Usuario nao foi encontrado'}
