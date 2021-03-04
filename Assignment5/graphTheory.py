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


def solution(color):
    for i in range(len(color)):
        color[i] += 1
    return color


def prt(color, chromaticNum):
    print("The Chromatic Number is:", chromaticNum, "and the colors are:", color)


def colorGraph(graph):
    colorResult = []
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            idx = graph[i].index(0)
            colorResult.append(idx)
            break

    col = legalColor(graph, colorResult)
    color = solution(col)
    chromaticNum = max(color)

    prt(color, chromaticNum)


def main():
    graph = [[0, 1, 1, 1],
             [1, 0, 1, 0],
             [1, 1, 0, 1],
             [1, 0, 1, 0]]
    """result should equal [1,2,3,2]"""
    # graph returns [1,2,3,2]

    graph2 = [[0, 1, 1, 0, 0],
              [1, 0, 1, 1, 0],
              [1, 1, 0, 1, 0],
              [0, 1, 1, 0, 1],
              [0, 0, 0, 1, 0]]
    """result should equal [1,2,3,1,2]"""
    # graph2 returns [[1,2,3,1,2]

    graph3 = [[0, 1, 1],
              [1, 0, 1],
              [1, 1, 0]]
    """result should equal [1,2,3]"""
    # graph3 return [1,2,3]

    graph4 = [[0, 1, 0, 0, 0],
              [1, 0, 1, 0, 0],
              [0, 1, 0, 1, 0],
              [0, 0, 1, 0, 1],
              [0, 0, 0, 1, 0]]
    """result should equal [1,2,1,2,1]"""
    # graph4 return [1,2,1,2,1]

    colorGraph(graph)
    colorGraph(graph2)
    colorGraph(graph3)
    colorGraph(graph4)


if __name__ == "__main__":
    main()
