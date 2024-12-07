string='话说天下大势，分久必合，合久必分。周末七国分争，并入于秦。及秦灭之后，楚、汉分争，又并入于汉。汉朝自高祖斩白蛇而起义，一统天下，后来光武中兴，传至献帝，遂分为三国。推其致乱之由，殆始于桓、灵二帝。'
#此段话的长度（包含标点符号）
print(f'文本的长度为{len(string)}个字符(包含标点符号)')

#判断"云长"这个词是否出现在段落中
x=string.find('云长')
if x>=0:
    print(f'云长出现在段落中，在{x}位置')
else:
    print('云长不在段落中')

#统计“汉”这个字出现的次数
print(f'汉在文本中出现了{string.count('汉')}次')

#统计“汉”这个字第一次出现的位置
print(f'汉在文本中第一次出现的位置是{string.find('汉')}')