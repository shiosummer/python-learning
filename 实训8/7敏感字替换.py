list_old=['敏感词1','敏感词2','敏感词3']
string=input('请输入需要检测替换敏感词的语句')
for i in list_old:
    string=string.replace(i,'*'*len(i))
print(string)