# Ejercicio 2.5: Definir una función
def saludar(nombre):
    print('¡ Hola,',nombre,'!')

name = input('¿cuál es tu nombre? ingresalo acá: ')
saludar(name)

# Ejercicio 2.7: Buscar precios
print()

def buscar_precio(fruta):
    f = open('Data/precios.csv', 'rt')
    mensaje = ''
    found = False
    for line in f: 
        row = line.split(',')
        if fruta in row:
            precio = round(float(row[1]),2)
            mensaje = (f'El precio del cajon de {fruta} es ${precio}')
            found = True

    if (not found):
        mensaje = (f'La fruta {fruta} no se encuentra en el listado.')
    f.close()    
    return mensaje

print(buscar_precio('Frambuesa'))



