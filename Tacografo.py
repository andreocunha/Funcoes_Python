def calculaDistancia(tempo, velo):
    result = tempo*velo
    return result


qtd = int(input())
soma = 0

while qtd > 0:
    valores = input()
    valores = valores.split(' ')
    tempo = int(valores[0])
    velo = int(valores[1])
    soma += calculaDistancia(tempo, velo)
    qtd -= 1

print(soma)
