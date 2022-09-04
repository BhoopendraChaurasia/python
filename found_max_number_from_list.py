list=[8,9,6,47,52,3,20,50,8,80]
max=list[0]
for i in range(len(list)):
    if max<list[i]:
        max=list[i]
print('Maximum number is',max)
