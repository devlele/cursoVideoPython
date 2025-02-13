while True:
    num = int(input('Digite um número: '))
    if num < 0:
        break
    for i in range(0, 11):
        print('{} x {} = {}'.format(num, i, num*i))