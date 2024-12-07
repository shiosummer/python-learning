#输入并判断两个正整数
def panduan(num1,num2):
    if num1<0:
        return panduan(int(input('请重新输入第一个正整数')),num2)
    elif num2<0:
        return panduan(num1,int(input('请重新输入第二个正整数')))
    return num1,num2
#计算输出两个数的公约数
def gongyueshu(num1,num2):
    if num1>num2:
        return gongyueshu(num1-num2,num2)
    elif num2>num1:
        return gongyueshu(num1,num2-num1)
    else:
        return f'两个数的最小公约数为{num1}'

if __name__=='__main__':
    num1, num2 = panduan(int(input('请输入第一个正整数')), int(input('请输入第二个正整数')))
    print(gongyueshu(num1,num2))