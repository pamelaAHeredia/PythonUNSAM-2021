import csv

# def leer_camion(nombre_archivo): 
#     camion = []
#     with open(nombre_archivo, 'rt') as f:
#         rows = csv.reader(f)
#         next(rows)
#         for row in rows:
#             try: 
#                 lote = (row[0], int(row[1]), float(row[2]))
#                 camion.append(lote)
#             except ValueError: 
#                 print('faltan datos en el archivo')    
#     return camion

# print(leer_camion('Data/camion.csv'))
# truck = leer_camion('Data/camion.csv')
# print('Pos 1: ',truck[1])
# print()

# total = 0
# for i in truck:
#     total += i[1] * i[2]
# print(total)

# print()

# Puedo acceder a los elementos usando las claves: 

# total = 0
# for nombre, cajones, precio in truck: 
#     total += cajones * precio

# print('reescrito: ', total)

# ============================= Ejercicio 2.16: Lista de diccionarios =============================

def leer_camion(nombre_archivo): 
    lista = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            try: 
                camion = {} 
                camion['nombre'] = row[0]
                camion['cajones']= int(row[1])
                camion['precio'] = float(row[2])
                lista.append(camion)
            except ValueError: 
                print('faltan datos en el archivo')                               
    return lista

cam = leer_camion('Data/camion.csv')
from pprint import pprint
# pprint(cam)

total_camion = 0
for i in cam: 
    total_camion += i.get('cajones') * i.get('precio')

# ============================= Ejercicio 2.17: Diccionarios como contenedores =============================

def leer_precios(nombre_archivo):
    d = {}
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        for row in rows: 
            try: 
                d[row[0]] = float(row[1])
            except IndexError: 
                print()   
    return d            

precios = leer_precios('Data/precios.csv')
# pprint (precios)

# =============================  Ejercicio 2.18: Balances =============================

total_venta = 0
for i in cam: 
    total_venta += precios.get(i.get('nombre')) * i.get('cajones') 

print('============================= B A L A N C E =============================')
print()
print('* Venta al público. Monto total: $', round(total_venta,2))
print('* Compra por mayor. Monto total: $', round(total_camion,2))

diferencia = round((total_venta - total_camion),2)
if (diferencia < 0): 
    print(f'* Monto total de la pérdida: $ {diferencia}')
else:
    print(f'* Ganancia total: $ {diferencia}')    
