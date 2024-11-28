import random
chars_list=[]
for i in range(6):
    tpye=random.randint(0,2)
    if tpye == 0:
        chars_list.append(random.randrange(0,9))
    elif tpye == 1:
        chars_list.append(chr(random.randrange(65,90)))
    else:
        chars_list.append(chr(random.randrange(97,122)))

str1 = ''
for el in chars_list:
    str1 += str(el)
print(str1)