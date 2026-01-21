from pydantic import BaseModel,Field

class UsuarioCreate(BaseModel):
    nome: str = Field(...,min_length = 1 , strip_whitespace=True) # usado para fazer validaçoes  e metadados do campo os tres pontos no começo , e essa string precisa ter pelo menos 1 caractere significa que o campo é obrigatorio 
    idade:int = Field(..., gt = 0) # mesma coisa se aplica para este campo onde se a idade for negativa a API ira retornar um erro 
    ## caso o usuario digite um nome vazio  a api ira retornar erro 

    
class UsuarioOut(BaseModel):
    id: int
    nome: str
    idade : int