key = []
value = []
list1 = []
output = []

see  = open('task1_input.txt')

keep = open('task1_output.txt','w')

tasks = see.readline()

sort_li = [0] * int(tasks)

for i in range(int(tasks)):
    task = see.readline().split()
    
    task = list(map(int, task))
    
    key.append(task[0])
    value.append(task[1])

sort_value =sorted(value)

for j in sort_value:
    if j in value:
        l = []
        l.append(key[value.index(j)])
        l.append(j)
    
        list1.append(l)
    
        key.pop(value.index(j))
        value.remove(j)

total = 1
fin = list1[0][1]
output.append(list1[0])

for i in list1[1::]:
    if i[0] >= fin:
        total = total + 1
        fin = i[1]
        
        output.append(i)

keep.write(str(total))
keep.write('\n')

for o in output:
    keep.write(str(o[0])+' '+str(o[1]))
    keep.write('\n')

see.close()
keep.close()