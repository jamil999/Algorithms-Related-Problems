see = open('input.txt')
see = see.read()

line = see.split('\n')

keep1 = open('output.txt','w')
keep2 = open('record.txt','w')

odd_counter = 0
even_counter = 0
palindrome_counter = 0

def paritychecker(value):
    global odd_counter
    global even_counter
    if value.isdigit():
        if int(value) % 2 != 0:
            odd_counter += 1
            return value+' has odd parity'

        else:
            even_counter += 1
            return value+' has even parity'

    else:
        return value+' cannot have parity'
    
    
def isPalindrome(letter):
    global palindrome_counter
    size = len(letter)
    if size == 0:
        return ' and no word is found so no palindrome'
    
    middle = size // 2
    for i in range(0,middle):
        if letter[i] != letter[size - 1 - i]:
            return ' and '+letter+' is not a palindrome'
    
    palindrome_counter += 1
    return ' and '+letter+' is a palindrome'
    
for x in line:
    x = x.split(' ')
    keep1.write(paritychecker(x[0]))
    keep1.write(isPalindrome(x[1]))
    keep1.write('\n')

percen_odd = int(odd_counter/len(line)*100)
percen_even = int(even_counter/len(line)*100)
percen_palin = int((palindrome_counter/len(line))*100)

keep2.write('Percentange of odd parity: '+str(percen_odd)+'%\n')
keep2.write('Percentange of even parity: '+str(percen_even)+'%\n')   
keep2.write('Percentange of no parity: '+str(100-(percen_odd+percen_even))+'%\n')
keep2.write('Percentange of palindrome: '+str(percen_palin)+'%\n')
keep2.write('Percentange of non-palindrome: '+str(100-percen_palin)+'%')

keep1.close()
keep2.close()