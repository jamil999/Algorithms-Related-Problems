dict1 = {}

see = open('input.txt')

keep = open('output2.txt','w')

keep.write('Places: ')

nodes_num = see.readline()

for i in range(int(nodes_num)):
    line = see.readline()
    line = line.split()
    
    line = list(map(int, line))
    
    n = line[0]

    dict1[n] = []

    if len(line) > 1:
        for j in range(1,len(line)):
            dict1[n].append(line[j])
    
seen = int(nodes_num) * [0]
the_queue = []

def the_BFS(seen, dict1, first, last):

    seen[int(first) - 1] = 1
    the_queue.append(int(first))
    
    while the_queue != []:
        out = the_queue.pop(0)
        keep.write(str(out)+' ')
        
        if out == int(last):
            break
        
        for nei in dict1[out]:
            if seen[nei - 1] == 0:
                seen[nei - 1] = 1
                
                the_queue.append(nei)
                
the_BFS(seen, dict1, list(dict1)[0], list(dict1)[-1])

see.close()
keep.close()