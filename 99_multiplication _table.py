i=1
j=1
for j in range(1,10):
    for i in range(1,j+1):
        print(str(i)+'*'+str(j)+'='+str(i*j),end='  ')
    print()