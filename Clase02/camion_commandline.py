import csv
import sys

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
if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)