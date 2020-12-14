n=int(input())
t=int((n*(n-1))/2)
arr=[]
for i in range(t):
    s=input()
    team1,team2,scores=s.split()
    score1,score2=map(int,scores.split('-'))
    # print(team1,team2,score1,type(score2))
    if score1>score2:
        arr.append([team1,3])
    elif score1<score2:
        arr.append([team2,3])
    else:
        arr.append([team1,1])
        arr.append([team2,1])




# n=int(input())
# noofMatches=int((n*(n-1))/2)
# points=dict()
#
# for i in range(noofMatches):
#     s=input()
#     team1,team2,scores=s.split()
#     score1,score2=scores.split('-')
#     if(score1>score2):
#         try:
#             v=points[team1]
#             points[team1]=v+3
#         except:
#             points[team1]=3
#     elif(score1<score2):
#         try:
#             v=points[team2]
#             points[team2]=v+3
#         except:
#             points[team2]=3
#     else:
#         try:
#             v=points[team1]
#             points[team1]=v+1
#         except:
#             points[team1]=1
#         try:
#             v=points[team2]
#             points[team2]=v+1
#         except:
#             points[team2]=1
#
# teammax = max(points, key=points.get)
# print(teammax)
# print(points[teammax])
