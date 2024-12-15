dict1 = {}
dict2 = {}

def Network(dict1, dict2, source):
    wei = [float('-inf')] * (len(dict2) + 1)
    par = [None] * (len(dict2) + 1)
    prior_q = {}

    wei[source] = float('inf')
    
    prior_q[wei[source]] = source
        
    while prior_q != {}:
        m = max(prior_q.keys())    
        max1 = prior_q.pop(m)
        
        for nei in dict2[max1]:
            check =min(wei[max1] , dict1[max1, nei])
    
            if check > wei[nei]:
                wei[nei] = check
                par[nei] = max1
                
                prior_q[wei[nei]]  = nei
    
    for i in range(1,len(wei)):
        if wei[i] == float('inf'):
            keep.write(str(0) + ' ')
            
        elif wei[i] == float('-inf'):
            keep.write(str(-1) + ' ')
            
        else:
            keep.write(str(wei[i]) + ' ')
            
    keep.write('\n')

see = open('input5.txt')

keep = open('output5.txt','w')

t = see.readline()

for a in range(int(t)):
    nm = see.readline().split()
    
    nm = list(map(int, nm))
    
    for a in range(1,nm[0]+1):
        dict2[a] = []
    
    for i in range(nm[1]):
        connection = see.readline().split()
        
        connection = list(map(int, connection))
        
        u = connection[0]
        v = connection[1]
        w = connection[2]
        
        dict1[u , v] = w
        
        if u in dict2:
            dict2[u].append(v)
            
        else:
            dict2[u] = [v]
        
    source = see.readline().split()
    Network(dict1, dict2, int(source[0]))
    
    dict1.clear()
    dict2.clear()
    
see.close()
keep.close()