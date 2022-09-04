list=[5,5,6,6,3,3,5,4,8,8,9]
print('List is:',list)

print('Element of List: ')
sum=0
for i in list:
    print(i)
    sum+=i
print('Sum of elements:',sum)
print()
print('Index position of elements using enumerate function')
for i,val in enumerate(list):
    print(f'{val} is index position {1+i}')
print()
print('Index position of elements using range and len function')
for i in range(len(list)):
    print(f'{list[i]} id index position {i}')
print()
print('Index position of elements using iteration')
i=1
for val in list:
    print(f'{val} is index position {i}')
    i+=1
