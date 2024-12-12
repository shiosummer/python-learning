with open('hnjm.txt','w',encoding='utf-8') as f:
    f.write('你好，欢迎来到河南经贸职业学院')
with open('hnjm.txt', 'r+', encoding='utf-8') as f:
    s1 = f.read()
    index = s1.find('河南经贸')
    s2 = s1[:index] + '我爱' + s1[index:]
    s2 = s2.replace('职业', '')
    f.seek(0)
    f.write(s2)