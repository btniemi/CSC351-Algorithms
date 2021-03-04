graph = [[0, 1, 1, 1],
         [1, 0, 1, 0],
         [1, 1, 0, 1],
         [1, 0, 1, 0]]
color = [0, 1, 2, 1]

graph2 = [[0, 1, 1, 0, 0],
          [1, 0, 1, 1, 0],
          [1, 1, 0, 1, 0],
          [0, 1, 1, 0, 1],
          [0, 0, 0, 1, 0]]
color2 = [0, 1, 2, 0, 0]

graph3 = [[0, 1, 1],
          [1, 0, 1],
          [1, 1, 0]]
color3 = [0, 1, 2]


def legalColor(graph, color):
    for i in range(len(graph)):
        for j in range(i + 1, len(graph)):
            grp = graph[i][j]
            chk = color[j]
            val = color[i]
            if grp and chk == val:
                color[j] = val + 1
                return color
    return color

def Solution(color):
    for i in range(len(color)):
        color[i] += 1
    return color

print(Solution(color3))

