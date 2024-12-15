see  = open('input3.txt')

keep = open('output3.txt','w')

take = see.read().split('\n')

def LCS(f, s, t):
    fm = len(f) + 1
    sn = len(s) + 1
    tz = len(t) + 1
    
    lc = [[ [0 for i in range(sn)] for j in range(tz)] for k in range(fm)]

    for a in range(1,fm):
        for b in range(1,sn):
            for c in range(1,tz):
                if a == 0 or b == 0 or c == 0:
                    lc[a][b][c] = 0
                    
                else:
                    if f[a - 1] == s[b - 1] and f[a - 1] == t[c - 1]:
                       lc[a][b][c] = 1 + lc[a - 1][b - 1][c - 1]
                       
                    else:
                        if lc[a - 1][b][c] >= lc[a][b - 1][c]:
                            maxi = lc[a - 1][b][c]
                            if maxi >= lc[a][b][c - 1]:
                                lc[a][b][c] = maxi
                                
                            else:
                                maxi = lc[a][b][c - 1]
                                lc[a][b][c] = maxi
                                
                        else:
                            maxi = lc[a][b - 1][c]
                            if maxi >= lc[a][b][c - 1]:
                                lc[a][b][c] = maxi
                                
                            else:
                                maxi = lc[a][b][c - 1]
                                lc[a][b][c] = maxi
            
    keep.write(str(lc[len(f)][len(s)][len(t)]))
    
LCS(take[0], take[1], take[2])

see.close()
keep.close()