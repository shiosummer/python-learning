#导入math库 引入邮件重量M与是否需要加急的变量Fast
import math
M = math.ceil(int(input('请输入您的邮件重量（g)：')))
Fast = input('请确认您的邮件是否需要加急(Y/N)：')

#计算 判断输入重量M是否合理 是否加急的变量是否正确
while M or Fast:
    if 0<M<=1000:
        if Fast=='Y':
            Cost=17
            print(f'您的邮费为{Cost}元')
            break
        elif Fast=='N':
            Cost=12
            print(f'您的邮费为{Cost}元')
            break
        else:
            Fast=input('请重新输入是否需要加急(Y/N)：')
    elif M>1000:
        if Fast=='Y':
            Cost=17+4*(math.ceil((M-1000)/500))
            print(f'您的邮费为{Cost}元')
            break
        elif Fast=='N':
            Cost=12+4*(math.ceil((M-1000)/500))
            print(f'您的邮费为{Cost}元')
            break
        else:
            Fast=input('请重新输入是否需要加急(Y/N)：')
    else:
        M=int(input('请重新输入正确的邮件重量：'))
