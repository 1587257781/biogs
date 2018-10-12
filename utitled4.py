cmd=input('请输入您要操作的命令：1.登录系统，2.退出系统\n')#退出系统好使
f1=open('D:\\深度学习工作目录\\user_password.txt','r+')
f2=open('D:\\深度学习工作目录\\locked_user.txt','r+')
k=0

if cmd.isdigit() and int(cmd)==2:
    exit()
elif cmd.isdigit() and int(cmd)==1:
    match = False
    user_name = input('请输入用户名：')
    password = input('请输入该用户的密码：')
    x = 0
    while k<3:
        k = k + 1
        for i in f2.readlines():
            u=i.split()
            if user_name==u[0]:
                print('该用户已被锁定')
                exit()

        for j in f1.readlines():
            u, p = j.strip('\n').split()
            if u == user_name:
                for x in range(2):
                    if password == p:
                        match = True
                        print('账号和密码匹配')
                        break
                    else:
                        password = input('请再次输入该用户的密码：')
                    x=x+1
if match==False:
    f2.write('%s\n'%user_name)
    print('登录已超过三次，账号已被锁定')
    print('登录失败')
    f2.close()
    f1.close()
    exit()
else :
    print('登录成功')


