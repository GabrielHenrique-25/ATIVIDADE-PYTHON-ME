class animais:
    def __init__(self, nome , idade, raça, peso, porte, cor, alimentação):
        self.nome = nome
        self.idade = idade
        self.raça = raça
        self.peso = peso
        self.porte = porte
        self.cor = cor
        self.alimentação = alimentação
    
    def informações (self):
        return f"Nome: {self.nome}, Idade = {self.idade}, raça = {self.raça}, peso = {self.peso}, porte = {self.porte}, cor = {self.cor}, alimentação = {self.alimentação}"
    
    def mudando_nome(self,novo_nome):
        self.nome = novo_nome
    def mudando_idade(self,nova_idade):
        self.idade = nova_idade
    def mudando_raça(self,nova_raça):
        self.raça = nova_raça
    def mudando_peso(self,novo_peso):
        self.peso = novo_peso
    def mudando_porte(self,novo_porte):
        self.porte = novo_porte
    def mudando_cor(self,nova_cor):
        self.cor = nova_cor
    def mudando_alimentação(self,nova_alimentação):
        self.alimentação = nova_alimentação

lista_das_informações = []

animal1 = animais("Tayná",6,"Samoida", "40kg", "Grande", "Branco", "Natural")
animal2 = animais("Gabriel",4,"Pastor Alemão","50kg","Grande","Dourado", "Natural")
animal3 = animais("William",4,"Husky siberiano", "27kg", "Grande", "Albino", "Natural")

lista_das_informações.append(animal1)
lista_das_informações.append(animal2)
lista_das_informações.append(animal3)

lista_das_informações[0].mudando_nome("Pedro")
lista_das_informações[0].mudando_idade(10)
lista_das_informações[0].mudando_raça("Golden Retriever")

for animal in lista_das_informações:
    print(animal.informações())