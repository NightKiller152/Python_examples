import mytests

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    dist = dsquared**0.5
    return dist


mytests.testEqual(distance(1, 2,  1, 2), 0)
mytests.testEqual(distance(1,2, 4,6), 5)