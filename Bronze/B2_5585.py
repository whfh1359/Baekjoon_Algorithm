# -*- coding: utf-8 -*-
"""
 * 문제를 푼 과정 :
 - 큰 돈부터 순회를 해야하기 때문에 배열로 구현했다.
 - 거스름돈은 모두 걸러주게 되어있으므로 거슬러지지 않을 경우는 구현하지 않았다.

 * 새로 알게된 것 :
 - 배열로 구현하면 직접 각 거스름돈을 나눌 필요가 없이 반복문을 사용하게 되어 편리하다
"""
def solution(n):
    money = [500, 100, 50, 10, 5, 1]
    count = 0
    for i in money:
        while n >= i:
            n -= i
            count += 1
    return count

n = int(input())
print(solution(1000-n))