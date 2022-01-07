# -*- coding: utf-8 -*-
"""
 * 문제를 푼 과정 :
 - 해당 전자레인지 버튼을 누를 때마다 각각의 버튼 수를 저장해야 하므로 해쉬로 구현했다.
 -
 * 새로 알게된 것 :
 - 처음에 10으로 나눠떨어지지 않았을 때 바로 -1을 리턴하게 했는데, 수행시간이 더 길어졌다.
 - 마지막에 if-else로 구현하였더니 시간이 더 줄어드는 것을 알 수 있었다.
"""

n = int(input())
time = [300, 60, 10]
count = {}

for i in time:
    count[i] = 0
    while n>= i:
        n -= i
        count[i] += 1
if n % 10 != 0:
    print(-1)
else:
    for i in count.values():
        print(i, end = ' ')

