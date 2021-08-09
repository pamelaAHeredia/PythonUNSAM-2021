numero_valido=False
while not numero_valido:
    try:
        a = input('Ingresá un número entero: ')
        n = int(a)
        numero_valido = True
    except ValueError:
        print('No es válido. Intentá de nuevo.')
print(f'Ingresaste {n}.')


# Ejercicio 2.8: Administración de errores

# for nombre in ['Pedro','Juan','Caballero']:
#     try:
#         edad = preguntar_edad(nombre)
#         print(f'{nombre} tiene {edad} años.')
#     except ValueError:
#         print(f'{nombre} no ingresó una edad válida.')