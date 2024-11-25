import random
chars_list=[]
for i in range(6):
    chars_list.append(random.randint(0,9))

num=''
for el in chars_list:
    num += str(el)
print(num)