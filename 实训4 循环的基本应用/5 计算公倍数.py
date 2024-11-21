#输入并判断两个正整数
num1 = int(input('请输入第一个正整数'))
while num1<0:
    num1 = int(input(('请重新输入第一个正整数')))
num2 = int(input('请输入第二个正整数'))
while num2<0:
    num2 = int(input(('请重新输入第二个正整数')))
#计算并输出最小公倍数
x = num1*num2
while num1!=num2:
    if num1 > num2:
        num1 = num1-num2
    else:
        num2=num2-num1
print(f'您输入的两个数的最小公倍数为{x//num1}')
