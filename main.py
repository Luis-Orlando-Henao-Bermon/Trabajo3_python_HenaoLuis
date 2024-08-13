import json
from datetime import datetime
from os import system


with open ("./json/menu.json", encoding="UTF-8") as file:
    menu=json.load(file)
with open ("./json/pagos.json", encoding="UTF-8") as file:
    pagos=json.load(file)
with open ("./json/pedidos.json", encoding="UTF-8") as file:
    pedidos=json.load(file)

bol=True

while bol==True:

    opcion=input("Menu\n1. Hacer pedido\n2. Pagar pedido")



jsonpedidos=json.dumps(pedidos)
with open("./pedidos.json","w") as file:
    file.write(jsonpedidos)
jsonpagos=json.dumps(pagos)
with open("./pagos.json","w") as file:
    file.write(jsonpagos)
jsonmenu=json.dumps(menu)
with open("./menu.json","w") as file:
    file.write(jsonmenu)