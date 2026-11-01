def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    m = len(a)
    n = len(a[0])
    p = len(b[0])

    # 维度检查
    if len(a[0]) != len(b):
        return -1

    res = []
    for i in range(m):        # 遍历a的每一行
        new_row = []
        for k in range(p):    # 遍历b的每一列
            s = 0
            for j in range(n):# 求和
                s += a[i][j] * b[j][k]
            new_row.append(s)
        res.append(new_row)
    return res