while True:
    try:
        cont = 0
        expr = input()
        for char in expr:
            if char not in ["(", ")"]:
                continue
            if char == "(":
                cont += 1
            else:
                cont -= 1
                if cont < 0:
                    break

        if cont == 0:
            print("correct")
        else:
            print("incorrect")
    except EOFError:
        break
