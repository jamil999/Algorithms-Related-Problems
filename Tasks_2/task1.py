see = open('input1.txt')
see = see.read()

div = see.split('\n')

the_list = div[1].split(' ')

for i in range(len(the_list)):
    the_list[i] = int(the_list[i])
    
def bubblesort(size,the_array):
    length = size
    checker = 0
    
    for x in range(length - 1):

        for y in range(length - x - 1):
     
            if the_array[y + 1] < the_array[y]:
                checker = 1
                store = the_array[y]
                the_array[y] = the_array[y + 1]
                the_array[y + 1] = store
                
        if checker == 0:
            break

    return the_array

size = int(div[0])
cap = bubblesort(size,the_list)

keep = open('output1.txt','w')

for i in cap:
    keep.write(str(i)+' ')
    
keep.close()


# In the case of bubble sort the best case scinario will be when the
#array is already sorted. So for example [1,2,3,4,5] this array will be
#best case scinario. So, I took a variable 'checker' in the function which is
#set to 0. if if any swapping happens then the checker will be set to 1.
#But in the first checking if the checker remains 0 then the array is
#already sorted. So, after first loop if checker is 0 then there is no need
#to check second time and we can break the loop. That is how it can be done for
#best case scinario.