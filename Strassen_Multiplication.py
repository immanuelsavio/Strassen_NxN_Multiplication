import numpy as np

a = []
b = []

size = int(input("Enter the size of the array 1 in 2^i"))
print("Enter the array elements of array 1")

for i in range(0, size):
    temp = []
    for j in range(0, size):
        x = int(input())
        temp.append(x)
    a.append(temp)

print("Enter the array elements of array 2")


for i in range(size):
    temp = []
    for j in range(size):
        x = int(input())
        temp.append(x)
    b.append(temp)


def zero_matrix(p, q):
    m = np.zeros((p, q))
    return m


def splitting_fun(m):
    a = m
    b = m
    c = m
    d = m
    while(len(a) > len(m)/2):
        a = a[:len(a)//2]
        b = b[:len(b)//2]
        c = c[len(c)//2:]
        d = d[len(d)//2:]
    while(len(a[0]) > len(m[0])/2):
        for i in range(len(a[0])//2):
            a[i] = a[i][:len(a[i])//2]
            b[i] = b[i][len(b[i])//2:]
            c[i] = c[i][:len(c[i])//2]
            d[i] = d[i][len(d[i])//2:]
    return a, b, c, d


def matrix_addition(a, b):
    if type(a) == int:
        d = a + b
    else:
        d = []
        for i in range(len(a)):
            c = []
            for j in range(len(a[0])):
                c.append(a[i][j] + b[i][j])
            d.append(c)
    return d


def matrix_subtract(a, b):
    if type(a) == int:
        d = a - b
    else:
        d = []
        for i in range(len(a)):
            c = []
            for j in range(len(a[0])):
                c.append(a[i][j] - b[i][j])
            d.append(c)
    return d


def strassen(a, b, q):
    # base case: 1x1 matrix
    if q == 1:
        d = [[0]]
        d[0][0] = a[0][0] * b[0][0]
        return d
    else:
        # split matrices into quarters
        a11, a12, a21, a22 = splitting_fun(a)
        b11, b12, b21, b22 = splitting_fun(b)

        # p1 = (a11+a22) * (b11+b22)
        p1 = strassen(matrix_addition(a11,a22), matrix_addition(b11,b22), q/2)

        # p2 = (a21+a22) * b11
        p2 = strassen(matrix_addition(a21,a22), b11, q/2)

        # p3 = a11 * (b12-b22)
        p3 = strassen(a11, matrix_subtract(b12,b22), q/2)

        # p4 = a22 * (b12-b11)
        p4 = strassen(a22, matrix_subtract(b21,b11), q/2)

        # p5 = (a11+a12) * b22
        p5 = strassen(matrix_addition(a11,a12), b22, q/2)

        # p6 = (a21-a11) * (b11+b12)
        p6 = strassen(matrix_subtract(a21,a11), matrix_addition(b11,b12), q/2)

        # p7 = (a12-a22) * (b21+b22)
        p7 = strassen(matrix_subtract(a12,a22), matrix_addition(b21,b22), q/2)


        # c11 = p1 + p4 - p5 + p7
        c11 = matrix_addition(matrix_subtract(matrix_addition(p1, p4), p5), p7)

        # c12 = p3 + p5
        c12 = matrix_addition(p3, p5)

        # c21 = p2 + p4
        c21 = matrix_addition(p2, p4)

        # c22 = p1 + p3 - p2 + p6
        c22 = matrix_addition(matrix_subtract(matrix_addition(p1, p3), p2), p6)

        c = zero_matrix(len(c11)*2, len(c11)*2)
        for i in range(len(c11)):
            for j in range(len(c11)):
                c[i][j] = c11[i][j]
                c[i][j+len(c11)] = c12[i][j]
                c[i+len(c11)][j] = c21[i][j]
                c[i+len(c11)][j+len(c11)] = c22[i][j]

        return c


print("The multiplied matrix is:")
print(strassen(a, b, size))
