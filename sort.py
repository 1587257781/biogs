num1=int(input('Enter a number:\n'))
num2=int(input('Enter a number:\n'))
num3=int(input('Enter a number:\n'))
num4=int(input('Enter a number:\n'))
num5=int(input('Enter a number:\n'))
a=[num1,num2,num3,num4,num5]
temp=a[0]
x=0
for i in range(0,len(a)):
    temp=a[i]
    for j in range(i,len(a)):
        if temp>a[j]:
            temp=a[j]
            x=j
    if a[i]!=temp:
        b=a[i]
        a[i]=temp
        a[x]=b
print(a)
###This is an arbitrary length data sorting algorithm
