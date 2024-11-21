#输入用户名
name = input('请输入用户名：\n')
for i in range(1,3):
    if name == 'root':
        break
    else:
        name = input('请重新输入用户名：\n')
#输入密码
if i != 2 or name == 'root':
    password = input('请输入用户密码(剩余次数3)：\n')
    for j in range(1,3):
        if password == 'sa123456':
            break
        else:
            password = input(f'请重新输入用户密码(剩余次数{3-j})：\n')
    if password =='sa123456':
        print('登陆成功')
    else:
        print('登陆失败')
else:
    print('登录失败')