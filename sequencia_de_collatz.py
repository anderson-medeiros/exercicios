def collatz(n, seq=[]):
    r = (3 * n + 1) if n % 2 else (n // 2)
    if -2 < r < 2:
        return seq + [r]
    return collatz(r, seq + [r])


def get_int(msg):
    try:
        return int(input(msg))
    except ValueError:
        print('\033[31mInsira um número inteiro\033[m')
        get_int(msg)

n = get_int('Número: ')
print(f'sequência collatz de {n}:\033[32m', end=' ')
print(*collatz(n), sep=' → ')

