# ============ Ejercicio 2.11: Tuplas ==============
import csv
f = open('Data/camion.csv')
filas = csv.reader(f)
next(filas)

fila = next(filas)
t = (fila[0], int(fila[1]), float(fila[2]))
cost = t[1] * t[2]
print(cost)

print()

nombre, cajones, precio = t
print('nombre: ', nombre, "\n",'cajones: ', cajones, "\n",'Precio: ', precio)

# Tomá las variables de arriba y empaquetalas en una tupla.
tupla = (nombre, 2*cajones, precio)
print()
print(tupla)

# ========== Ejercicio 2.12: Diccionarios como estructuras de datos ============
diccionario = {
        'nombre' : fila[0],
        'cajones' : int(fila[1]),
        'precio'  : float(fila[2])
    }

costo = diccionario['cajones'] * diccionario['precio']

print('costo usando diccionario: ',costo)

# ===== Compará este ejemplo con el mismo cálculo hecho con tuplas más arriba. Cambiá el número de cajones a 75
diccionario['cajones'] = 75
cajon = diccionario.get('cajones')
print('cajones: ', diccionario['cajones'])
print('usando .get(): ', cajon)

# ====== Agregá algunos atributos: =========
diccionario['fecha'] = 'una fecha'
diccionario['cuenta'] = 12345

print(diccionario)

# ==== Si usás el comando for para iterar sobre el diccionario, obtenés las claves: =====
for k in diccionario: 
    print(' clave: ',k,'\n','contenido: ',diccionario[k])
    print()

# Método ítems
print('usando ítems')
for k,v in diccionario.items():
    print(k,'=',v)