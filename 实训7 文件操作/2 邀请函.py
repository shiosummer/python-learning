def writefile():
    with open('邀请函.txt','w',encoding='utf-8') as f:
        f.write('诚挚邀请您来参加本次宴会\n')
        return
def addcontent():
    with open('邀请函.txt','a',encoding='utf-8') as f:
        f.write('best regards\n郑蔚楠')
        return
def creatfile(name):
    with open('邀请函.txt','r',encoding='utf-8') as f:
        s=f.read()
    with open(f'{name}.txt','w',encoding='utf-8') as f:
        f.write(f'{name}:\n{s}')
        return
def readfile(filename):
    with open(filename,'r',encoding='utf-8') as f:
        return f.read()

if __name__ == '__main__':
    writefile()
    addcontent()
    creatfile('丁一')
    creatfile('王美丽')
    creatfile('韩梅梅')
    print(readfile('邀请函.txt'))
    print(readfile('丁一.txt'))
    print(readfile('王美丽.txt'))
    print(readfile('韩梅梅.txt'))