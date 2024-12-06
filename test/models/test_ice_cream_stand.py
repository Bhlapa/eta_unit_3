from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand:

    def test_flavors_available_lista_preenchida(self):
        # Setup
        ics = IceCreamStand("San Paolo", "Sorvete",["Ninho","Oreo","Doce de Leite"])
        resultado_esperado =f"\nNo momento temos os seguintes sabores de sorvete disponíveis:\n-Ninho\n-Oreo\n-Doce de Leite"

        # Chamada
        resultado = ics.flavors_available()

        # Avalicação
        assert resultado == resultado_esperado

    def test_flavors_available_lista_vazia(self):
        # Setup
        ics = IceCreamStand("San Paolo", "Sorvete",[])
        resultado_esperado = "Estamos sem estoque atualmente!"

        # Chamada
        resultado = ics.flavors_available()

        # Avalicação
        assert resultado == resultado_esperado

    def test_find_flavor_disponivel(self):
        # Setup
        ics = IceCreamStand("San Paolo", "Sorvete", ["Ninho","Oreo","Doce de Leite"])
        resultado_esperado = f"No momento o sabor Oreo está disponivel!"

        # Chamada
        resultado = ics.find_flavor("Oreo")

        # Avalicação
        assert resultado == resultado_esperado

    def test_find_flavor_disponivel_indisponivel(self):
        # Setup
        ics = IceCreamStand("San Paolo", "Sorvete", [])
        resultado_esperado = "Estamos sem estoque atualmente!"

        # Chamada
        resultado = ics.find_flavor("Oreo")

        # Avalicação
        assert resultado == resultado_esperado

    def test_add_flavor_disponivel(self):
        # Setup
        ics = IceCreamStand("San Paolo", "Sorvete", ["Ninho", "Oreo", "Doce de Leite"])
        resultado_esperado = "Pistache adicionado ao estoque!"

        # Chamada
        resultado = ics.add_flavor("Pistache")

        # Avalicação
        assert resultado == resultado_esperado

    def test_add_flavor_indisponivel(self):
        # Setup
        ics = IceCreamStand("San Paolo", "Sorvete", ["Ninho", "Oreo", "Doce de Leite"])
        resultado_esperado = "\nSabor não adicionado, pois já está disponivel para consumo!"

        # Chamada
        resultado = ics.add_flavor("Oreo")

        # Avalicação
        assert resultado == resultado_esperado
