dict1 = {}

see = open('input.txt')

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
    
print(dict1)

see.close()