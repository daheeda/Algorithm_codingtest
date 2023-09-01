n,m = map(int,input().split()) # 남은기간, 챕터수
book = [list(map(int,input().split())) for _ in range(m)] # 일수, 페이지
limit = sum(row[0] for row in book)
if limit < m : m = limit
dp = [[0]*(n+1) for _ in range(m+1)] # 기간, 챕터

for day in range(1,n+1):
    for chapter in range(1,m+1):
        iday = book[chapter-1][0]
        page = book[chapter-1][1]
        
        if iday > day :
            dp[chapter][day] = dp[chapter-1][day]
        else :
            dp[chapter][day] = max(dp[chapter-1][day], dp[chapter-1][day-iday]+page)
        
print(dp[m][n])
