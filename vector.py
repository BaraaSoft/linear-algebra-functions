
import math
import numpy as np


class Vector(object):
    pass


def copy(vectA, vectB):
    result = []
    if not(validate(vectA, vectB)):
        return
    if(isColumnVect(vectB)):
        if(isColumnVect(vectA)):
            for (elmA, elmB) in zip(vectA, vectB):
                elmB = elmA
                result.append(elmB)
            return result
        elif(isRowVect(vectA)):
            for (elmA, elmB) in zip(vectA[0], vectB):
                elmB = [elmA]
                result.append(elmB)
            return result
    else:
        if(isColumnVect(vectA)):
            for (elmA, elmB) in zip(vectA, vectB[0]):
                elmB = elmA[0]
                result.append(elmB)
            return [result]

        elif(isRowVect(vectA)):
            for (elmA, elmB) in zip(vectA[0], vectB[0]):
                elmB = elmA
                result.append(elmB)
            return [result]

# takes a matrix 'vect' and mutliply or its elements by a value 'alpha'


def scale(vect, alpha):
    result = []
    if not(isColumnVect(vect) or isRowVect(vect)):
        raise Exception('Error ! first argumnet must be a vector')
    if(isMatrix(vect)):
        for elm in vect:
            scalledElm = [x * alpha for x in elm]
            result.append(scalledElm)
        return result
    else:
        return [i * alpha for i in vect]


def axpy(a, vectX, vectY):
    result = []
    validate(vectX, vectY)
    vectXScl = scale(vectX, a)
    if(isColumnVect(vectY)):
        if(isColumnVect(vectXScl)):
            for elmX, elmY in zip(vectXScl, vectY):
                val = elmX[0] + elmY[0]
                result.append([val])
            return result
        elif(isRowVect(vectXScl)):
            for elmX, elmY in zip(vectXScl[0], vectY):
                val = elmX + elmY[0]
                result.append([val])
            return result
    else:
        if(isColumnVect(vectXScl)):
            for elmX, elmY in zip(vectXScl, vectY[0]):
                val = elmX[0] + elmY
                result.append(val)
            return [result]
        elif(isRowVect(vectXScl)):
            for elmX, elmY in zip(vectXScl[0], vectY[0]):
                val = elmX + elmY
                result.append(val)
            return [result]


def axpyAdvance(a, vectX, vectY):
    scallVect = scale(vectX, a)
    return doOperation(lambda elmX, elmY: elmX+elmY, scallVect, vectY)


def dot(vectX, vectY):
    arry = doOperation(lambda elmX, elmY: elmX * elmY, vectX, vectY)
    accum = 0
    if(isColumnVect(arry)):
        for x in arry:
            accum += x[0]
    else:
        for x in arry[0]:
            accum += x

    return accum


def doOperation(callback, vectX, vectY):
    result = []
    validate(vectX, vectY)
    if(isColumnVect(vectY)):
        if(isColumnVect(vectX)):
            for elmX, elmY in zip(vectX, vectY):
                val = callback(elmX[0], elmY[0])
                result.append([val])
            return result
        elif(isRowVect(vectX)):
            for elmX, elmY in zip(vectX[0], vectY):
                val = callback(elmX, elmY[0])
                result.append([val])
            return result
    else:
        if(isColumnVect(vectX)):
            for elmX, elmY in zip(vectX, vectY[0]):
                val = callback(elmX[0], elmY)
                result.append(val)
            return [result]
        elif(isRowVect(vectX)):
            for elmX, elmY in zip(vectX[0], vectY[0]):
                val = callback(elmX, elmY)
                result.append(val)
            return [result]


def norm(vect):
    accum = 0
    if not(isColumnVect(vect) or isRowVect(vect)):
        raise Exception("Error! param is not vector")
    if(isColumnVect(vect)):
        for elm in vect:
            accum += elm[0] * elm[0]
        return math.sqrt(accum)
    else:
        for elm in vect[0]:
            accum += elm * elm
        return math.sqrt(accum)


def validate(vectA, vectB):
    if not((isColumnVect(vectA) or isRowVect(vectA))):
        raise Exception(
            'first argumnet is not vector: {}'.format(vectA))
    if not((isColumnVect(vectB) or isRowVect(vectB))):
        raise Exception(
            'second argumnet is not vector: {}'.format(vectB))
    if (vectCalcSize(vectA) != vectCalcSize(vectB)):
        raise Exception(
            'vectors must have same size {}'.format(vectB))
    return True


def vectCalcSize(vect):
    col = len(vect)
    row = len(vect[0])
    print(f'>> {row} X {col}')
    return col * row


def size(vect):
    col = len(vect)
    row = len(vect[0])
    return(row, vect)


def isRowVect(vect):
    return len(vect) == 1


def isColumnVect(vect):
    return len(vect) > 1


def isMatrix(vect):
    try:
        # print('>> type of :: %s' % (type(vect[0])))
        # print('>> is a matrix %s' % (type(vect[0]) == 'list'))
        return type(vect[0]) is list
    except:
        return False


def oneOfVect(vect):
    zerovect = scale(vect, 0)
    result = []
    if(isMatrix(vect)):
        for elm in zerovect:
            res = [x + 1 for x in elm]
            result.append(res)
        return result
    else:
        return [x + 1 for x in zerovect]


def zeroOfVect(vect):
    return scale(vect, 0)


tst = [[7, 5, 5]]
tst1 = [[3], [3], [3]]
tst2 = [[1], [2], [0]]
tst4 = [[1, 3, 2]]

# print(">> tst: %s \n>> tst2: %s " % (tst, tst2))
# print(copy(tst2, tst))

# scalling :
# print('>> scalling:')
# print('>> tst: \n%s' % (scale(tst, 2)))
# print('>> tst2: \n%s' % (scale(tst2, 2)))

# axpy operation:
print('>> norm:')
print('me >> %s' % (dot([[.01, 45, 50]], [[1], [2], [6]])))
print('np >> %s' % (np.array([.01, 45, 50])).dot([1, 2, 6]))
# print('>> tst2: \n%s' % (axpy(tst2, 2)))

# To flat out list using python List Comprehensions:
# val = [i for x in tst2 for i in x]
# print(val)


# takes a matrix 'vect' and mutliply or its elements by a value 'alpha'
