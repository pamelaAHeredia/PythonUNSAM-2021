# =========== Ejercicio 2.2: Lectura de un archivo de datos =============

# costo_total = 0
# f = open('Data/camion.csv', 'rt')
# next(f)

# for line in f: 
#     row = line.split(',')
#     costo_total += int(row[1]) * float(row[2])

# print('Costo total: $',costo_total)
# f.close()

# ============= Ejercicio 2.3: Precio de la naranja ===============

# print()
# f = open('Data/precios.csv','rt')

# for line in f: 
#     row = line.split(',')
#     if 'Naranja' in row:
#         print('Precio de la naranja: $',row[1])
# f.close()   

# ============= Ejercicio 2.4: Archivos comprimidos ================

# import gzip
# with gzip.open('Data/camion.csv.gz', 'rt') as f:
#         for line in f:
#             print(line, end = '')

# ========== Ejercicio 2.6: Transformar un script en una función =========

# def costo_camion(nombre_archivo):
#     costo_total = 0
#     f = open(nombre_archivo, 'rt')
#     next(f)

#     for line in f: 
#         row = line.split(',')
#         costo_total += int(row[1]) * float(row[2])
#     f.close()   
#     return float(costo_total)
# print()
# print('Costo total del camión: ', round(costo_camion('Data/camion.csv'),2))   

# ========== Ejercicio 2.8: Administración de errores =====================
# Modificá el programa costo_camion.py para que atrape la excepción con un bloque try - except, 
# imprima un mensaje de aviso (warning) y continúe procesando el resto del archivo.

# def costo_camion(nombre_archivo):
#     costo_total = 0
#     f = open(nombre_archivo, 'rt')
#     next(f)

#     for line in f: 
#         try:
#             row = line.split(',')
#             costo_total += int(row[1]) * float(row[2])
#         except ValueError:
#             print('Faltan datos en el archivo')   
    
#     f.close()   
#     return float(costo_total)

# print()
# print(round(costo_camion('Data/camion.csv'),2))    

# Ejercicio 2.9: Funciones de la biblioteca
# print()
# import csv
# f = open('Data/camion.csv')
# rows = csv.reader(f)
# headers = next(rows)
# print('Headers: ',headers)

# for row in rows:
#         print(row)

# f.close()

# Modificá tu programa costo_camion.py para que use el módulo csv para leer los archivos
import csv
def costo_camion(nombre_archivo):    
    f = open(nombre_archivo)  
    rows = csv.reader(f)  
    costo_total = 0
    next(f)

    for line in rows: 
        try:
            costo_total += int(line[1]) * float(line[2])
        except ValueError:
            print('Faltan datos en el archivo')   
    
    f.close()   
    return round(float(costo_total),2)

print('Costo de la carga del camión: $', costo_camion('Data/camion.csv'))