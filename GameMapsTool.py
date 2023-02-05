import random


mapList = ['绿地', '风暴','未开发岩石区','北极圈','失落之城']
while True:
    num = input('输入赛制：(如BO3,BO5)')#可以重复输入，输入.stop停止(注意stop前有英文句号)
    ln = len(num)
    if ln == 3:
        num = int(num[2])
    elif ln == 4:
        num = int(num[2]+num[3])
    elif ln > 4 and 'BO' in num:
        print('暂不支持>BO99')
    else:
        break
    i = 1
    while i <= num:
        res = random.choice(mapList)
        if num <= 5:
            mapList.remove(res)
        print(i, res)
        i += 1
        random.shuffle(mapList)
    if num == '.stop':
        break
