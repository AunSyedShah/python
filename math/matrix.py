# matrix in 2 dimensional 2 x 2 matrix
m = [
    [2, 3],
    [5, 6]
]
# adjoint left blank for future use
adjoint = [
    [ 0, 0],
    [0, 0]
]
# calculating determinant
d = (m[0][0] * m[1][1]) - (m[0][1] * m[1][0])
if d != 0:
    adjoint[0][0] = m[1][1]
    adjoint[0][1] = m[0][1] * -1
    adjoint[1][0] = m[1][0] * - 1
    adjoint[1][1] = m[0][0]
    for i in adjoint:
        print(i)
else:
    print("matrix is non singular")
