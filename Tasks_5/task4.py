import math

see  = open('task4_input.txt')

keep = open('task4_output.txt','w')

while True:
    
    s = see.readline().split()

    a = int(s[0])
    b = int(s[1])

    if a == 0 and b == 0:
        break

    else:
        c = 0  
        sq = math.sqrt(a)
  
        while sq * sq <= b:  
            c = c + 1
            sq = sq + 1
            
        keep.write(str(c))
        keep.write('\n')
        
see.close()
keep.close()