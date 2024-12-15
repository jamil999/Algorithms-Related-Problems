key = []
value = []
list1 = []
dictp ={}

see  = open('task2_input.txt')

keep = open('task2_output.txt','w')

nm = see.readline().split()

for i in range(int(nm[0])):
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

for i in range(1,int(nm[1])+1):
    dictp[i] = []

for x in range(1,int(nm[1])+1):
    for i in list1:
        if dictp[x] == []:
            
            fin1 = i[1]
            dictp[x] = [i[1]]
            list1.remove(i)
            
        else:
            if i[0] >= fin1:
                fin1 = i[1]
                dictp[x].append(i[1])   
                list1.remove(i)

total = 0
for k in dictp:
    total = total + len(dictp[k])

keep.write(str(total))

see.close()
keep.close()