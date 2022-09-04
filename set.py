set={2,5,8,9,6,6,4,8,9,6,3}
print('Set is:', set)
print()
print('Elements of set:')
sum=0
for i in set:
    print(i)
    sum+=i
print('Sum:',sum)
print()
print('Index position using iteration')
i=1
for val in set:
    print(f'{val} at index position {i}')
print()
print('Index position using enumerate function')
for i,val in enumerate(set):
    print(f'{val} at index position {i+1}')
# print()
# print('Index position using range and len function')
# for i in range(len(set)):
#     print(f'{set} at index position {i}')
