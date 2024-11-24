#引入圆周率 小圆桶的深度h和底面半径r
import math
pi = math.pi
print('小圆桶的深度和底面半径均为整数')
h = int(input('请输入小圆桶的深度h(cm)：'))
r = int(input('请输入小圆桶的底面半径r(cm)：'))

#判断输入的数字是否正确
while h or r:
    if h<0:
        h = int(input('请重新输入正确的小圆桶的深度h(cm)：'))
    else:
        pass
    if r<0:
        r = int(input('请重新输入正确的小圆桶的底面半径r(cm)：'))
    else:
        break
#计算 输出结果
h1=h/10
r1=r/10
need=20/((pi*r1**2)*h1)
if need%1==0:
    print(f'大象至少需要喝{need}桶水')
else:
    print(f'大象至少需要喝{math.ceil(need)}桶水')
