see  = open('task3_input.txt')

keep = open('task3_output.txt','w')

t = see.readline().split()

h = see.readline().split()

h = list(map(int,h))

sort1 =sorted(h)

s = see.readline()

st = []

sq = ''

pointer = 0

jack_h = 0
jill_h = 0

for x in s:
    if x == 'J':
        st.append(sort1[pointer])
        sq = sq + str(sort1[pointer])
        jack_h = jack_h + sort1[pointer]
        pointer = pointer + 1
        
        
    elif x == 'j':
        take = st.pop()
        sq = sq + str(take)
        jill_h = jill_h + take

keep.write(sq+'\n')
keep.write('Jack will work for '+str(jack_h) +' hours\n')
keep.write('Jill will work for '+str(jill_h) +' hours')
        
see.close()
keep.close()