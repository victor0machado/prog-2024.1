def fatorial(n):
    fat = 1
    for i in range(1, n + 1):
        fat *= i

    return fat

def soma_fatoriais():
    while True:
        nums = [int(i) for i in input().split()]
        print(fatorial(nums[0]) + fatorial(nums[1]))

try:
    soma_fatoriais()
except EOFError:
    pass
