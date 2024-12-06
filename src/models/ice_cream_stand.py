from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e imprima."""
        if self.flavors:
            result = "\nNo momento temos os seguintes sabores de sorvete disponíveis:"
            for flavor in self.flavors:
                result += f"\n-{flavor}"  #Melhoria /t trocado por /n para uma melhor visualização
            return result
        else:
            return "Estamos sem estoque atualmente!"

    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""
        if self.flavors:
            if flavor in self.flavors:
                return f"No momento o sabor {flavor} está disponivel!"  #Melhoria da frase para o usuário e troca a exibição de todos os sabores por apenas o solicitado
            else:
                return f"No momento não temos {flavor}!"    #Melhoria da frase para o usuário e remoção da exibição de todos os sabores
        else:
            return "Estamos sem estoque atualmente!"

    def add_flavor(self, flavor):
        """Add o sabor informado ao estoque."""
        #Remoção da validação se a lista de sabores está vazia ou não. Essa informação é irrelevante para adicionar um novo sabor
        if flavor in self.flavors:
            return "\nSabor não adicionado, pois já está disponivel para consumo!"    #Melhoria da frase para o usuário
        else:
            self.flavors.append(flavor)
            return f"{flavor} adicionado ao estoque!"

