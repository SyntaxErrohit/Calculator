def multiply(matrix_a, matrix_b):
    ma = len(matrix_a)
    na = len(matrix_a[0])
    mb = len(matrix_b)
    nb = len(matrix_b[0])
    if na != mb:
        return [[]]
    else:
        ans = [[0]*3, [0]*3, [0]*3]
        for i in range(ma):
            for j in range(nb):
                for k in range(mb):
                    ans[i][j] += matrix_a[i][k] * matrix_b[k][j]
        return ans

a = [[3, -3, 4], [2, -3, 4], [0, -1, 1]]
b = multiply(a,a)
c = multiply(b,a)
print(*c, sep='\n')