from item import Item


class Sistema:
    def __init__(self):
        self.items = []
        
    def menu(self):
        while True:
            print("""1.Mostrar Menu
    2.Cadastrar Item
    3. Listar Items
    4.Sair""")
            try:
                opcao = int(input('Escolha oque deseja fazer'))
            except ValueError:
                
                print('valor invalido tente novamente')
                continue
            if opcao == 1:
                continue
            elif opcao == 2:
                self.cadastrar_item()
            elif opcao == 3:
                self.listar_items()
            elif opcao == 4:
                 print('saindo do sistema')
                 break
               
                
    def cadastrar_item(self):
        nome = input('Nome: ').strip()
        while True:
            try: 
                idade = int(input('Idade:'))
                break
            except ValueError:
                print('idade invalida . digite um numero')
                
        item = Item(nome,idade)
        self.items.append(item)
    
        print(f'Item {item.nome} cadastrado com sucesso !')
        
    def listar_items(self):
        if not self.items:
            print('Nenhum item cadastrado ainda ')
            return
        print("\n=== ITENS CADASTRADOS ===")
        for i , item in enumerate(self.items,start=1):
            print(f'{i} . {item.exibir()}')
        

if __name__ == "__main__":
    sistema = Sistema()
    sistema.menu()