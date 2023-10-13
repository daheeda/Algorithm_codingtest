n = int(input())
m = int(input())
stu = list(map(int, input().split()))
# 학생들이 추천을 시작하기 전에 모든 사진틀은 비어있다.
pic = [0] * n 
piccnt = [0] * n
days = [0] * n
cnt = [0] * (101)

for st in stu :
    days = [ x+1 if x > 0 else x for x in days]
    cnt[st] += 1
    # 현재 사진이 게시된 학생이 다른 학생의 추천을 받은 경우에는 추천받은 횟수만 증가시킨다.
    if pic.count(st) > 0 :
        idx = pic.index(st)
        piccnt[idx] = cnt[st]
    # 어떤 학생이 특정 학생을 추천하면, 추천받은 학생의 사진이 반드시 사진틀에 게시되어야 한다.
    elif pic.count(0) > 0:
        idx = pic.index(0)
        pic[idx] = st
        piccnt[idx] = cnt[st]
        days[idx] = 1
    # 비어있는 사진틀이 없는 경우에는 
    # 현재까지 추천 받은 횟수가 가장 적은 학생의 사진을 삭제하고, 
    # 그 자리에 새롭게 추천받은 학생의 사진을 게시한다. 
    # 이때, 현재까지 추천 받은 횟수가 가장 적은 학생이 두 명 이상일 경우에는 
    # 그러한 학생들 중 게시된 지 가장 오래된 사진을 삭제한다.
    else :
        min_cur = min(piccnt)
        idxlist = []
        for i in range(len(piccnt)):
            if min_cur == piccnt[i] : idxlist.append(i)
        cur = 0
        idx = 0
        for i in idxlist :
            if days[i] > cur : 
                cur = days[i]
                idx = i
        # 사진틀에 게시된 사진이 삭제되는 경우에는 해당 학생이 추천받은 횟수는 0으로 바뀐다.
        cnt[pic[idx]] = 0
        pic[idx] = st
        piccnt[idx] = cnt[st]
        days[idx] = 1
        
# 사진틀에 사진이 게재된 최종 후보의 학생 번호를 증가하는 순서대로 출력한다.
pic.sort()
if pic.count(0) == 0 : print(' '.join(map(str,pic)))
else :
    for i in range(pic.count(0)):
        pic.remove(0)
    print(' '.join(map(str,pic)))
