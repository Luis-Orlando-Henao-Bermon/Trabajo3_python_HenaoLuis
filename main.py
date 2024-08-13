import json
from datetime import datetime
from os import system


with open ("./json/menu.json", encoding="UTF-8") as file:
    menu=json.load(file)
with open ("./json/pagos.json", encoding="UTF-8") as file:
    pagos=json.load(file)
with open ("./json/pedidos.json", encoding="UTF-8") as file:
    pedidos=json.load(file)


try:
    ""
except ValueError:
    ""
bol=True

while bol==True:
    system("clear") 
    print("==========Menu==========\n1. Hacer pedido\n2. Pagar pedido\n3. Cambiar estado de pedido\n4. Moificar pedidos\n5. Mostrar pedidos\n6. Salir")
    bolInt=True
    while bolInt==True:
        try:
            opcion=int(input("Ingresa tu opcion: "))
            while opcion<1 or opcion>6:
                opcion=int(input("Ingrese una opcion valida: "))
            bolInt=False
        except ValueError:
            print("Ingrese una opcion valida (Numero)")

    system("clear")
    if opcion==1:
        DiccionarioE=[]
        nombreCliente=input("Ingresa el nombre del cliente que realiza el pedido\n")
        system("clear")
        entrada=input("¿El cliente desea plato de entrada? (s/n)\n")
        while entrada=="s":
                cantPlato=0
                print("-----Entradas-----")
                for i in menu:
                    if i["categoria"]=="entrada":
                        print(" ID:",i["id"],"\n","Nombre",i["nombre"],"\n","Precio",i["precio"],"\n----------------------")
                        cantPlato+=1
                
                bolInt=True
                while bolInt==True:
                    try:
                        idCliete=int(input("Ingresa el id del plato que quiere el cliente: "))
                        while idCliete<1 or idCliete>cantPlato:
                            idCliete=int(input("Ingrese un id de los que aparecen en pantalla: "))
                        bolInt=False
                    except ValueError:
                        print("Ingrese una opcion valida (Numero)")

                for i in menu:
                    if i["categoria"]=="entrada" and i["id"]==idCliete:
                        datos={"categoria":i["categoria"],"nombre":i["nombre"],"precio":i["precio"]}
                DiccionarioE.append(datos)
                entrada=input("¿Quieres otras entrada mas? (s/n)")
                system("clear")

        platoFuerte=input("¿El cliente desea plato fuerte? (s/n)\n")
        while platoFuerte=="s":
                cantPlato=0
                print("-----Platos Fuertes-----")
                for i in menu:
                    if i["categoria"]=="plato_fuerte":
                        print(" ID:",i["id"],"\n","Nombre",i["nombre"],"\n","Precio",i["precio"],"\n----------------------")
                        cantPlato+=1
                
                bolInt=True
                while bolInt==True:
                    try:
                        idCliete=int(input("Ingresa el id del plato que quiere el cliente: "))
                        while idCliete<1 or idCliete>cantPlato:
                            idCliete=int(input("Ingrese un id de los que aparecen en pantalla: "))
                        bolInt=False
                    except ValueError:
                        print("Ingrese una opcion valida (Numero)")

                for i in menu:
                    if i["categoria"]=="plato_fuerte" and i["id"]==idCliete:
                        datos={"categoria":i["categoria"],"nombre":i["nombre"],"precio":i["precio"]}
                DiccionarioE.append(datos)
                platoFuerte=input("¿Quieres otras entrada mas? (s/n)")
                system("clear")

    elif opcion==2:
        print(DiccionarioE)
        input()
    elif opcion==3:
        ""
    elif opcion==4:
        ""
    elif opcion==5:
        ""
    elif opcion==6:
        print("Gracias por usar el programa ^_^")
        bol=False
    

jsonpedidos=json.dumps(pedidos)
with open("./json/pedidos.json","w") as file:
    file.write(jsonpedidos)
jsonpagos=json.dumps(pagos)
with open("./json/pagos.json","w") as file:
    file.write(jsonpagos)
jsonmenu=json.dumps(menu)
with open("./json/menu.json","w") as file:
    file.write(jsonmenu)