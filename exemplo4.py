def dobraLista(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


lista = [2, 3, 1, 8]
dobraLista(lista)
print(lista)