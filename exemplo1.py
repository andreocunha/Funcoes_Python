# primeira forma:
print('------------------------------')
print('Andre')
print('------------------------------')

print('------------------------------')
print(' Laranja')
print('------------------------------')

print('------------------------------')
print('Henrique')
print('------------------------------')

print('------------------------------')
print('Bruno')
print('------------------------------')

#------------------------------------------------------------------------------------------------------------------------

# segunda forma:
def linha():
    print('-'*30)

linha()
print('Andre')
linha()

linha()
print('Emerson')
linha()

linha()
print('Henrique')
linha()

#------------------------------------------------------------------------------------------------------------------------

#  terceira forma:
def cabeçalho(nome):
    print('-'*30)
    print(nome)
    print('-'*30)

cabeçalho('Andre')
cabeçalho('Emerson')
cabeçalho('Henrique')