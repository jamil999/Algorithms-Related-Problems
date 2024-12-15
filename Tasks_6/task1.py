count = 0

see  = open('input1.txt')

keep = open('output1.txt','w')

value = see.read()

while int(value) > 0:
    div = list(str(value))
    maxi = int(max(div))
    
    value = int(value) - maxi
    
    count = count + 1

keep.write(str(count))

see.close()
keep.close()  