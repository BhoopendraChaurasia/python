list=[8,65,6,9,41,2,6,7,4]
min=list[0]
for i in range(len(list)):
    if min>list[i]:
        min=list[i]
print('Mimimum number is:',min)
