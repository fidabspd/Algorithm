stock = 4
dates = [4,10,15]
supplies = [20,5,10]
k = 30
# result 2


### 알고리즘 잘못 이해
def solution1(stock, dates, supplies, k):
    answer = 0
    for i in range(len(dates)):
        if i == len(dates) - 1:
            if stock - dates[i] < k - dates[i]:
                stock += supplies[i]
                answer += 1
                # print(i + 1)
        else:
            if stock - dates[i] < dates[i + 1] - dates[i]:
                stock += supplies[i]
                answer += 1
                # print(i + 1)
        if i == 0:
            stock -= dates[i]
        else:
            stock -= (dates[i] - dates[i - 1])
        # print(stock, '\n')
    
    return answer

print(solution1(stock, dates, supplies, k))



### 틀림
def solution(stock, dates, supplies, k):
    import heapq
    stock = -stock
    k = -k
    answer = 0
    supplies = list(map(lambda x: x * -1, supplies))
    heapq.heapify(supplies)
    # print('\n\n', stock)
    for i in range(len(supplies)):
        answer += 1
        m = heapq.heappop(supplies)
        stock += m
        # print(stock)
        if stock < k:
            break
    return answer

print(solution(stock, dates, supplies, k))