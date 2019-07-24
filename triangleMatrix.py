import vector
import matrixMulti


def setToUpperTriMatrix(matrix):
    result = []
    vectSubA = matrixMulti.getAllCols(matrix)
    for index, columnVect in enumerate(vectSubA):
        vectSubB = setColumnValue(columnVect, index)
        result.append(vectSubB)
    # rotating back to original vector dimensions
    vectSub = matrixMulti.getAllCols(result)
    return vectSub


def setColumnValue(vect, index):
    if(index >= len(vect)):
        raise Exception(
            "\n >> Error! Invalid index \n >> vectorLength:%s \n >> index:%s " % (len(vect), index))
    vectSubA = vect[:index]
    vectSubB = vect[index:]
    vectA = []
    vectB = []
    # Becuase at first iteration vectSubA will be empty array
    if(len(vectSubA) > 0):
        vectA = vectSubA
    vectB = firstRemainElseZero(vectSubB)
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


def firstRemainElseZero(vect):
    a1 = vect[0]
    resultvect = vector.zeroOfVect(vect)
    resultvect[0] = a1
    return resultvect

#####################################################
########### strictly upper triangular matrix ########
#####################################################


def setToStrictlyUpperTriMatrix(matrix):
    result = []
    vectSubA = matrixMulti.getAllCols(matrix)
    for index, columnVect in enumerate(vectSubA):
        vectSubB = setSutmColumnValue(columnVect, index)
        result.append(vectSubB)
    # rotating back to original vector dimensions
    vectSub = matrixMulti.getAllCols(result)
    return vectSub


def setSutmColumnValue(vect, index):
    if(index >= len(vect)):
        raise Exception(
            "\n >> Error! Invalid index \n >> vectorLength:%s \n >> index:%s " % (len(vect), index))
    vectSubA = vect[:index]
    vectSubB = vect[index:]
    vectA = []
    vectB = []
    # Becuase at first iteration vectSubA will be empty array
    if(len(vectSubA) > 0):
        vectA = vectSubA
    vectB = vector.zeroOfVect(vectSubB)
    return vectA+vectB

#####################################################
############ unit upper triangular matrix ###########
#####################################################


def setToUnitUpperTriMatrix(matrix):
    result = []
    vectSubA = matrixMulti.getAllCols(matrix)
    for index, columnVect in enumerate(vectSubA):
        vectSubB = setColumnUUTMValue(columnVect, index)
        result.append(vectSubB)
    # rotating back to original vector dimensions
    vectSub = matrixMulti.getAllCols(result)
    return vectSub


def setColumnUUTMValue(vect, index):
    if(index >= len(vect)):
        raise Exception(
            "\n >> Error! Invalid index \n >> vectorLength:%s \n >> index:%s " % (len(vect), index))
    vectSubA = vect[:index]
    vectSubB = vect[index:]
    vectA = []
    vectB = []
    # Becuase at first iteration vectSubA will be empty array
    if(len(vectSubA) > 0):
        vectA = vectSubA
    vectB = firstOneElseZero(vectSubB)
    return vectA+vectB


def firstOneElseZero(vect):
    resultvect = vector.zeroOfVect(vect)
    resultvect[0] = 1
    return resultvect

#####################################################
########### strictly lower triangular part ##########
#####################################################


vt = [[8, 9, 4], [3, 7, 2], [4, 5, 3]]
#vtb = [9, 99, 999]

print(setToUnitUpperTriMatrix(vt))

# 8 9 4
# 3 7 2
# 4 5 3
##### Visualization UT Matrix ######
# 8 9 4
# 0 7 2
# 0 0 3
##### Visualization SUT Matrix ######
# 0 9 4
# 0 0 2
# 0 0 0

##### Visualization UUT Matrix ######
# 1 9 4
# 0 1 2
# 0 0 1

##### Visualization SLT Matrix ######
# 0 0 0
# 3 0 0
# 4 5 0

# 0 0 0 0
# 4 0 0 0
# 2 2 0 0
# 6 7 9 0

# 0 0 0 0 0
# 4 0 0 0 0
# 2 2 0 0 0
# 6 7 9 0 0
# 6 7 9 4 0
