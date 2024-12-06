from src.models.restaurant import Restaurant
from src.models.ice_cream_stand import IceCreamStand


res = Restaurant("Italiano", "Massa")
ics = IceCreamStand("San Paolo","Sorvete",["Ninho","Oreo","Doce de Leite"])



print(ics.flavors_available())
print(ics.add_flavor("Pìstache"))
print(ics.flavors_available())





