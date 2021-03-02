"""with the help of https://www.geeksforgeeks.org/m-coloring-problem-backtracking-5/
Jerry Malcomson for explainging some loop structures and providing me what he wrote to walk through it in code
and Andy Niemantsverdriet for a nudge in the right direction for checking if valid colors"""

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


def colorGraph(graph):
    colorResult = []
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            idx = graph[i].index(0)
            colorResult.append(idx)
            break

    color = legalColor(graph, colorResult)

    return color


def main():
    graph = [[0, 1, 1, 1],
             [1, 0, 1, 0],
             [1, 1, 0, 1],
             [1, 0, 1, 0]]
    """result should equal [0,1,2,1]"""
    # graph returns [0,1,2,1]

    graph2 = [[0, 1, 1, 0, 0],
              [1, 0, 1, 1, 0],
              [1, 1, 0, 1, 0],
              [0, 1, 1, 0, 1],
              [0, 0, 0, 1, 0]]
    """result should equal [0,1,2,0,1]"""
    # graph2 returns [0,1,2,0,1]

    graph3 = [[0, 1, 1],
              [1, 0, 1],
              [1, 1, 0]]
    """result should equal [0,1,2]"""
    # graph3 return [0,1,2]

    graph4 = [[0, 1, 0, 0, 0],
              [1, 0, 1, 0, 0],
              [0, 1, 0, 1, 0],
              [0, 0, 1, 0, 1],
              [0, 0, 0, 1, 0]]
    """result should equal [0,1,0,1,0]"""
    # graph4 return [0,1,0,1,0]

    print(colorGraph(graph))
    print(colorGraph(graph2))
    print(colorGraph(graph3))
    print(colorGraph(graph4))


if __name__ == "__main__":
    main()
