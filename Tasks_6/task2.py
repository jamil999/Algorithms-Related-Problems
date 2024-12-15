see  = open('input2.txt')

keep = open('output2.txt','w')

take = see.read().split('\n')

def LCS(n,f,s):
    
    zone_seq = {'Y': 'Yasnaya', 'R': 'Rozhok', 'S': 'School', 'P': 'Pochinki', 'F': 'Farm', 'M': 'Mylta', 'H': 'Shelter', 'I': 'Prison'}
    
    str1 = ''
    fm = len(f) + 1
    fn = len(s) + 1
    
    lc = [[0 for i in range(fm)] for j in range(fn)]
    lt = [[0 for i in range(fm)] for j in range(fn)]

    for x in range(1, fm):
        lc[x][0] = 0
        lt[x][0] = None
        
    for y in range(1, fn):
        lc[0][y] = 0
        lt[0][y] = None
        
    for a in range(1,fm):
        for b in range(1,fn):
            if f[a - 1] == s[b - 1]:
               lc[a][b] = lc[a - 1][b - 1] + 1
               lt[a][b] = 'd'
               
            elif lc[a - 1][b] >= lc[a][b - 1]:
                lc[a][b] = lc[a -1][b]
                lt[a][b] = 'u'
                
            else:
                lc[a][b] = lc[a][b - 1]
                lt[a][b] = 'l'                

    r = len(f) - 1
    k = len(s) - 1

    while r >= 0 or k >= 0:
        if f[r] == s[k]:
            str1 = str1 + f[r]
            r = r - 1
            k = k - 1
            
        elif lc[r - 1][k] >= lc[r][k - 1]:
            k = k - 1
            
        else:
            r = r - 1

    for z in str1[::-1]:
        keep.write(zone_seq[z]+' ')   

    correctness = (len(str1) * 100) / int(n)
    
    keep.write('\nCorrectness of prediction: '+str(int(correctness))+'%')

LCS(take[0], take[1], take[2])

see.close()
keep.close()