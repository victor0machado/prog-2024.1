n = int(input())
input()
for i in range(n):
    if i > 0:
        print()

    madeiras = {}
    try:
        while True:
            madeira = input()
            if not madeira:
                break

            if madeira in madeiras:
                madeiras[madeira] += 1
            else:
                madeiras[madeira] = 1
    except EOFError:
        pass

    pop = sum([qtd for qtd in madeiras.values()])
    for madeira in sorted(list(madeiras.keys())):
        print(f"{madeira} {(100 * madeiras[madeira] / pop):.4f}")
