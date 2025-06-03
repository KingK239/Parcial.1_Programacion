from Inputs import pedir_opcion_menu
from Funciones import *

participantes = []
datos_cargados = False


def verificar_datos():
    if datos_cargados:
        return True
    else:
        return False

while True:
    print("\n===================== MENU PRINCIPAL =========================")
    print()
    print("1. Cargar participantes")
    print("2. Cargar puntajes")
    print("3. Mostrar puntajes")
    print("4. Promedios > 4")
    print("5. Promedios > 7")
    print("6. Promedio por jurado")
    print("7. Jurado mas estricto")
    print("8. Buscar participante")
    print("9. Top 3")
    print("10. Orden alfabetico")
    print("0. Salir")
    print()
    print("=================================================================")

    opcion = pedir_opcion_menu()

    if opcion == 1:
        participantes = cargar_participantes()
        datos_cargados = False
    elif opcion == 2:
        if len(participantes) > 0:
            cargar_puntajes(participantes)
            datos_cargados = True
        else:
            print("ERROR: NO hay datos cargados de ningun participante.")
    elif opcion == 3 and datos_cargados:
        mostrar_puntajes(participantes)
    elif opcion == 4 and datos_cargados:
        mostrar_promedios_mayores(participantes, 4)
    elif opcion == 5 and datos_cargados:
        mostrar_promedios_mayores(participantes, 7)
    elif opcion == 6 and datos_cargados:
        promedio_por_jurado(participantes)
    elif opcion == 7 and datos_cargados:
        jurado_estricto(participantes)
    elif opcion == 8 and datos_cargados:
        buscar_participante(participantes)
    elif opcion == 9 and datos_cargados:
        top3(participantes)
    elif opcion == 10 and datos_cargados:
        ordenar_alfabetico(participantes)
    elif opcion == 0:
        print("Espero haber cumplido con todo :).")
        break
    else:
        print("ERROR: Primero tenes que cargar los datos de los participantes y sus puntajes.")
