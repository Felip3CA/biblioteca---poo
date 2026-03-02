import item_biblioteca

class Livro(item_biblioteca.ItemBiblioteca):
    def __init__(self, codigo: str, titulo: str, ano: int, autor: str, num_paginas: str):
        super().__init__(codigo, titulo, ano, True)
        self.__autor = autor
        self.__num_paginas = num_paginas

    def exibir_detalhes(self):
        super().exibir_detalhes()
        print(f"Autor: {self.__autor}")
        print(f"Número de páginas: {self.__num_paginas}")

    def get_autor(self):
        return self.__autor

    def get_num_paginas(self):
        return self.__num_paginas
