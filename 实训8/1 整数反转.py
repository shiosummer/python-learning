num = int(input('请输入一个整数'))
if num>0:
    num1 = str(num)
    print(int(num1[::-1]))
elif num==0:
    print(0)
else:
    num1 = str(-num)
    print(-int(num1[::-1]))