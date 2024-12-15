see = open('input3.txt')
see = see.read()

div = see.split('\n')

student_id = div[1].split(' ')

student_marks = div[2].split(' ')

for i in range(len(student_id)):
    student_id[i] = int(student_id[i])
    
for i in range(len(student_marks)):
    student_marks[i] = int(student_marks[i])

def insertion_sort(size,student_id,student_marks):
    for i in range(1,size):
        store1 = student_marks[i]
        store2 = student_id[i]
        prev = i - 1
        
        while prev >= 0:
            if student_marks[prev] < store1:
                student_marks[prev + 1] = student_marks[prev]
                student_id[prev + 1] = student_id[prev]
                
            else:
                break
            
            prev -= 1
            
        student_marks[prev + 1] = store1
        student_id[prev + 1] = store2
        
    return student_id

size = int(div[0])
sorted_id = insertion_sort(size,student_id,student_marks)

keep = open('output3.txt','w')

for i in sorted_id:
    keep.write(str(i)+' ')
    
keep.close()