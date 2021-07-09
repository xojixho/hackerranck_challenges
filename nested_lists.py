if __name__ == '__main__':
    datos = []
    for _ in range(int(input())):
        lista = []
        name = input()
        lista.append(name)
        score = float(input())
        lista.append(score)
        datos.append(lista)

datos = sorted(datos, key = lambda dato: dato[1])
peor_puntage = datos[0][1]
indice = 0
for j in range(1, len(datos)):
    if datos[j][1] == peor_puntage:
        continue
    else:
        indice = j
        break

segundo_peor = datos[indice][1]

segundos_peores = []
for i in range(indice, len(datos)):
    if datos[i][1] == segundo_peor:
        segundos_peores.append(datos[i][0])

segundos_peores.sort()

for item in segundos_peores:
    print(item)