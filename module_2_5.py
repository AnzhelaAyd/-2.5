def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix


n = int(input('n= '))
m = int(input('m= '))
value = int(input('value= '))

result = get_matrix(n, m, value)
if n == 0 or m == 0:
    print('Данная матрица не существует ')
else:
    print(result)
