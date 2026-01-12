from item import Item


class Sistema:
    def __init__(self):
        self.items = []
        
    def menu(self):
        while True:
            print("""1.Mostrar Menu
    2.Cadastrar Item
    3. Listar Items
    4.Remover items
    5.Sair""")
            try:
                opcao = int(input('Escolha oque deseja fazer'))
                if opcao > 5:
                    print('Valor invalido de menu')
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
                try:
                    indice = int(input('Oque deseja remover ? '))
                except ValueError:
                    print('Digite um valor valido')
                    continue
                self.remover_item(indice) # chamamos apenas a funçao junto com a variavel que pede , e removemos o metodo print pois ira causar confusao
            elif opcao == 5:
                print('saindo do programa')
                break      
              
               
                
    def cadastrar_item(self):
        nome = input('Nome: ').strip()
        while True:
            try: 
                idade = int(input('Idade:'))
                if idade <= 0:
                    print('Digite uma idade maior que zero')
                    continue
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
            
    def remover_item(self, indice_item):
        item_removido = indice_item - 1
         
        if 0 <= item_removido < len(self.items):
                item_remove = self.items.pop(item_removido)
                print(f'ITEM {item_remove} foi removido com sucesso')
        else:
                print('Indice invalido !')
        

if __name__ == "__main__":
    sistema = Sistema()
    sistema.menu()