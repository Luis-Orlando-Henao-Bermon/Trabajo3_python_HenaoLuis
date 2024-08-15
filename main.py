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
                pedidos.append({"cliente":nombreClienteT,"items":DiccionarioE,"estado":"creado","estado_pago":"no pagado","total":total})
                input("Gracias por hacer tu pedido ╰(*°▽°*)╯\nPreciona (Enter) para continuar ")
            else:
                input("Pedido cancelado\nPreciona Enter para continuar ")
    elif opcion==2:
        contPedido=0
        print("-------------- Pedidos no pagados --------------")
        for i in pedidos:
            contPedido+=1
            if i["estado_pago"]=="no pagado":#se usa un bucle for para mirar el json de pedidos y mirar todos los que no esten pagados y mostrarlos con su id en es la posicion en el json
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
        fechaPago=str(datetime.today())
        pedidos[idPedido-1]["estado_pago"]="pagado"#sabiendo la posicion del pedido que se va a pagar se busca en el json ese pedido y se cambia su estado de no pagado a pagado
        pedidos[idPedido-1]["fecha_pago"]=fechaPago#sabiendo la posicion del pedido que se va a pagar se busca en el json ese pedido y se cambia su estado de no pagado a pagado
        
        input("Pedido pagado con exito ╰(*°▽°*)╯\nPreciona (Enter) para continuar")
    elif opcion==3:
        contCambiop=0
        #en la siguiente seccion se usa un buclle while y un try except para evitar cualquier error al momento de pedir un numero y tambien se usa un bucle while para que el numero ingresado no sea diferente de los que aparecen en pantalla
        bolInt=True
        while bolInt==True:
            try:
                opcion3=int(input("1. Pasar pedido de creado a preparacion\n2. pasar pedido de preparacion a servido\n3. Cancelar pedido\nIngresa tu opcion: "))
                while opcion3<1 or opcion3>3:
                    opcion3=int(input("Ingrese una opcion de las que aparecen en pantalla: "))
                bolInt=False
            except ValueError:
                print("Ingrese una opcion valida (Numero)")
        #----------------------------------------------------------------------------------------------------
        if opcion3==1:
            print("==========Pedidos en estado 'creado'==========")
            for i in pedidos:
                contCambiop+=1
                if i["estado"]=="creado":#se usa un bucle for para mirar todos los productos que tienen estado de creado
                    print("ID del pedido:",contCambiop,"\nDueño del pedido:",i["cliente"],"\n-----------------------------------------------")
            #en la siguiente seccion se usa un buclle while y un try except para evitar cualquier error al momento de pedir un numero y tambien se usa un bucle while para que el numero ingresado no sea diferente de los que aparecen en pantalla
            bolInt=True
            while bolInt==True:
                try:
                    cambioCtoP=int(input("Ingresa el id del pedido que va a cambiar de estado: "))
                    while cambioCtoP<1 or cambioCtoP>contCambiop:
                        cambioCtoP=int(input("Ingrese un id de los que aparecen en pantalla: "))
                    bolInt=False
                except ValueError:
                    print("Ingrese una opcion valida (Numero)")
            #----------------------------------------------------------------------------------------------------
            pedidos[cambioCtoP-1]["estado"]="preparacion"#sabiendo la posicion del pedido al que se le cambiara el estado se busca en el json y se le cambia el estado
        elif opcion3==2:
            contCambiop=0
            print("==========Pedidos en estado 'preparacion'==========")
            for i in pedidos:
                contCambiop+=1
                if i["estado"]=="preparacion":#se usa un bucle for para mirar todos los productos que tienen estado de preparacion
                    print("ID del pedido:",contCambiop,"\nDueño del pedido:",i["cliente"],"\n-----------------------------------------------")
            #en la siguiente seccion se usa un buclle while y un try except para evitar cualquier error al momento de pedir un numero y tambien se usa un bucle while para que el numero ingresado no sea diferente de los que aparecen en pantalla
            bolInt=True
            while bolInt==True:
                try:
                    cambioCtoP=int(input("Ingresa el id del pedido que va a cambiar de estado: "))
                    while cambioCtoP<1 or cambioCtoP>contCambiop:
                        cambioCtoP=int(input("Ingrese un id de los que aparecen en pantalla: "))
                    bolInt=False
                except ValueError:
                    print("Ingrese una opcion valida (Numero)")
            #----------------------------------------------------------------------------------------------------

            if pedidos[cambioCtoP-1]["estado_pago"]=="pagado":
                pedidos[cambioCtoP-1]["estado"]="servido"#sabiendo la posicion del pedido al que se le cambiara el estado se busca en el json y se le cambia el estado
            else:
                input("El pedido no a sido pagado por lo tanto no se puede camiar el estado a servido\nPreciona (Enter) para continuar")
        elif opcion3==3:
            contCancelar=0
            for i in pedidos:
                contCancelar+=1
                print("ID del pedido:",contCancelar,"\nDueño del pedido:",i["cliente"],"\n-----------------------------------------------")

            #en la siguiente seccion se usa un buclle while y un try except para evitar cualquier error al momento de pedir un numero y tambien se usa un bucle while para que el numero ingresado no sea diferente de los que aparecen en pantalla
            bolInt=True
            while bolInt==True:
                try:
                    cancelarP=int(input("Ingresa el id del pedido que va a cambiar de estado: "))
                    while cancelarP<1 or cancelarP>contCancelar:
                        cancelarP=int(input("Ingrese un id de los que aparecen en pantalla: "))
                    bolInt=False
                except ValueError:
                    print("Ingrese una opcion valida (Numero)")
            #----------------------------------------------------------------------------------------------------
            if pedidos[cancelarP-1]["estado"]=="creado" and pedidos[cancelarP-1]["estado_pago"]=="no pagado":
                pedidos[cancelarP-1]["estado"]="cancelado"
                input("Pedido cancelado")
            else:
                print("Tu pedido no puede ser cancelado ya que su estado es:",pedidos[cancelarP-1]["estado"],"y su estado de pago es:",pedidos[cancelarP-1]["estado_pago"])
                input("Preciona (Enter) para continuar")

    elif opcion==4:
        DiccionarioE=[]
        modificarP=0
        for i in pedidos:
            modificarP+=1
            print("ID del pedido:",modificarP,"\nDueño del pedido:",i["cliente"],"\n--------------------------------------------")
        
        #en la siguiente seccion se usa un buclle while y un try except para evitar cualquier error al momento de pedir un numero y tambien se usa un bucle while para que el numero ingresado no sea diferente de los que aparecen en pantalla
        bolInt=True
        while bolInt==True:
            try:
                idmodificar=int(input("Ingresa el id del pedido que se quiere modificar: "))
                while idmodificar<1 or idmodificar>modificarP:
                    idmodificar=int(input("Ingrese un id de los que aparecen en pantalla: "))
                bolInt=False
            except ValueError:
                print("Ingrese una opcion valida (Numero)")
        #----------------------------------------------------------------------------------------------------

        if pedidos[idmodificar-1]["estado"]=="creado":
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

            nombreClienteM=pedidos[idmodificar-1]["cliente"]
            pedidos[idmodificar-1]={"cliente":nombreClienteM,"items":DiccionarioE,"estado":"creado","estado_pago":"no pagado"}
            input("modificaste tu pedido con exito ╰(*°▽°*)╯\nPreciona (Enter) para continuar ")
        else:  
            print("Este pedido tiene estado:",pedidos[idmodificar-1]["estado"],"por lo tanto no se puede modificar")
            input("Preciona (Enter) para continuar")

    elif opcion==5:
        #en la siguiente seccion se usa un buclle while y un try except para evitar cualquier error al momento de pedir un numero y tambien se usa un bucle while para que el numero ingresado no sea diferente de los que aparecen en pantalla
        bolInt=True
        while bolInt==True:
            try:
                opcion5=int(input("1. Mostrar todos los pedidos\n2. Mostrar pedido en particular\nIngresa tu opcion: "))
                while opcion5<1 or opcion5>2:
                    opcion5=int(input("Ingrese una opcion de las que aparecen en pantalla: "))
                bolInt=False
            except ValueError:
                print("Ingrese una opcion valida (Numero)")
        #----------------------------------------------------------------------------------------------------
        system("clear")
        if opcion5==1:
            nPedido=0
            for i in pedidos:
                print("Cliente:",i["cliente"],"\n------------------------------------Plato------------------------------------")
                total=0
                for x in pedidos[nPedido]["items"]:
                    print("Categoria del plato:",x["categoria"],"\nNombre del plato:",x["nombre"],"\nPrecio del plato:",x["precio"],"\n-----------------------------------------------------------------------------")
                    total=total+x["precio"]
                
                print("==========Total:",total,"==========\nEstado:",i["estado"],i["estado_pago"],"\n\n************************************************************\n")
                nPedido+=1
            input()
        elif opcion5==2:
            system("clear")
            contPedido=0
            for i in pedidos:
                contPedido+=1
                print("ID:",contPedido,"----- Nombre del cliente dueño del pedido:",i["cliente"],"\n-------------------------------------------------------------------------------")
            #en la siguiente seccion se usa un buclle while y un try except para evitar cualquier error al momento de pedir un numero y tambien se usa un bucle while para que el numero ingresado no sea diferente de los que aparecen en pantalla
            bolInt=True
            while bolInt==True:
                try:
                    idCliente=int(input("Ingresa el id del cliente que quieres ver el pedido: "))
                    while idCliente<1 or idCliente>contPedido:
                        idCliente=int(input("Ingrese un id de los que aparecen en pantalla: "))
                    bolInt=False
                except ValueError:
                    print("Ingrese una opcion valida (Numero)")
            #----------------------------------------------------------------------------------------------------
            system("clear")
            print("==================Pedido==================")
            total=0
            for i in pedidos[idCliente-1]["items"]:
                print("Categoria del plato:",i["categoria"],"\nNombre del plato:",i["nombre"],"\nPrecio del plato:",i["precio"],"\n---------------------------------------------------------------------")
                total=total+i["precio"]

            print("Total:",total,"\nEstado:",pedidos[idCliente-1]["estado"],"\nEstado de pago:",pedidos[idCliente-1]["estado_pago"])
            input()
    elif opcion==6:
        print("Gracias por usar el programa ^_^")
        bol=False
    
#seccion de exportacion de jsons
jsonpedidos=json.dumps(pedidos,indent=4)
with open("./json/pedidos.json","w") as file:
    file.write(jsonpedidos)
jsonpagos=json.dumps(pagos,indent=4)
with open("./json/pagos.json","w") as file:
    file.write(jsonpagos)
jsonmenu=json.dumps(menu,indent=4)
with open("./json/menu.json","w") as file:
    file.write(jsonmenu) 