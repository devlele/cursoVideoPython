num = int(input('Digite um número inteiro: '))
fatorial = num
while num != 0:
    fatorial = num
    for i in range(num, 1, -1):
        fatorial *= (i-1)
    
    print(fatorial)
    num = int(input('Digite outro número: '))