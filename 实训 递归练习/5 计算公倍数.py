#输入并判断两个正整数
def panduan(num1,num2):
    if num1<0:
        return panduan(int(input('请重新输入第一个正整数')),num2)
    elif num2<0:
        return panduan(num1,int(input('请重新输入第二个正整数')))
    return num1,num2
#计算并输出最小公倍数
def gongbeishu(num1,num2):
    if num1 > num2:
        return gongbeishu(num1-num2,num2)
    elif num1 < num2:
        return gongbeishu(num1,num2-num1)
    print(f'您输入的两个数的最小公倍数为{x//num1}')

if __name__=='__main__':
    num1,num2 = panduan(int(input('请输入第一个正整数')),int(input('请输入第二个正整数')))
    x = num1 * num2
    gongbeishu(num1,num2)