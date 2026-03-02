class ItemBiblioteca:
    def __init__ (self,codigo:str, titulo:str, ano:int, disponivel:bool):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__disponivel = disponivel

    def exibir_detalhes(self):
        print(f"Código: {self.__codigo}")
        print(f"Título: {self.__titulo}")
        print(f"Ano: {self.__ano}")

    def emprestar(self):
        if self.__disponivel == False:
            print("O item não está disponível para empréstimo.")
        else:
            self.__disponivel = False
            print("Empréstimo realizado com sucesso.")

    def devolver(self):
        if self.__disponivel == True:
            print("O item já está disponível na biblioteca.")
        else:
            self.__disponivel = True
            print("Devolução realizada com sucesso.")

    def set_validacao(self, codigo:str, titulo:str, ano:int):
        if len(codigo) == 0:
            print("Código inválido. O código não pode ser vazio.")
        else:
            self.__codigo = codigo
        if len(titulo) == 0:
            print("Título inválido. O título não pode ser vazio.")
        else:
            self.__titulo = titulo
        if ano < 0:
            print("Ano inválido. O ano não pode ser negativo.")
        else:
            self.__ano = ano
            
    def get_codigo(self):
        return self.__codigo
