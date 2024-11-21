def result(num1,num2,operation='+'):
   if operation == '+':
       return num1+num2
   elif operation == '-':
       return num1-num2
   elif operation == '*':
       return num1*num2
   else:
       if num2 != 0:
           return num1/num2

num1 = int(input('请输入第一个数字'))
num2 = int(input('请输入第二个数字'))
operation = input('请输入运算符号(+,-,*,/)')
while operation:
   if operation != '+' and operation != '-' and operation != '*' and operation !='/':
       operation = input('请重新输入运算符号(+,-,*,/)')
   else:
       break
print(result(num1, num2, operation))