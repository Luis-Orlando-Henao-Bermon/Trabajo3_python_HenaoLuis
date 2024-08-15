import json
from datetime import datetime
from os import system

#seccion de importacion de jsons
with open ("./json/menu.json", encoding="UTF-8") as file:
    menu=json.load(file)
with open ("./json/pagos.json", encoding="UTF-8") as file:
    pagos=json.load(file)
with open ("./json/pedidos.json", encoding="UTF-8") as file:
    pedidos=json.load(file)

bol=True
while bol==True:#se usa un bucle while con el fin de que cada vez que se termine una opcion vuelva al menu principal
    system("clear") 
    print("==========Menu==========\n1. Hacer pedido\n2. Pagar pedido\n3. Cambiar estado de pedido\n4. Moificar pedidos\n5. Mostrar pedidos\n6. Salir")
    #en la siguiente seccion se usa un buclle while y un try except para evitar cualquier error al momento de pedir un numero
    bolInt=True
    while bolInt==True:
        try:
            opcion=int(input("Ingresa tu opcion: "))
            while opcion<1 or opcion>6:
                opcion=int(input("Ingrese una opcion valida: "))
            bolInt=False
        except ValueError:
            print("Ingrese una opcion valida (Numero)")
#------------------------------------------------------------------------------------------------------------------------

    system("clear")
    if opcion==1:
        DiccionarioE=[]
        nombreCliente=input("Ingresa el nombre del cliente que realiza el pedido\n")
        nombreClienteT=nombreCliente.title() #al tener el nombre del cliente se usa el .title para que pase la primera letra de cada palabra a mayuscula esto con el fin de que en el json tengan todos los nombres de cliente esta estructura
        confi="no"#esta variable se usa en el caso de que el cliente ingresado anteriormenete no tenga ningun pedido en proceso
        for i in pedidos:
            if i["cliente"]==nombreClienteT and (i["estado"]=="creado" or i["estado"]=="preparacion"):#con e bucle for y la condicional if se mira si el nombre ingresado ya esta en el json de pedidos y si su estado es creado o preparacion si es asi se le informa que no puede hacer ningun pedido
                print("El estado de tu pedido es:'",i["estado"], "' por lo tanto no puedes hacer otro pedido aun\npreciona (Enter) para continuar")
                input()
                confi="si"
        
        if confi != "si":    
            system("clear")
            entrada=input("¿El cliente desea plato de entrada? (s/n)\n")
            while entrada=="s":
                    cantPlato=0
                    print("-----Entradas-----")
                    for i in menu:
                        if i["categoria"]=="entrada":#se usa un bucle for y una condicional if para mostrar todos los id, nombresy precios que hay en el json de menu y que estan en la categoria entrada
                            print(" ID:",i["id"],"\n","Nombre:",i["nombre"],"\n","Precio:",i["precio"],"\n----------------------")
                            cantPlato+=1#este es un contador que se usa para saber cuantas comidas hay en la categoria entrada
                    #en la siguiente seccion se usa un buclle while y un try except para evitar cualquier error al momento de pedir un numero y tambien se usa un bucle while para que el numero ingresado no sea diferente de los que aparecen en pantalla
                    bolInt=True
                    while bolInt==True:
                        try:
                            idCliete=int(input("Ingresa el id del plato que quiere el cliente: "))
                            while idCliete<1 or idCliete>cantPlato:
                                idCliete=int(input("Ingrese un id de los que aparecen en pantalla: "))
                            bolInt=False
                        except ValueError:
                            print("Ingrese una opcion valida (Numero)")
                    #----------------------------------------------------------------------------------------------------
                    for i in menu:
                        if i["categoria"]=="entrada" and i["id"]==idCliete:#se usa un bucle for para mirar que producto tiene ese id y tambien tenga la categoria entrada y toma el nombre, categoria y precio y los agrega al diccionario datos 
                            datos={"categoria":i["categoria"],"nombre":i["nombre"],"precio":i["precio"]}
                    DiccionarioE.append(datos)#despues de tener los datos del producto que se desea se agregan al diccionario DiccionarioE. Este contendra todos los productos que se vallan a tener el el pedido
                    entrada=input("¿Quieres otra entrada? (s/n)\n")#se pregunta si quiere otra entrada en caso de que diga que si se repetira el proceso usando el bucle while
                    system("clear")

            platoFuerte=input("¿El cliente desea plato fuerte? (s/n)\n")
            while platoFuerte=="s":
                    cantPlato=0
                    print("-----Platos Fuertes-----")
                    for i in menu:
                        if i["categoria"]=="plato_fuerte":#se usa un bucle for y una condicional if para mostrar todos los id, nombresy precios que hay en el json de menu y que estan en la categoria plato_fuerte
                            print(" ID:",i["id"],"\n","Nombre:",i["nombre"],"\n","Precio:",i["precio"],"\n----------------------")
                            cantPlato+=1

                    #en la siguiente seccion se usa un buclle while y un try except para evitar cualquier error al momento de pedir un numero y tambien se usa un bucle while para que el numero ingresado no sea diferente de los que aparecen en pantalla
                    bolInt=True
                    while bolInt==True:
                        try:
                            idCliete=int(input("Ingresa el id del plato que quiere el cliente: "))
                            while idCliete<1 or idCliete>cantPlato:
                                idCliete=int(input("Ingrese un id de los que aparecen en pantalla: "))
                            bolInt=False
                        except ValueError:
                            print("Ingrese una opcion valida (Numero)")
                    #----------------------------------------------------------------------------------------------------

                    for i in menu:
                        if i["categoria"]=="plato_fuerte" and i["id"]==idCliete:#se usa un bucle for para mirar que producto tiene ese id y tambien tenga la categoria entrada y toma el nombre, categoria y precio y los agrega al diccionario datos 
                            datos={"categoria":i["categoria"],"nombre":i["nombre"],"precio":i["precio"]}
                    DiccionarioE.append(datos)#despues de tener los datos del producto que se desea se agregan al diccionario DiccionarioE. Este contendra todos los productos que se vallan a tener el el pedido
                    platoFuerte=input("¿Quieres otro plato fuerte? (s/n)\n")#se pregunta si quiere otro plato fuerte en caso de que diga que si se repetira el proceso usando el bucle while
                    system("clear")

            bebida=input("¿El cliente desea bebida? (s/n)\n")
            while bebida=="s":
                    cantPlato=0
                    print("-----Bebidas-----")
                    for i in menu:
                        if i["categoria"]=="bebida":#se usa un bucle for y una condicional if para mostrar todos los id, nombresy precios que hay en el json de menu y que estan en la categoria bebida
                            print(" ID:",i["id"],"\n","Nombre:",i["nombre"],"\n","Precio:",i["precio"],"\n----------------------")
                            cantPlato+=1

                    #en la siguiente seccion se usa un buclle while y un try except para evitar cualquier error al momento de pedir un numero y tambien se usa un bucle while para que el numero ingresado no sea diferente de los que aparecen en pantalla
                    bolInt=True
                    while bolInt==True:
                        try:
                            idCliete=int(input("Ingresa el id del plato que quiere el cliente: "))
                            while idCliete<1 or idCliete>cantPlato:
                                idCliete=int(input("Ingrese un id de los que aparecen en pantalla: "))
                            bolInt=False
                        except ValueError:
                            print("Ingrese una opcion valida (Numero)")
                    #----------------------------------------------------------------------------------------------------

                    for i in menu:
                        if i["categoria"]=="bebida" and i["id"]==idCliete:#se usa un bucle for para mirar que producto tiene ese id y tambien tenga la categoria entrada y toma el nombre, categoria y precio y los agrega al diccionario datos 
                            datos={"categoria":i["categoria"],"nombre":i["nombre"],"precio":i["precio"]}
                    DiccionarioE.append(datos)#despues de tener los datos del producto que se desea se agregan al diccionario DiccionarioE. Este contendra todos los productos que se vallan a tener el el pedido
                    bebida=input("¿Quieres otra bebida? (s/n)\n")#se pregunta si quiere otra bebida en caso de que diga que si se repetira el proceso usando el bucle while
                    system("clear")
            print("---------Pedido----------")
            for i in DiccionarioE:#se usa un bucle for en DiccionarioE para mostrar el tipo de plato(categoria), nombre del plato y precio de los productos que quiere el cliente en el pedido
                print("Tipo de plato:",i["categoria"]," ----- Nombre del plato:",i["nombre"]," ----- Precio:",i["precio"],"\n------------------------------------")
            total=0
            for i in DiccionarioE:#se usa un bucle for para mirar los precios de todos los productos del pedido y sumarlos y mostrar el total de los productos
                total=total+i["precio"]
            print("===== Total:",total,"=====")
            cancelar=input("Escribe (s) para confirmar el pedido o (n) para cancelarlo\n")
            if cancelar=="s":#si el pedido se confirma se agregan el nombre del cliente, productos estado(se pone por defecto en creado) y estado_pago (se pone por defecto en no pagado)
                pedidos.append({"cliente":nombreClienteT,"items":DiccionarioE,"estado":"creado","estado_pago":"no pagado"})
                input("Gracias por hacer tu pedido ╰(*°▽°*)╯\nPreciona (Enter) para continuar ")
            else:
                input("Pedido cancelado\nPreciona Enter para continuar ")
    elif opcion==2:
        contPedido=0
        print("-------------- Pedidos no pagados --------------")
        for i in pedidos:
            contPedido+=1
            if i["estado_pago"]=="no pagado":
                print("ID del pedido:",contPedido,"Dueño del pedido:",i["cliente"])
       #en la siguiente seccion se usa un buclle while y un try except para evitar cualquier error al momento de pedir un numero y tambien se usa un bucle while para que el numero ingresado no sea diferente de los que aparecen en pantalla
        bolInt=True
        while bolInt==True:
            try:
                idPedido=int(input("Ingresa el id del pedido que va a ser pagado: "))
                while idPedido<1 or idPedido>contPedido:
                    idPedido=int(input("Ingrese un id de los que aparecen en pantalla: "))
                bolInt=False
            except ValueError:
                print("Ingrese una opcion valida (Numero)")
        #----------------------------------------------------------------------------------------------------
        pedidos[idPedido-1]["estado_pago"]="pagado"

        input("Pedido pagado con exito ╰(*°▽°*)╯\nPreciona (Enter) para continuar")
    elif opcion==3:
        ""
    elif opcion==4:
        ""
    elif opcion==5:
        ""
    elif opcion==6:
        print("Gracias por usar el programa ^_^")
        bol=False
    
#seccion de exportacion de jsons
jsonpedidos=json.dumps(pedidos)
with open("./json/pedidos.json","w") as file:
    file.write(jsonpedidos)
jsonpagos=json.dumps(pagos)
with open("./json/pagos.json","w") as file:
    file.write(jsonpagos)
jsonmenu=json.dumps(menu)
with open("./json/menu.json","w") as file:
    file.write(jsonmenu) 