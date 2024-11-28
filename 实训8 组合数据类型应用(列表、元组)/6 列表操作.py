demo1_list=[1,2,'Python',[3,4,'d',0],5]
print(f'列表:>>>{demo1_list}')
demo1_list.append('Java')
print(f"追加元素'Java':>>>{demo1_list}")
demo1_list[demo1_list.index([3,4,'d',0])]= 34
print(f"查找[3,4,'d',0],并将其改为34:>>>{demo1_list}")
demo2_list=demo1_list[::-1]
print(f"将列表进行逆置:>>>{demo2_list}")
demo2_list.pop()
print(f'删除最后一个元素:>>>{demo2_list}')
demo2_list.remove('Python')
print(f"删除元素'python':>>>{demo2_list}")