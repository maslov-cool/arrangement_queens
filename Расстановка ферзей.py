def queens(size):
    min_value = int(''.join(str(i) for i in range(1, size + 1)))
    solutions = []
    for i in [i for i in range(min_value, int(str(min_value)[::-1])) if len(set(str(i))) == size and
                                                                        all(1 <= int(j) <= size for j in str(i))]:
        boolean = True
        for j in range(size):
            for q, k in enumerate(range(j - 1, -1, -1), 1):
                if int(str(i)[j]) + q < size + 1:
                    if int(str(i)[k]) == int(str(i)[j]) + q:
                        boolean = False
                        break
                if int(str(i)[j]) - q > 0:
                    if int(str(i)[k]) == int(str(i)[j]) - q:
                        boolean = False
                        break
            if not boolean:
                break
            for q, k in enumerate(range(j + 1, size), 1):
                if int(str(i)[j]) + q < size + 1:
                    if int(str(i)[k]) == int(str(i)[j]) + q:
                        boolean = False
                        break
                if int(str(i)[j]) - q > 0:
                    if int(str(i)[k]) == int(str(i)[j]) - q:
                        boolean = False
                        break
            if not boolean:
                break
        if boolean:
            solutions.append(i)
    print(*sorted(solutions), sep='\n')



