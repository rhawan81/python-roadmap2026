from fastapi import FastAPI
from pydantic import BaseModel ,Field,validator
usuarios_cadastrados = []

class Usuario(BaseModel):
    nome: str = Field(...,min_length = 1) # usado para fazer validaçoes  e metadados do campo os tres pontos no começo , e essa string precisa ter pelo menos 1 caractere significa que o campo é obrigatorio 
    idade:int = Field(..., gt = 0) # mesma coisa se aplica para este campo onde se a idade for negativa a API ira retornar um erro 
    ## caso o usuario digite um nome vazio  a api ira retornar erro 
    @validator('nome')
    def nome_vazio(cls,value):
        if value.strip() == "":
            raise ValueError('Nome nao pode ser vazio')
        
        return value

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
    for p, item in enumerate(usuarios_cadastrados):
        if item['id'] == id:
            usuarios_cadastrados.pop(p)
            return {'mensagem': 'Usuario  removido com sucesso'}
    return {'mensagem': 'Usuario nao foi encontrado'}
