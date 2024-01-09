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
    p = Point(value)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~


    #your ALG here...


    color_num = int(random.random()*50)


    #~~~~~~~~~~~~~~~~~~~~

    p.col_num=color_num
    points.append(p)
    return color_num