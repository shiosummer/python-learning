#定义检查函数
def delta(a,b,c):
   if a+b>c and a+c>b and b+c>a:
       return '能构成三角形'
   else:
       return '不能构成三角形'

#输入三角形三边
a = int(input('请输入第一个边长'))
b = int(input('请输入第二个边长'))
c = int(input('请输入第三个边长'))

#调用函数
result = delta(a,b,c)
print(result)