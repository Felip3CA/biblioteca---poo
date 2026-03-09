class Biblioteca: 
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def listar_itens(self):
        for item in self.itens:
            print(f"{item.titulo} por {item.autor}")

    def buscar_por_codigo(self, codigo):
        for item in self.itens:
            if item.codigo == codigo:
                return item
    
    def emprestar_item(self, codigo):
        item = self.buscar_por_codigo(codigo)
        if item and not item.emprestado:
            item.emprestado = True
            print(f"{item.titulo} emprestado com sucesso!")
        else:
            print("Item não disponível para empréstimo.")
    
    def devolver_item(self, codigo):
        item = self.buscar_por_codigo(codigo)
        if item and item.emprestado:
            item.emprestado = False
            print(f"{item.titulo} devolvido com sucesso!")
        else:
            print("Item não encontrado ou não está emprestado.")