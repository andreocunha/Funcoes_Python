def qtdQuadrados(num):
    soma = 0
    for i in range(0, num+1):
        soma += i*i
    print(soma)


num = int(input())
while num != 0:
    qtdQuadrados(num)
    num = int(input())
