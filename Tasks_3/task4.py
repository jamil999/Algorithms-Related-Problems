dict1 = {}

def the_BFS(seen, dict1, first, last, dis):

    seen[int(first) - 1] = 1
    the_queue.append(int(first))
    
    while the_queue != []:
        out = the_queue.pop(0)
     
        for nei in dict1[out]:
            if seen[nei - 1] == 0:
                seen[nei - 1] = 1
                the_queue.append(nei)
                dis[nei] = dis[out] + 1
               
see = open('input4.txt')

keep = open('output4.txt','w')

total_graphs = see.readline()

for b in range(int(total_graphs)):
    n_m_1 = see.readline()
    
    n_m_1 = n_m_1.split()
    
    n1 = n_m_1[0]
    m1 = n_m_1[1]
    
    for i in range(int(m1)):
        line = see.readline()
        line = line.split()
        
        line = list(map(int, line))
        
      
        nd1 = line[0]
        
        for a in range(int(n1)):
            for x in line:
                if x not in dict1:
                    dict1[x] = []
       
        if len(line) > 1:
            for j in range(1,len(line)):
                dict1[line[0]].append(line[j])
        
        if len(line) > 1:
            for j in range(1,len(line)):
                dict1[line[j]].append(line[0])
                    
    #print(dict1)
       
    seen = int(n1) * [0]
    dis = (int(n1) + 1) * [0]
    the_queue = []
    the_BFS(seen,dict1, 1, int(n1), dis)
    
    keep.write(str(dis[int(n1)]))
    keep.write('\n')
    
    dict1.clear()
    seen.clear()
    dis.clear()
    the_queue.clear()
    
see.close()
keep.close()