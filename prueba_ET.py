import random
trabajadores = ['Juan Pérez','María García','Carlos López','Ana Martínez','Pedro Rodríguez','Laura Hernández','Miguel Sánchez','Isabel Gómez','Francisco Díaz','Elena Fernández']
lista_P=[]
def asignar_sueldos_aleatorios():
    lista=[]
    for i in range(0,len(trabajadores)):
        sueldo=random.randint(300000,2500000)
        lista.append([trabajadores[i],sueldo])
        lista_P.append([trabajadores[i],sueldo])
    return lista







def Salir_del_programa():
    print('Finalizando el programa...')
    print('Hecho por Luis Ignacio Villalobos Baez')
    print('Rut: 22.111.531-7')
    return

print('Analizador de datos enterprise')
while True:
    print('Escoja la opcion que desea')
    print('1. Asignar sueldos aleatorios')
    print('2. Clasificar sueldos')
    print('3. Ver estadísticas.')
    print('4. Reporte de sueldos')
    print('5. Salir del programa')
    while True:
        try:
            opc_MP=int(input('=>'))
        except ValueError:
            print('Solo se aceptan valores numericos')
        else:
            break
    
    match opc_MP:
        case 1:
            asignar_sueldos_aleatorios()
            lista_P=sorted(lista_P)
            for i in range(0,len(lista_P)):
                print(f'{i+1}.{lista_P[i]}')
            
        case 2:
            pass
        
        case 3:
            pass
        
        case 4:
            pass
        
        case 5:
            Salir_del_programa()
            break
        
        case default:
            print('Solo se aceptan valores de 1 al 5')