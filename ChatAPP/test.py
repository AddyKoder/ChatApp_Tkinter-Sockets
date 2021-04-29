a = {2:'2',4:'4'}

a[1] = '1'


for i in a.keys():
    if a[i] == '1':
        a.pop(i)
        break

print(a)