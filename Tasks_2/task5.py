see = open('input5.txt')
see = see.read()

div = see.split('\n')

b_array = div[0].split(' ')

for i in range(len(b_array)):
    b_array[i] = int(b_array[i])
    

import time

def quickShort(the_array, first, last):
    
    
    if last > first:
        parti = partition(the_array, first, last)
        quickShort(the_array, first, parti - 1)
        quickShort(the_array, parti + 1, last)
        
    return the_array
        
def partition(the_array, first, parti):
    the_piv = the_array[first]
    arr_idx = first
    
    for i in range(first + 1, parti + 1):
        if the_piv >= the_array[i]:
            arr_idx += 1
            
    
            store = the_array[i]
            the_array[i] = the_array[arr_idx]
            the_array[arr_idx] = store
     
    store1 = the_array[first]
    the_array[first] = the_array[arr_idx]
    the_array[arr_idx] = store1
    
    return arr_idx

def findK(the_array, first, last, k):
    
    if first == last:
        return the_array[last]
    
    parti2 = findK_partition(the_array, last, first)
    take = parti2 - first + 1
    if take == k:
        return the_array[parti2]
    
    elif k < take:
        return findK(the_array, first, parti2 - 1, k)
    
    else:
        return findK(the_array, parti2 + 1, last, k - take)
    
def findK_partition(the_array, last, first):
    start = first - 1
    end = the_array[last]
    
    while last > first:
        
        if end >= the_array[first]:
            start += 1
            store = the_array[first]
            the_array[first] = the_array[start]
            the_array[start] = store
            
            first += 1

    store1 = the_array[start + 1]
    the_array[start + 1] = the_array[last]
    the_array[last] = store1

    return start + 1            
        
the_array = [-3,5,6,2,1,6,2]

prev_array = []

for x in the_array:
    prev_array.append(x)
    
starting_time = time.time()
sorted_array = quickShort(the_array, 0, len(the_array) - 1)
ending_time = time.time()

difference = ending_time - starting_time

# Time complexity of the quick sort is O(n(log(n)))

keep = open('output5.txt','w')


print('The Unsorted array:')
print(prev_array)
print('After perferming quick Sorting the sorted array:')
print(sorted_array)
print('The time it will take:',difference)

for e in range(1,len(div)):
    keep.write(str(findK(b_array,0, len(b_array) - 1, int(div[e]))))
    keep.write('\n')
    
keep.close()     