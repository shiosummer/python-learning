def parking(times,pay):
    if 0<times<=15:
        pay=0
        return f'停车时间为{times}分钟,收费{pay}元'
    elif 15<times<=120:
        pay = 2
        return f'停车时间为{times}分钟,收费{pay}元'
    elif times>120:
        if times%60!=0:
            pay = 2+(((times-120)//60)+1)*3
        elif times%60==0:
            pay = 2+((times-120)//60)*3
        if pay>=50:
            pay=50
        return f'停车时间为{times}分钟,收费{pay}元'
    else:
        return '错误的停车时间，请重新输入'

if __name__ == '__main__':
    print(parking(int(input('请输入停车时间')),0))