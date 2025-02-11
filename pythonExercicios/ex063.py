num = int(input('Digite um número: '))
cont = 0
fibo = 0
antFibo = 1
while cont != num:
    fibo += antFibo
    antFibo = fibo 
    print(fibo)
    cont += 1

