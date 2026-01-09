import math
A,B,C,D = map(int,input().split())
ans = B * math.log(A,)
ans2 = D * math.log(C)
if ans>ans2:
    print("YES")
else:
    print("NO")