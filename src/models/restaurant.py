class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def describe_restaurant(self):
        """Imprima uma descrição simples da instância do restaurante."""
        result = f"Esse restaurante se chama {self.restaurant_name}, serve {self.cuisine_type}"   #Bug - Tipo do nome incorreto e ajuste da frase
        if self.open:
            result += f" e serviu {self.number_served} consumidores desde que abriu."  # Melhoria indicando se o restaurante está aberto ou fechado e ajuste da frase
        else:
            result += f" e está fechado"
        return result

    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""
        if not self.open:
            self.open = True    #BUG = Open estava False e foi modificado para True
            self.number_served = 0  #Melhoria - Pessoas servidas foi mudado de -2 para 0
            return f"{self.restaurant_name} agora está aberto!"
        else:
            return f"{self.restaurant_name} já está aberto!"

    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""
        if self.open:
            self.open = False
            self.number_served = 0
            return f"{self.restaurant_name} agora está fechado!"
        else:
            return f"{self.restaurant_name} já está fechado!"

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""
        if self.open:
            self.number_served = total_customers
            return f"Pessoas atendidas até o momento: {self.number_served}"  #Melhoria - Mensagem informando numero de consumidores adicionada
        else:
            return f"{self.restaurant_name} está fechado!"

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        if self.open:
            self.number_served = self.number_served + more_customers    #BUG - Aplicação estava definindo um número de pessoas atendidas ao invés de somar
            return f"Pessoas atendidas até o momento: {self.number_served}"   #Melhoria - Mensagem informando numero de consumidores atual
        else:
            return f"{self.restaurant_name} está fechado!"
