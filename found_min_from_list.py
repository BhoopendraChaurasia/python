list1=list=[8,65,6,9,41,2,6,7,4]
print('List is:',list)
print()
print('Find Minimum number using traditional method')
min=list[0]
for i in range(len(list)):
    if min>list[i]:
        min=list[i]
print('Mimimum number is:',min)
print()
print('Find Minimum number using by sort function')
list.sort();
print('Minimum number is:',*list[:1])
