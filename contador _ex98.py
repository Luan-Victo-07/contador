
from time import sleep
def contador(i, f, p):
    print('-=' * 20)
    print(f'contagem de {i} até {f} de {p} em {p}')
    print('-=' * 20)
    c = i
    if c <= f:
        while c <= f:
            print(f'{c}', end=' ')
            c += p
            sleep(0.5)
        print('FIM!')

    else:
        c = i
        while c >= f:
            print(f'{c}', end=' ')
            c -= p
            sleep(0.5)
        print('FIM!')
#principal
contador(0, 100, 10)  
contador(100, 0, 20)
sleep(1)
print('Agora é sua vez de personalizar a contagem! ')
i = int(input('Digite o valor inicial: '))
f = int(input('Digite o valor final: '))
p = int(input('Digite o passo da contagem: '))
sleep(0.5)
s = sleep(0.5)
print(f'{contador(i, f, p)} ')

