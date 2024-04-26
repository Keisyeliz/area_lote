import os

list_urbano = []
list_comercial = []
list_campestre = []
sw = True
def fnt_limpiar():
    os.system('cls')
    print('Autor: Keisy Murillo')

def fnt_selector(op):
    if op == '1':
        fnt_limpiar()
        tipo_lote = input('---TIPO DE LOTE---\n1. Urbano\n2. Comercial\n3. Campestre\n->')
        fnt_limpiar()
        if tipo_lote == '1':
            propietario = input('Ingrese el nombre del propietario: ')
            frente = float(input('Ingrese la medida del frente del lote: '))
            fondo = float(input('Ingrese la medida del fondo del lote: '))
            area = frente * fondo
            mt2 = 25000 * area
            permiso_const = 0.45 * mt2
            total = mt2 + permiso_const
            lote = f"Nombre del propietario: {propietario} Area: $ {area} Valor del area: $ {mt2} Permiso de construcción: $ {permiso_const} Valor total: $ {total}"
            list_urbano.append(lote)
            print('Registro exitoso\n')
            enter = input('Presione <Enter> para continuar...')

        elif tipo_lote == '2':
            propietario = input('Ingrese el nombre del propietario: ')
            frente = float(input('Ingrese la medida del frente del lote: '))
            fondo = float(input('Ingrese la medida del fondo del lote: '))
            area = frente * fondo
            mt2 = 60000 * area
            permiso_const = 0.75 * mt2
            total = mt2 + permiso_const
            lote = f"Nombre del propietario: {propietario} Area: $ {area} Valor del area: $ {mt2} Permiso de construcción: $ {permiso_const} Valor total: $ {total}"
            list_comercial.append(lote)
            print('Registro exitoso\n')
            enter = input('Presione <Enter> para continuar...')

        elif tipo_lote == '3':
            propietario = input('Ingrese el nombre del propietario: ')
            frente = float(input('Ingrese la medida del frente del lote: '))
            fondo = float(input('Ingrese la medida del fondo del lote: '))
            area = frente * fondo
            mt2 = 35000 * area
            permiso_const = 0.15 * mt2
            total = mt2 + permiso_const
            lote = f"Nombre del propietario: {propietario} Area: $ {area} Valor del area: $ {mt2} Permiso de construcción: $ {permiso_const} Valor total: $ {total}"
            list_campestre.append(lote)
            print('Registro exitoso\n')
            enter = input('Presione <Enter> para continuar...')

    if op == '2':
        tipo_lote = input('---TIPO DE LOTE---\n1. Urbano\n2. Comercial\n3. Campestre\n->')

        if tipo_lote == '1':
            print('---LISTA DE LOTES URBANOS---\n' )
            if len(list_urbano) == 0:
                print('No hay lotes registrados\n')
                enter = input('Presione <Enter> para continuar...')
            else:
                for lote in list_urbano:
                    print(lote)

        elif tipo_lote == '2':
            print('---LISTA DE LOTES COMERCIALES---\n' )
            if len(list_comercial) == 0:
                print('No hay lotes registrados\n')
                enter = input('Presione <Enter> para continuar...')
            else:
                for lote in list_comercial:
                    print(lote)

        elif tipo_lote == '3':
                    print('---LISTA DE LOTES CAMPESTRES---\n' )
                    if len(list_campestre) == 0:
                        print('No hay lotes registrados\n')
                        enter = input('Presione <Enter> para continuar...')
                    else:
                        for lote in list_campestre:
                            print(lote)

    if op == '3':
        sw = False


while sw == True:
    opcion = input('---MENÚ---\n1. Agregar\n2. Mostrar\n3. Salir\n->')
    fnt_selector(opcion)
    
