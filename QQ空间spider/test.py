while True:
    s = input("Please Input the Name('q' for Exit):\n")
    if s == 'q':
        break
    if len(s) == 2:
        s1 = list(s)
        s1[1] = "*"
        s1 = str(s1)
        print(s1)
    elif len(s) > 2:
        s1 = list(s)
        s1[0] = "*"
        s1 = str(s1)
        print(s1)
        print(str(s1))
    else:
        print("输入错误！")

        # 如果s为2字符，则ss为“*”加后面的字符
        # 否则ss为取首字符，加“*”，再加后面的字符
        # 使用2.7版的考生可将中文注释删掉后调试
