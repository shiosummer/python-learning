#定义公倍数的计算过程
def gbs(m,n):
   x=m*n
   while m!=n:
       if m>n:
           m=m-n
       else:
           n=n-m
   return x//m

#输入数字及输出结果
m=int(input('请输入第一个数字'))
n=int(input('请输入第二个数字'))
print(gbs(m,n))