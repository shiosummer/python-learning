#引入字符串
zfc = '000itcast and itheima000'
#查找'it'出现的索引位置，并打印输出
found = zfc.find('it')
found1 = zfc.find('it',found+1)
found2=str(found)
while found1 > int(found):
    found2=str(found2)+','+str(found1)
    found=found1
    found1=zfc.find('it',found1+1)
    print(found2)
#检测'it'出现的次数
print(zfc.count('it'))
#把'000'替换为空格
replacing=zfc.replace('000',' ')
print(replacing)
#把所有字母转换为大写形式
uppering=replacing.upper()
print(uppering)
#删除字符串头尾的空格
striping=uppering.strip()
print(striping)