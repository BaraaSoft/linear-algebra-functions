import vector
import matrixMulti


##### PART F #####
def identityMatrix(vect):
    result = []
    columnsArray = transpose(vect)
    for index, columnVect in enumerate(columnsArray):
        subArray = columnSlicing(columnVect, index)
        result.append(subArray)
    # rotating back to original matrix dimensions
    identityMtrx = transpose(result)
    return identityMtrx

##### PART D #####


def columnSlicing(vect, index):
    if(index >= len(vect)):
        raise Exception("\n >> Error! Invalid index")
    vectSubA = vect[:index]
    vectSubB = vect[index:]
    vectA = []
    # if vectSubA is empty(that's true in the first iteration)
    # then no need todo any operation on it
    if(len(vectSubA) > 0):
        vectA = setAllElmToZero(vectSubA)
    vectB = setElmOneElseZero(vectSubB)
    return vectA+vectB


##### PART C #####

# check of argument is matrix or an array
# if its an array simply set the first element to One
# if its matrix set the first element of the first nested array to One
def setElmOneElseZero(vect):
    zeroMatrix = setAllElmToZero(vect)
    if not(isMatrix(vect)):
        zeroMatrix[0] = 1
        return zeroMatrix
    zeroMatrix[0][0] = 1
    return zeroMatrix

# set each element of given array 'vect' to zero


def setAllElmToZero(vect):
    zeroMatrix = scale(vect, 0)
    return zeroMatrix


##### PART B #####
# check if a given value is matrix or an array


def isMatrix(vect):
    try:
        return type(vect[0]) is list
    except:
        return False


def scale(vect, alpha):
    result = []
    if(isMatrix(vect)):
        for elm in vect:
            scalledElm = [x * alpha for x in elm]
            result.append(scalledElm)
        return result
    else:
        return [i * alpha for i in vect]


vt = [[7, 8, 1], [9, 10, 2], [11, 12, 1]]

##### PART A #####
# loop though a matrix only return  a single column given by its index


def getColumn(matrix, col):
    return [y[col] for y in matrix]

# loop through an array returning all its columns array


def transpose(matrix):
    result = []
    numberOfCol = len(matrix)
    for index in range(numberOfCol):
        result.append(getColumn(matrix, index))
    return result


print(identityMatrix(vt))


##### extra for the blog ######
