tup=(8,6,9,3,5,4,6,9,5)
print('Tuple is:',tup)
print()
print('Element of tuple is:')
sum=0
for i in tup:
    print(i)
    sum+=i
print()
print('Sum of element: ',sum)
print()
print('Index position using iteration')
i=1
for val in tup:
    print(f'{val} at index position {i}')
    i+=1
print()
print('Index position using enumerate function')
for i,val in enumerate(tup):
    print(f'{val} at index position {i+1}')
print()
print('Index position using range and len function')
for i in range(len(tup)):
    print(f'{tup[i]} at index position {i+1}')
