import time
def printf(output,str,acsiii):
    if acsiii!=ord(str) and acsiii!=10:
        print(output+chr(acsiii))
        return printf(output,str,acsiii+1)
    output+=str
    return str

if __name__ == '__main__':
    output=''
    needoutput='Hello world!And I like Python!'
    for str in (needoutput):
        output+=printf(output,str,32)
        time.sleep(0.5)
    print(output)