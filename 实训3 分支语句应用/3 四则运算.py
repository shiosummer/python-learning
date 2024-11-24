#输入数字1，数字2和运算符
num1 = float(input('请输入第一个数：'))
num2 = float(input('请输入第二个数：'))
calculate = input('请输入运算符号(+ - * /)：')

#判断进行什么运算以及进行运算输出
while calculate:
    if calculate=='+':
        print(num1+num2)
        break
    elif calculate=='-':
        print(num1-num2)
        break
    elif calculate=='*':
        print(num1*num2)
        break
    elif calculate=='/':
        print(num1/num2)
        break
    else:
        calculate = input('请重新输入正确的运算符号(+ - * /)：')
