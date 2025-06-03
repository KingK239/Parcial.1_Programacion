def pedir_opcion_menu():
    while True:
        texto = input("Opcion: ")
        try:
            numero = int(texto)
            if 0 <= numero <= 10:
                return numero
            else:
                print("ERROR: Debe ser un numero entre 0 y 10.")
        except:
            print("ERROR: Ingresa un numero valido.")
