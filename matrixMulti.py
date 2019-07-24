import vector


def multiplyMatrix(vectX, vectY):
    result = []
    for elm in vectX:
        result.append(innerloop(elm, vectY))
    return result


def scaleMatrix(vect, alpha):
    result = []
    for elm in vect:
        scalledElm = [x * alpha for x in elm]
        result.append(scalledElm)
    return result


def innerloop(vectA, vectB):
    result = []
    index = 0
    for elm in vectB:
        if (index >= len(vectB)-1):
            return result
        col = getCol(vectB, index)
        result.append(sum(doMulti(vectA, col)))
        index += 1
    return result


def doMulti(A, B):
    if not(len(A) == len(B)):
        raise Exception("Error! Vectors aren't in same size")
    result = []
    for x, y in zip(A, B):
        result.append(x * y)
    return result


def getCol(vect, colnum):
    return [y[colnum] for y in vect]


def getRow(vect, rownum):
    return vect[rownum]


def getAllCols(vect):
    result = []
    for index in range(getNumOfColumns(vect)):
        result.append(getCol(vect, index))
    return result


def getNumOfColumns(vect):
    if not(vector.isMatrix(vect)):
        raise Exception(">> Error! args is not matrix \n>> %s" % (vect))
    return len(vect[0])


vt = [[1, 2, 3], [4, 5, 6]]
vtB = [[7, 8], [9, 10], [11, 12]]
print(getAllCols(vtB))


##### extra for the blog ######
