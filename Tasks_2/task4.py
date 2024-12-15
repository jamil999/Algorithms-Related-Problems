see = open('input4.txt')
see = see.read()

div = see.split('\n')

the_array = div[1].split(' ')

for i in range(len(the_array)):
    the_array[i] = int(the_array[i])
    
    
def merge(the_array, first, middle, last):
    len1 = middle - first + 1
    len2 = last - middle
    
    l_array = [0 for a in range(len1)]
    r_array = [0 for b in range(len2)]
    
    for x in range(len1):
        l_array[x] = the_array[first + x]
        
    for y in range(len2):
        r_array[y] = the_array[middle + y + 1]
        
        
    point_i = 0
    point_j = 0
    point_k = first
    
    while len1 > point_i and len2 > point_j:
        if r_array[point_j] >= l_array[point_i]:
            the_array[point_k] = l_array[point_i]
            point_i = point_i + 1
            
        else:
            the_array[point_k] = r_array[point_j]
            point_j = point_j + 1
            
        point_k = point_k + 1

    while len1 > point_i:
        the_array[point_k] = l_array[point_i]
        point_i = point_i + 1
        point_k = point_k + 1
        
    while len2 > point_j:
        the_array[point_k] = r_array[point_j]
        point_j = point_j + 1
        point_k = point_k + 1
        

def merge_sort(the_array, first, last):
    if last > first:
        middle = (first + last) // 2
        
        merge_sort(the_array, first, middle)
        merge_sort(the_array, middle + 1, last)
        merge(the_array, first, middle, last)
        
    return the_array

merged_array = merge_sort(the_array, 0, int(div[0]) - 1)

keep = open('output4.txt','w')

for i in merged_array:
    keep.write(str(i)+' ')
    
keep.close()
    
