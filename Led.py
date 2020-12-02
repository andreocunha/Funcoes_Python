def qtdIndividualLedPorNumero(num):
    if num == 1:
        return 2
    elif num == 2:
        return 5
    elif num == 3:
        return 5
    elif num == 4:
        return 4
    elif num == 5:
        return 5
    elif num == 6:
        return 6
    elif num == 7:
        return 3
    elif num == 8:
        return 7
    elif num == 9:
        return 6
    elif num == 0:
        return 6

def qtdTotalLed(num):
    qtd = 0
    pos = 0
    while pos < len(num):
        qtd += qtdIndividualLedPorNumero(int(num[pos]))
        pos += 1
        
    return qtd


qtdNum = int(input())

for i in range(qtdNum):
    numDisplya = input()
    numLeds = qtdTotalLed(numDisplya)
    print(f'{numLeds} leds')


