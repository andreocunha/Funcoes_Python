#variavel local
def imprimeValores():
    num3 = 14
    print(f'O valor do num1 na função é {num1}')
    print(f'O valor do num2 na função é {num2}')
    print(f'O valor do num3 na função é {num3}')

#variavel global
num1 = 16
num2 = 7
imprimeValores()

print(f'O valor do num1 é {num1}')
print(f'O valor do num2 é {num2}')