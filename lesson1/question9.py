L=[1,2,3,4,5]
reserved_L=L[::-1]
for i in reserved_L:
    print(i,end=' ')
i=0
print()
while True:
    if(i==5): break
    print(reserved_L[i],end=' ')
    i=i+1