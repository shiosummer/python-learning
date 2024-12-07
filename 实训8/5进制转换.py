num = int(input('请输入需要转换的十进制数字'))
jinzhi = int(input('请输入需要转换的进制(数字)：'))
while jinzhi:
    if jinzhi == 2:
        print(bin(num))
        break
    elif jinzhi == 8:
        print(oct(num))
        break
    elif jinzhi == 16:
        print(hex(num))
        break
    else:
        jinzhi = int(input('请重新输入需要转换的进制(数字)：'))