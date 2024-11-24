#导入math库 引入变量时间time 用户套餐user
import math
Time = math.ceil(int(input('请输入本月通话时间(min)：')))
User = input('是否为固定套餐用户(Y/N)：')

#判断 计算 输出
while Time and User:
    if User == 'Y':
        if 0<Time<=300:
            Cost = 50
            print(f'您本月的话费为：{Cost}元')
            break
        elif Time>300:
            Cost = 50+0.1*(Time-300)
            print(f'您本月的话费为：{Cost}元')
            break
        else:
            Time = math.ceil(int(input('请重新正确输入本月通话时间(min)：')))
    elif User =='N':
        Cost = 0.2*Time
        print(f'您本月的话费为：{Cost}元')
        break
    else:
        User = input('请重新确认是否为固定套餐用户(Y/N)：')
