
lotev = [['[ ]','[ ]','[ ]','[ ]'],
        ['[ ]','[ ]','[ ]','[ ]'],
        ['[ ]','[ ]','[ ]','[ ]'],
        ['[ ]','[ ]','[ ]','[ ]']]

def most_lote(lotev):
    print('---------------')
    for i in lotev:
        print('-'.join(i))
        print('---------------')

def v_lote(lotev,i,j,lot_vend):
    lotev[i][j] = lot_vend

def select_lotes():
    lotev = [['[ ]','[ ]','[ ]','[ ]'],
             ['[ ]','[ ]','[ ]','[ ]'],
             ['[ ]','[ ]','[ ]','[ ]'],
             ['[ ]','[ ]','[ ]','[ ]']]
    comprado = '[x]'
    key = 0
    while key == 0:
        most_lote(lotev)

        i = int(input('Ingrese el número de fila (0-3): '))
        j = int(input('Ingrese el número de columna (0-3): '))

        if lotev[i][j] != '[ ]':
            print('Lote YA Vendido - Seleccione otro')
            key = 0
        
        lote = v_lote(lotev, i, j, comprado)
        key = 1
    return lote

def registr_lote(lote):
    rut = input("Ingrese su rut: ")
    nomb = input("Ingrese su Nombre Completo: ")
    tel = int(input("Ingrese su telefono: "))
    email = input("Ingrese su Email: ")
    detlot=[rut,nomb,tel,email]
    return detlot


def menu():
    slcmenu = int(input('''
    1.- Disponibilidad de Lotes
    2.- Seleccionar un Lote
    3.- Detalles de Lotes Seleccionado
    4.- Ver Clientes
    5.- Salir
    -> '''))
    return slcmenu

def str_prog():
    a=0
    while a == 0:
        slcmenu = menu()
        if slcmenu == 1:
            print(lotev)
        elif slcmenu == 2:
            a = select_lotes()
            registr_lote(a)
        elif slcmenu == 3:
            print
        elif slcmenu == 4:
            print
        else:
            print

str_prog()

#profe lo siento no me hice el tiempo de verdad intente hacerlo
#pero el dia miercoles me sentia muy mal
#aun asi esto es lo que pude lograr
#disculpe mis palabras sin sentido 