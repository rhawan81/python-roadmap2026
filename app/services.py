usuarios_cadastrados  = []
next_id = 1

def cadastrar_user(nome: str,idade: int) -> dict:
    global next_id 
    novo_usuario = {'id': next_id ,   
        "nome": nome , 
        'idade': idade}
    usuarios_cadastrados.append(novo_usuario)
    next_id += 1
    return novo_usuario

def mostrar_cadastros() -> list[dict]:
   return usuarios_cadastrados
    

def deletar_user(user_id: int) -> bool:
    for p, item in enumerate(usuarios_cadastrados):
        if item['id'] == user_id:
            usuarios_cadastrados.pop(p)
            return True
    return False
