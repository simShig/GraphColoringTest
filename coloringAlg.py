import random

from Point import Point

maxCol = 0
points = []
def coloringAlg (value):
    '''
    students' algorithm for "online coloring"
    :param value: numeric value of the point (x-coordinate)
    :return: color_num
    '''
    global maxCol
    p = Point(value)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~


    #your ALG here...

    color_num = maxCol


    #~~~~~~~~~~~~~~~~~~~~

    p.col_num=color_num
    points.append(p)
    return color_num