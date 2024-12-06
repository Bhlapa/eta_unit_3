from src.models.restaurant import Restaurant


class TestRestaurant:

    def test_describe_restaurant_open(self):
        # Setup
        res = Restaurant("San Paolo", "Sorvete")
        resultado_esperado = "Esse restaurante se chama San Paolo, serve Sorvete e serviu 0 consumidores desde que abriu."

        # Chamada
        res.open_restaurant()
        resultado = res.describe_restaurant()

        # Avalicação
        assert resultado == resultado_esperado

    def test_describe_restaurant_closed(self):
        # Setup
        res = Restaurant("San Paolo", "Sorvete")
        resultado_esperado = "Esse restaurante se chama San Paolo, serve Sorvete e está fechado"

        # Chamada
        resultado = res.describe_restaurant()

        # Avalicação
        assert resultado == resultado_esperado

    def test_open_restaurant_closed(self):
        # Setup
        res = Restaurant("San Paolo", "Sorvete")
        resultado_esperado = "San Paolo agora está aberto!"

        # Chamada
        resultado = res.open_restaurant()

        # Avalicação
        assert resultado == resultado_esperado

    def test_open_restaurant_opened(self):
        # Setup
        res = Restaurant("San Paolo", "Sorvete")
        resultado_esperado = "San Paolo já está aberto!"

        # Chamada
        res.open_restaurant()
        resultado = res.open_restaurant()

        # Avalicação
        assert resultado == resultado_esperado


    def test_close_restaurant_opened(self):
        # Setup
        res = Restaurant("San Paolo", "Sorvete")
        resultado_esperado = "San Paolo agora está fechado!"

        # Chamada
        res.open_restaurant()
        resultado = res.close_restaurant()

        # Avalicação
        assert resultado == resultado_esperado

    def test_close_restaurant_closed(self):
        # Setup
        res = Restaurant("San Paolo", "Sorvete")
        resultado_esperado = "San Paolo já está fechado!"

        # Chamada
        resultado = res.close_restaurant()

        # Avalicação
        assert resultado == resultado_esperado

    def test_set_number_served_opened(self):
        # Setup
        res = Restaurant("San Paolo", "Sorvete")
        resultado_esperado = "Pessoas atendidas até o momento: 6"

        # Chamada
        res.open_restaurant()
        resultado = res.set_number_served(6)

        # Avalicação
        assert resultado == resultado_esperado

    def test_set_number_served_closed(self):
        # Setup
        res = Restaurant("San Paolo", "Sorvete")
        resultado_esperado = "San Paolo está fechado!"

        # Chamada
        resultado = res.set_number_served(6)

        # Avalicação
        assert resultado == resultado_esperado

    def test_increment_number_served_opened(self):
        # Setup
        res = Restaurant("San Paolo", "Sorvete")
        resultado_esperado = "Pessoas atendidas até o momento: 12"

        # Chamada
        res.open_restaurant()
        res.increment_number_served(6)
        resultado = res.increment_number_served(6)

        # Avalicação
        assert resultado == resultado_esperado

    def test_increment_number_served_closed(self):
        # Setup
        res = Restaurant("San Paolo", "Sorvete")
        resultado_esperado = "San Paolo está fechado!"

        # Chamada
        resultado = res.increment_number_served(6)

        # Avalicação
        assert resultado == resultado_esperado
