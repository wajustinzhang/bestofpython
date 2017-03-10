import numpy

def transpose1(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def transpose2(matrix):
    return zip(*matrix)

def transpose3(matrix):
    return map(list, zip(*matrix))

def transpose4(matrix):
    return numpy.transpose(matrix)

def printMatrix(matrix):
    for x in matrix:
        print(x)

if __name__ =="__main__":
    m = [[1,2,3,4],[5,6,7,8]]

    printMatrix(transpose1(m))

    print("\n")

    printMatrix(transpose2(m))

    print('\n')

    printMatrix(transpose3(m))

    print('\n')

    printMatrix(transpose4(m))