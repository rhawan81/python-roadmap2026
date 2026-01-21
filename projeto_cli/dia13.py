class Usuario:
    def __init__(self,Nome,idade):
        self.Nome = Nome
        self.idade = idade
     
     
    def exibir_dados(self):
        return f'Nome: {self.Nome} com idade de {self.idade}'
    
class SistemaUsuario:
    def __init__(self):
        self.usuarios = []

    
    def adicionar_usuario(self,usuario):
        self.usuarios.append(usuario)
        print(f'Usuario {usuario.Nome} adicionado com sucesso!!')
        
    def lista_usuarios(self):
        for user in self.usuarios:
            print(user.exibir_dados())
        
            
jose = Usuario('JOSE', 19)
mauro = Usuario('mauro', 19)
arthur = Usuario('arthur', 28)
michel = Usuario('michel', 28)
sistema  = SistemaUsuario()
sistema.adicionar_usuario(jose)
sistema.adicionar_usuario(mauro)
sistema.adicionar_usuario(arthur)
sistema.adicionar_usuario(michel)


sistema.lista_usuarios()    
   
        