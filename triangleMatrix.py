import vector
import matrixMulti


def setToDiagonalMatrix(matrix, colVect):
    result = []
    vectSubA = matrixMulti.getAllCols(matrix)
    for index, columnVect in enumerate(vectSubA):
        vectSubB = setColumnToDiagnolValue(columnVect, colVect, index)
        result.append(vectSubB)
    # rotating back to original vector dimensions
    vectSub = matrixMulti.getAllCols(result)
    return vectSub


def setColumnToDiagnolValue(vect, alphaVect, index):
    if(index >= len(vect)):
        raise Exception(
            "\n >> Error! Invalid index \n >> vectorLength:%s \n >> index:%s " % (len(vect), index))
    vectSubA = vect[:index]
    vectSubB = vect[index:]
    vectA = []
    vectB = []
    if(len(vectSubA) > 0):
        vectA = vector.zeroOfVect(vectSubA)
    if(index < len(alphaVect)):
        vectB = firstElmValueElseZero(vectSubB, alphaVect, index)
    return vectA+vectB


def firstElmValueElseZero(vect, alphaVect, index):
    if(index > len(alphaVect)):
        raise Exception("Index Error! cannot set fist element value")
    zerosVect = vector.zeroOfVect(vect)
    if not(vector.isMatrix(vect)):
        zerosVect[0] = alphaVect[index]
        return zerosVect
    zerosVect[0][0] = alphaVect[index]
    return zerosVect


vt = [[7, 8, 1], [9, 10, 2], [11, 12, 1]]
vtb = [9, 99, 999]

print(setToDiagonalMatrix(vt, vtb))

##### extra for the blog ######
