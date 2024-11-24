#输入一个三位数
num = int(input('请输入一个三位数：'))
while num>999 or num<100:
    num = int(input('请重新输入一个三位数：'))

#提取百分位数 十位数 个位数
a = num//100
b = num//10%10
c = num%10

#判断是否为水仙花数
if a**3+b**3+c**3==num:
    print('您输入的数字为水仙花数')
else:
    print('您输入的数字不是水仙花数')
