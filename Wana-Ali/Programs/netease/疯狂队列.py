# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

n = int(raw_input())
numbers = list(map(int,raw_input().strip().split()))
numbers.sort()
if n < 2 :
    print '0'
else:
    numbers.append(0)
    cache = []
    value = 0
    times = n / 2
    head , end = 0 , n
    for i in range(times+1):
        if i % 2 == 0 :
            cache.append(numbers[end])
            cache.append(numbers[end-1])
            end -= 2
        else:
            cache.append(numbers[head])
            cache.append(numbers[head+1])
            head += 2
    cache.pop(0)
    if n == 2 :
        value = cache[0] - cache[1]
    else:
        value = cache[0] *2 - cache[1] - cache[2]
        for j in range(1,n):
            if j < n-2:
                value += abs(cache[j] - cache[j + 2])
        print ''.join(str(value))

