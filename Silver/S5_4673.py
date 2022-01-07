# -*- coding: utf-8 -*-
"""
 * 문제를 푼 과정 :
 - 각 숫자마다 DFS로 풀어야하기 때문에 DFS 형식으로 문제를 풀었다.
 - 처음에 자릿수 구하는 것을 10으로 나누는게 아니라, 리스트로 접근하니 시간 초과가 났다.
 - 생성자가 반복된다는 점에서 생성자를 담는 자료구조를 list 대신 set을 사용했다.

 * 새로 알게된 것 :
 - 각 자릿수마다 DFS 돌리는 문제가 나오면 10으로 나누는 자릿수 기억하기, 파이썬에서 /와 //은 다르다.(한번 더 기억하기)
"""

def creater(num):
    add = num
    while num != 0:
        add += num % 10
        num = num // 10
    return add

a = [_ for _ in range(1, 10001)]
result = set()

for i in a:
    while creater(i) <= 10000:
        tmp = creater(i)
        result.add(tmp)
        i = tmp

for i in a:
    if i not in result:
        print(i)
