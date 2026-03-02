import item_biblioteca

class Revista(item_biblioteca.ItemBiblioteca):
    def __init__(self, codigo: str, titulo: str, ano: int, edicao: str, mes: str):
        super().__init__(codigo, titulo, ano, True)
        self.__edicao = edicao
        self.__mes = mes

    def exibir_detalhes(self):
        super().exibir_detalhes()
        print(f"Edição: {self.__edicao}")
        print(f"Mês: {self.__mes}")

    def get_edicao(self):
        return self.__edicao

    def get_mes(self):
        return self.__mes
