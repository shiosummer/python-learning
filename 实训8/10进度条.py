import time
x=50
print('-'*25+'开始下载'+'-'*25)
for i in range(51):
    str1 = '*'*i
    str2 = '.'*(x-i)
    str3 = int((i/x)*100)
    print(f'\r{str3}% [{str1}{str2}]',end='')
    time.sleep(0.1)
print('\n'+'-'*25+'下载完成'+'-'*25)