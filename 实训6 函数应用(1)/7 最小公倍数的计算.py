#定义公倍数的计算过程
def minMultiplier(a,b):
   x=a*b
   while a!=b:
       if a>b:
           a=a-b
       else:
           b=b-a
   return x//a

#输入数字及输出结果
a=int(input('请输入第一个数字'))
b=int(input('请输入第二个数字'))
print(minMultiplier(a,b))