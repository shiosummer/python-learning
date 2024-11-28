from module import load_dishes,save_dishes,add_dishes,edit_price,view_menu,order_menu,cancel_order,check_order,check_pay,load_main_menu,exit_system,usr_password

def main():
 load_main_menu()#加载主菜单(假进度条)
 menu_tpye=usr_password()#判断进入的是管理员面板还是顾客面板
 #进入管理员界面
 while menu_tpye == 1:
   choice = input('\n管理员界面：\n1.添加菜品\n2.修改菜品单价/库存\n3.查看菜单\n4.退出系统\n请选择功能:')
   if choice == '1':#添加菜单菜品功能
    add_dishes(name = input('请输入添加的菜品名称:'),price = input('请输入菜品定价:'),stock = input('请输入菜品库存:'))
   elif choice == '2':#修改菜品定价/库存功能
    edit_price(name = input('请输入需要修改定价/库存的菜品:'), price = input('请输入修改后的菜品定价:'), stock = input('请输入修改后的菜品库存:'))
   elif choice == '3':#查看菜单
    view_menu()
   elif choice == '4':#退出系统
    exit_system()
  #进入顾客界面
 while menu_tpye==0:
  choice = input('\n顾客界面：\n1.查看菜单\n2.创建订单\n3.查看订单\n4.取消点餐\n5.结账\n6.退出系统\n请选择功能:')
  if choice == '1':#查看菜单功能
   view_menu()
  elif choice == '2':#进入点菜功能
   order_menu(name = input('请输入您要点的菜品:'),quantity = int(input('请输入您所点菜品的数量:')))
  elif choice == '3':#查看已点菜品
   check_order()
  elif choice == '4':#取消点餐功能
   cancel_order(name = input('请输入您要取消的菜品:'),cancel_quantity=int(input('请输入您要取消的数量:')))
  elif choice == '5':#模拟支付
   check_pay()
  elif choice == '6':#退出系统
   exit_system()

#运行点餐系统
if __name__ == '__main__':
 main()