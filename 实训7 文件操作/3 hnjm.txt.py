with open('hnjm.txt','w',encoding='utf-8') as f:
    f.write('你好，欢迎来到河南经贸职业学院')
with open ('hnjm.txt','r+',encoding='utf-8') as f:
    s=f.read()
    f.seek(s.find('河南经贸'))
    print(f.tell())
