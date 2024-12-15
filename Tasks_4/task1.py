dict1 = {}
dict2 = {}

see = open('input1.txt')

keep = open('output1.txt','w')

def Dijkstra(dict1, dict2, source):
    wei = [float('inf')] * (len(dict2) + 1)
    par = [None] * (len(dict2) + 1)
    prior_q = {}
    visi = [False] * (len(dict2) + 1)

    wei[source] = 0
    
    prior_q[wei[source]] = source
        
    while prior_q != {}:
        m = min(prior_q.keys())    
        min1 = prior_q.pop(m)
        
        if visi[min1]:
            continue
        
        visi[min1] = True
        
        for nei in dict2[min1]:
            check = wei[min1] + dict1[min1, nei]
    
            if check < wei[nei]:
                wei[nei] = check
                par[nei] = min1
                
                prior_q[wei[nei]]  = nei
                

    keep.write(str(wei[len(dict2)]))
    keep.write('\n')

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
        
    #print(dict1)
    #print(dict2)

    Dijkstra(dict1, dict2, next(iter(dict2)))

    dict1.clear()
    dict2.clear()
    
see.close()
keep.close()