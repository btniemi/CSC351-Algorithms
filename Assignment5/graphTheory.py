def colorGraph(graph):
    result = []
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            idx = graph[i].index(0)
            result.append(idx)
            break

    return result


def main():
    graph = [[0, 1, 1, 1],
             [1, 0, 1, 0],
             [1, 1, 0, 1],
             [1, 0, 1, 0]]
    """result should equal [0,1,2,0]"""

    graph2 = [[0, 1, 1, 0, 0],
              [1, 0, 1, 1, 0],
              [1, 1, 0, 1, 0],
              [0, 1, 1, 0, 1],
              [0, 0, 0, 1, 0]]
    """result should equal [0,1,2,0,1]"""

    print(colorGraph(graph))
    print(colorGraph(graph2))


if __name__ == "__main__":
    main()
