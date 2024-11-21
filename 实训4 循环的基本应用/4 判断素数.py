#输入正整数并判断正整数
num = int(input('请输入一个正整数'))
while num<0:
    num = int(input('请重新输入一个正整数'))
#判断是否为质数
for i in range(2,num-1):
    if num%i==0:
        print(f'您输入的正整数{num}不是质数(素数)')
        break
    else:
        print(f'您输入的正整数{num}是质数(素数)')
        break