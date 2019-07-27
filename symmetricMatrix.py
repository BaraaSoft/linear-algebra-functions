import vector
import matrixMulti


def setSymmetricFromLowerTri(orgMatrix):
    colMatrix = matrixMulti.getAllCols(orgMatrix)
    resultMatrix = []

    for index, colVect in enumerate(colMatrix):
        rowVect = orgMatrix[index]
        print("\n>>colVect:%s \n>>rowVect:%s \n>> index :%s " %
              (rowVect, colVect, index))
        resultCol = transformVectToLowerSymmetric(rowVect, colVect, index)
        resultMatrix.append(resultCol)

    print("\n>>resultMatrix: %s" % (resultMatrix))
    return matrixMulti.getAllCols(resultMatrix)


def transformVectToLowerSymmetric(rowVect, colVect, index):
    resultVect = []
    subUpperColVectUp = colVect[:index]
    subLowerRowVect = rowVect[:index]

    subUpperVectDown = colVect[index:]
    # becuse the first iteration subUpperColVectUp = 0 & in the first iteration we return the same column vector
    if not (len(subUpperColVectUp) > 0 or len(subLowerRowVect) > 0):
        return colVect
    return subLowerRowVect + subUpperVectDown


vt = [[8, 9, 4], [3, 7, 2], [4, 5, 3]]
#vtb = [9, 99, 999]

print(setSymmetricFromLowerTri(vt))

# 8 9 4
# 3 7 2
# 4 5 3
# ---------
# 8 3 4
# 3 7 5
# 4 5 3
