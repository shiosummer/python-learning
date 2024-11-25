data='library.txt'
buy_list={'item':[],'total_price':0}
def load_data():
    library=[]
    with open(data,'r',encoding='utf-8') as f:
        for line in f:
            num,name,price,stock=line.strip().split('-')
            library.append({'num':num,'name':name,'price':price,'stock':stock})
        return library
load_data()
def eadit_data():
