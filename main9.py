for x in range(1, 8):
    for y in range(1, 8):
        for z in range(1, 8):
            if x != y and y != z and x != z:
                print(x, end='')
                print(y, end='')
                print(z)
