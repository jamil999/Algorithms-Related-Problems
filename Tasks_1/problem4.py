def Multiply_matrix():
    n = int(input('The N for n*n matrix:'))
    mat1 = []
    
    print('The first Matrix:')
    for c in range(n):
        take = list(map(int, input().split()))
        mat1.append(take)
    mat2 = []

    print('The second Matrix:')
    for d in range(n):
        take = list(map(int, input().split()))
        mat2.append(take)    
    size = len(mat1)
    mat3  =[]

    for b in range(size):
        mat3.append([0]*size)

 
    for x in range(size):
        for y in range(size):
            for z in range(size):
                mat3[x][y] = mat3[x][y] + (mat1[x][z]*mat2[z][y]) 
     
    return mat3
    
print(Multiply_matrix())