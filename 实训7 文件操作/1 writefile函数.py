def writefile(s):
    with open('ZhengWeinan.txt','w',encoding='utf-8')as f:
        f.write(s)
        return
def readfile():
    with open('ZhengWeinan.txt','r',encoding='utf-8') as f:
        return f.read()

if __name__=='__main__':
    s = "我爱经贸,\n我爱python"
    writefile(s)
    print(readfile())