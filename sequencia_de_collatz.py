def collatz(n):
    if n % 2:
        return 3 * n + 1
    return n // 2

def get_number():
    try:
        return int(input('Insira um número: '))
    except ValueError:
        get_number()



number = get_number()
result = 0
while result != 1:
    result = collatz(number)
    print(result, end=' ')
    # print(result := collatz(number), end=' ')
    number = result
