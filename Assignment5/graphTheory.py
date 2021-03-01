def colorGraph(graph):
    result = []
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            idx = graph[i].index(0)
            result.append(idx)
            break

    """i need to add a check here but not sure"""

    return result


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
    # graph2 returns [0,1,2,0,0]

    graph3 = [[0, 1, 1],
              [1, 0, 1],
              [1, 1, 0]]
    """result should be [0,0,1] how is this possible"""
    #graph3 return [0,1,2]

    print(colorGraph(graph))
    print(colorGraph(graph2))
    print(colorGraph(graph3))


if __name__ == "__main__":
    main()
