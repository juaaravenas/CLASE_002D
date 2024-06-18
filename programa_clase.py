from os import system
lista_trabajador =[]

def menu_principal():
    opciones = {
        '1': ('Registrar trabajador', reg_trabajador),
        '2': ('Listar todos los trabajadores', lis_trabajador),
        '3': ('Imprimir planilla de sueldos', imp_trabajador),
        '4': ('Salir del Programa', salir)
    }

    generar_menu(opciones, '4')

def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        system("cls")
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print() # se imprime una línea en blanco para clarificar la salida por pantalla

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def reg_trabajador():
    system("cls")
    nombres = input("Ingrese  nombre  y Apellido del trabajador ")
    cargo   = input("Ingrese el cargo del trabajador ")
    sueldo_bruto = int(input("Ingrese el sueldo bruto del Trabajador "))
    desc_salud =  int(round(sueldo_bruto *  7/100,0))
    desc_afp =  int(round(sueldo_bruto*12/100,0))
    liquido = sueldo_bruto - desc_salud - desc_afp
    lista_trabajador.append({
                    "nombres": nombres,
                    "cargo": cargo,
                    "sueldo_bruto": sueldo_bruto,
                    "desc_salud": desc_salud,
                    "desc_afp": desc_afp,
                    "liquido": liquido,
                })
    
    return 


def lis_trabajador():
     system("cls")
     longitud = len(lista_trabajador)
     print(f"Nombres\t        Cargo\t   Sueldo_Bruto\t Desc_salud\t Desc_afp\t Liquido\t")
     for contador  in  range(longitud):
         print(f"{lista_trabajador[contador]['nombres']}\t {lista_trabajador[contador]['cargo']}\t   {lista_trabajador[contador]['sueldo_bruto']}\t  {lista_trabajador[contador]['desc_salud']}\t   {lista_trabajador[contador]['desc_afp']}\t  {lista_trabajador[contador]['liquido']}\t\n" )
     input()
    
   

def imp_trabajador():
     with open(r"C:\Users\cetecom\Documents\salida.txt", "w", newline='') as archivo:
        archivo.write(f"Nombres\t        Cargo\t   Sueldo_Bruto\t Desc_salud\t Desc_afp\t Liquido\t\n")
        for lista  in  lista_trabajador:
          archivo.write(f"{lista['nombres']}\t {lista['cargo']}\t   {lista['sueldo_bruto']}\t  {lista['desc_salud']}\t   {lista['desc_afp']}\t  {lista['liquido']}\t\n" )
     


def salir():
    print('Saliendo')


menu_principal()