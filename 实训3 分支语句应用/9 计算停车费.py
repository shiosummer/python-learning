#导入math库 引入变量停车时间P_time
import math
P_time = int(input('请输入停车时间（分钟）：'))

#判断输入时间是否错误 计算并输出结果
while P_time:
    if 0<=P_time<15:
        Cost = 0
        print(f'停车{P_time}分钟，缴费{Cost}元')
        break
    elif 15<=P_time<120:
        Cost = 2
        print(f'停车{P_time}分钟，缴费{Cost}元')
        break
    elif P_time>=120:
        Cost = 2+3*math.ceil((P_time-120)/60)
        if 0<Cost<=50:
            print(f'停车{P_time}分钟，缴费{Cost}元')
            break
        else:
            print(f'停车{P_time}分钟，缴费50元')
            break
    else:
        P_time = int(input('请重新输入正确的停车时间（分钟）：'))
