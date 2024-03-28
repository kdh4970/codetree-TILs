# 무빙워크 판의 개수 N, 안정성이 0인 판의 개수가 K일 떄 실험 종료
# 종료 조건 : 안정성이 0인 판이 K개
# 
import itertools

N, K = list(map(int,input().split()))
moving_walk = list(map(int,input().split()))


# def simul():
#     cnt = 0
#     person = []
#     while True:
#         #1
#         cnt += 1
#         # person += 1
#         #2
#         if person:
#             for _ in range(len(person)):
#                 if person[_+1] or moving_walk[person[_]-cnt]

#         #3

#         #4
#         if moving_walk.count(0) == K:
#             return cnt

# print(simul())