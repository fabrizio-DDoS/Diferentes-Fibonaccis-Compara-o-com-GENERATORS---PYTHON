import time

fuser = int(input('Digite o F da sequencia:'))

def cronometro(base):
    def segundos():
        start = time.time()
        base()
        stop = time.time()
        print(f'Tempo total: {stop - start}')
    return(segundos)


@cronometro
def executor():
    def fibonacci_rapido(fuser):
        a = 0 #penultimo
        b = 1 #ultimo
        for i in range(fuser):
            yield a #para os numeros 1 por 1
            temp = a
            a = b
            b = temp + b
    for x in fibonacci_rapido(fuser):
        print(x)

@cronometro
def fibonacci_demorado():
    nada = 1
    seque = 1
    listaf = [0]
    while nada < fuser:
        listaf.append(seque)
        item = listaf[nada]
        pre = listaf[nada - 1]
        seque = (item + pre)
        nada += 1
        print(seque)