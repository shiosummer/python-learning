#引入变量学生成绩m
m = int(input('请输入学生成绩：'))

#判断分支 输出等级
while m:
    if 0<=m<=59:
        print('学生成绩不及格')
        break
    elif 60<=m<=69:
        print('学生成绩及格')
        break
    elif 70<=m<=79:
        print('学生成绩中等')
        break
    elif 80<=m<=89:
        print('学生成绩良好')
        break
    elif 90<=m<=100:
        print('学生成绩优秀')
        break
    else:
        m = int(input('请重新输入正确的学生成绩：'))
