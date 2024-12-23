class User:
    ID=None
    realname=None
    telephone=None
    address=None
    def printf(self):
        print(f'天猫账号:{self.ID}\n姓名:{self.realname}\n电话:{self.telephone}\n地址:{self.address}')

user1=User()
user1.ID='zmjjkk'
user1.realname='郑永康'
user1.telephone='1008611'
user1.address='上海市静安区灵石路695号珠江创意中心一号楼e101室'
user1.printf()