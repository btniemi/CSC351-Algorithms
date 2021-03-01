graph = [[0, 1, 1, 1],
         [1, 0, 1, 0],
         [1, 1, 0, 1],
         [1, 0, 1, 0]]

graph2 = [[1, 2], [2, 3], [3, 1]]


def graphColor(g):
    colored = []
    for i in range(0, len(g)):
        ncolored = []
        for u in range(0, len(g[i])):
            value = g[i][u]
            if (len(colored) < value):
                continue
            ncolored.append(colored[value])
        temp = 0
        nchanged = False
        while (not nchanged):
            nchanged = True
            for n in ncolored:
                if (temp == n):
                    temp += 1
                    nchanged = False
        colored.append(temp)
    return colored


print(graphColor(graph2))
