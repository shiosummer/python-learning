def username(i,name):
    if name != 'admin':
        if i < 3:
            print(f'登陆失败,还剩{3-i}次机会')
            return username(i+1,input('请重新输入用户名:'))
        else:
            return '用户名错误，登陆失败'
    else:
        password = input('请输入密码：')
        return passwords(1,password)
def passwords(j,password):
    if password != 'admin':
        if j < 3:
            print(f'登陆失败，还剩{3-j}次机会')
            return passwords(j+1,input('请重新输入密码：'))
        else:
            return '密码错误，登陆失败'
    else:
        return f'您好{name},登陆成功'

if __name__ == '__main__':
    name = input('请输入用户名：')
    print(username(1,name))