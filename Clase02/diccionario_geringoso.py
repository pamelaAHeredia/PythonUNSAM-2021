# ======= Ejercicio 2.14: Diccionario geringoso ========

#función que, a partir de una lista de palabras, devuelva un diccionario geringoso.

def convertir(palabras):
    d = {}
    for n in palabras:
        c = ''
        for i in n: 
            if i.lower() not in 'aeiou':
                c += i
            else:
                c += i+'p'+i 
        d[n] = c
    return d    

lista = ['banana', 'manzana', 'mandarina']

print(convertir(lista))

