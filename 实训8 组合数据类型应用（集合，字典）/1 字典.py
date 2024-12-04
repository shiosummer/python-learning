str = 'skdaskerkjsalkj'
cont={}
for i in str:
    if i in cont:
        cont[i]+=1
    else:
        cont[i]=1
print(cont)