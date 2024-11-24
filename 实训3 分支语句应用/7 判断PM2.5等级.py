#引入24小时内PM2.5的平均值
PM25 = float(input('请输入24小时内PM2.5的平均值：'))

#判断空气质量等级及输入的PM2.5的值是否正确
while PM25:
        if 0<PM25<=50:
            print('24小时内空气质量等级为“优”')
            break
        elif 50<PM25<=100:
            print('24小时内空气质量等级为“良好”')
            break
        elif 100<PM25<=150:
            print('24小时内空气质量等级为“轻度污染”')
            break
        elif 150<PM25<=200:
            print('24小时内空气质量等级为“中度污染”')
            break
        elif 200<PM25<=300:
            print('24小时内空气质量等级为“重度污染”')
            break
        elif PM25>300:
            print('24小时内空气质量等级为“严重污染”')
            break
        else:
            PM25 = float(input('请重新输入正确的PM2.5平均值：'))
