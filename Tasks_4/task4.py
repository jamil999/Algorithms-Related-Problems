dict1 = {}
dict2 = {}
rank = []

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
                
    path = []
    real_path = []
    x = 10
    path.append(x)
    
    while par[x] != None:
        path.append(par[x])
        
        x = par[x]
        
    path.reverse()
    
    for p in path:
        keep.write(rank[p] + ' ')
        real_path.append(rank[p])
        
    #print(real_path)
    
    
see = open('input4.txt')

keep = open('output4.txt','w')

while True:   
    connection = see.readline().split()
 
    if connection == []:
        break   
    
    for f in connection:
        if f not in rank and f.isdigit() == False:
            rank.append(f)
            
    u = connection[0]
    v = connection[1]
    w = int(connection[2])
            
    dict1[rank.index(u) , rank.index(v)] = w
            
    if rank.index(u) in dict2:
        dict2[rank.index(u)].append(rank.index(v))
                
    else:
        dict2[rank.index(u)] = [rank.index(v)]
        
    for a in range(0,len(rank)):
        if a not in dict2:
            dict2[a] = []
            
Dijkstra(dict1, dict2, 0)

see.close()
keep.close()

# We can't use bfs algorithm is this case because bfs
#only finds the shortest path in terms of node. So, it
# works perfectly for unweighted or same weighted graph but
# as here there is traffic level which means it's a weighted
# graph and so here not bfs but dijkstra algorithm will
# help to find the shortest path in terms of the weight