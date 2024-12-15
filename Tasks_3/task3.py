dict1 = {}

see = open('input.txt')

keep = open('output3.txt','w')

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
output = []

def DFS_VISIT(dict1, the_node):
    
    seen[int(the_node) - 1] = 1
    output.append(the_node)
    
    for x in dict1[the_node]:
        if seen[x - 1] == 0:
            DFS_VISIT(dict1, x)

            
def DFS(dict1, last):
     for j in dict1:
        if seen[j - 1] == 0:
            DFS_VISIT(dict1, j)
            
     for i in output:
             keep.write(str(i)+' ')
             if i == last:
                 break

DFS(dict1, list(dict1)[-1])

see.close()
keep.close()