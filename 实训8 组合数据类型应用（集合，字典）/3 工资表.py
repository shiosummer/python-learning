Paylist=[10000,5200,4700,3860,1200,8500]
print(Paylist)#创建一个月薪数据列表并输出
Paylist.insert(2,4500)
Paylist.pop(5)
for i in Paylist:
    if i<5000:
        n=Paylist.index(i)
        Paylist[n]=5000
        print(f'索引{n}的员工月薪小于5000')
print(Paylist)
data={"a1":['王保华',10000],
      "a2":['李伟新',5200],
      "a3":['张强',4700],
      "a4":['张明',3860],
      "a5":['陈鑫',1200],
      "a6":['李牧',8500]}
print(data)
data["a7"]=['李梅',9000]
data["a4"]=['张明',4900]
data.pop("a4")
for key in data:
    print(data[key])