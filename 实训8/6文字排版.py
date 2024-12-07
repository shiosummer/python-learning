#输入原始文本并选择处理类型
word = input('请粘贴您需要重新排版的文字\n')
need_tpye = input('请选择您需要处理的类型\nA.删除空格÷\nB.英文标点替换\nC.英文单词大写\n')
while need_tpye:
    #去空格并输出
    if need_tpye == 'A' or need_tpye == 'a':
        print(word.strip())
        break
    #替换英文标点为中文标点并输出
    elif need_tpye == 'B' or need_tpye == 'b':
        ChineseChar = ['，', '！', '。', '：']
        EnglishChar = [',', '!', '.', ':']
        replacing = word
        for i in range(0,len(EnglishChar)):
            replacing = replacing.replace(EnglishChar[i],ChineseChar[i])
        print(replacing)
        break
    #英文单词大写并输出
    elif need_tpye == 'C' or need_tpye == 'c':
        print(word.upper())
        break
    else:
        need_tpye = input('请重新选择你需要处理的类型\nA.删除空格÷\nB.英文标点替换\nC.英文单词大写\n')