see = open('input2.txt')
see = see.read()

div = see.split('\n')

div1 = div[0].split(' ')

div2 = div[1].split(' ')

for i in range(len(div1)):
    div1[i] = int(div1[i])
    
for i in range(len(div2)):
    div2[i] = int(div2[i])

def selection_sort(m_n, the_array):
    
    for i in range(m_n[0]):
        i_min = i
        for x in range(i + 1, m_n[0]):
            if the_array[x] < the_array[i_min]:
                i_min = x
            
        store = the_array[i]
        the_array[i] = the_array[i_min]
        the_array[i_min] = store
    
    return the_array

sorted_array = selection_sort(div1,div2)


keep = open('output2.txt','w')

for i in range(div1[1]):
    keep.write(str(sorted_array[i])+' ')
    
keep.close()