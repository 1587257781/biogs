#author:Administrator
#date:2018/10/13 0013,22:26
#week:
name=input('name:')
age=input('age:')
Job=input('job:')
salary=input('salary:')
years=0
if salary.isdigit():
    years=65-int(age)
else:
    print('age must be digit')
msg='''
-----------info of %s-------------
Name:%s
Age:%s
Job:%s
Salary:%s
He still has %s years of retirement
--------------End--------------------
'''%(name,name,age,Job,salary,years)
print(msg)