import random



#注意：程序运行后会覆盖同级目录下的1.txt，如果你在同级目录下拥有1.txt或上一次运行后1.txt有内容，请在运行前保存好！
f = open('1.txt','w')
f.close()
tlst = input('输入全部参赛舰队名称，舰队数量需为偶数，舰队名称之间用英文逗号分隔').split(',')
if len(tlst) % 2 == 0:
    tnum = len(tlst)
    group = int(tnum / 2)
    Gnum = range(1, int(group / 2 + 1))
    battletable = {}
    def group(G):
        global tlst, Gtmp, battletable
        for i in Gnum:
            tmp1 = []
            a = random.choice(tlst)
            tlst.remove(a)
            tmp1.append(a)
            b = random.choice(tlst)
            tlst.remove(b)
            tmp1.append(b)
            Gtmp = G + str(i)
            battletable[Gtmp] = tmp1
    group(G='A')
    group(G='B')
    f = open('1.txt', 'a')
    for y in battletable:
        tmp3 = str(y + ': ' + battletable[y][0] + '  VS  ' + battletable[y][1] + '\n')
        tmp4 = y + ': ' + battletable[y][0] + '  VS  ' + battletable[y][1]
        print(tmp4)
        f.write(tmp3)
    f.close()
else:
    print('舰队数量不是偶数，请重启程序后重新输入，否则可能导致出错')