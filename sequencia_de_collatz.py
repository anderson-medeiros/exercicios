def collatz(n):
    seq = []
    def inner_collatz(n):
        result = (3 * n + 1) if n % 2 else (n // 2)
        seq.append(result)
        if -2 < result < 2:
            return seq
        return inner_collatz(result)
    return inner_collatz(n)


def get_int(msg):
    try:
        return int(input(msg))
    except ValueError:
        print('\033[31mInsira um número inteiro\033[m')
        get_int(msg)

n = get_int('Número: ')
print(f'sequência collatz de {n}:\033[32m', end=' ')
print(*collatz(n), sep=' → ')

