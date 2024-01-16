import random

from Point import Point

maxCol = 0
points = []


def findNeighbours(value):
    '''
    find the place of the value among the excisting points
    :param value:
    :return: pLeft,pRight (neigbours)
    '''
    sorted_points = sorted(points, key=lambda point: point.value)
    pLeft = None
    pRight = None
    for p in sorted_points:
        if value > p.value:
            pLeft = p
            continue
        else:
            pRight = p
            break
    return pLeft, pRight

def safe_min(a, b):
    if a is None and b is None:
        return maxCol
    if a is None:
        return b
    if b is None:
        return a
    return min(a, b)

def chooseCol(pLeft, pRight):
    global maxCol
    cLeft = None
    cRight = None
    if pLeft:
        cLeft = pLeft.col_num
    if pRight:
        cRight = pRight.col_num
    cMin = safe_min(cRight, cLeft)
    if not cMin and cMin!=0:  # ifNone
        color = maxCol
    elif cMin == 0:
        maxCol += 1
        color = maxCol  # new color
    else:
        color = cMin - 1
    return color


def coloringAlg(value):
    '''
    students' algorithm for "online coloring"
    :param value: numeric value of the point (x-coordinate)
    :return: color_num
    '''
    global maxCol
    p = Point(value)

    # examples:
    '''random coloring'''
    color_num = int(random.random() * 50)
    #
    # '''naive coloring'''
    # color_num = maxCol
    # maxCol += 1

    # '''some-how logical coloring'''
    # pL, pR = findNeighbours(value)
    # color_num=chooseCol(pL,pR)
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~

    # your ALG here...

    # color_num = maxCol

    # ~~~~~~~~~~~~~~~~~~~~

    p.col_num = color_num
    points.append(p)
    print(f"max col is:{maxCol}")
    return color_num
