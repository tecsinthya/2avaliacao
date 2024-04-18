class Cliente:

    def __init__(self, nome, anodenascimento, sexo, limite, endereco):
        self.nome = nome
        self.anodenascimento = anodenascimento 
        self.sexo = sexo 
        self.limite = limite 
        self.endereco = endereco

    def Imprimir(self):
        print(self.nome)
        print(self.anodenascimento)
        print(self.sexo)
        print(self.limite)
        print(self.endereco)


cliente1 = Cliente("Sinthya", 2007 , "F", 7000, "rua Vicente Biella")  
cliente1.Imprimir()

