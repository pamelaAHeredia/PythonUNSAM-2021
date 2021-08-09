with open('Data/camion.csv', 'rt') as f:
        # representación cruda de la cadena, incluyendo comillas y códigos de escape
        data = f.read()

# salida formateada de la cadena
print(data)
# print()
# print('next()')
# f = open('Data/camion.csv', 'rt')
# headers = next(f)

# for line in f:
#         print(line, end = '')

# f.close()

print()
print('split()')
f = open('Data/camion.csv', 'rt')
headers = next(f).split(',')
headers

for line in f:
        row = line.split(',')
        print(row)

f.close()