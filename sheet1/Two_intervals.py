l1,r1,l2,r2 = map(int,input().split())
St = max(l1,l2)         #St = start
end = min(r1,r2)
if St > end:
    print("-1")
else:
    print(St,end)