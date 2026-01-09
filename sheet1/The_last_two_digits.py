A,B,C,D = map(int,input().split())
r = (A % 100) * (B % 100)
r %= 100
re = (C % 100) * (D % 100)
re %= 100
ans = r * re
ans%= 100
print("{:02d}".format(ans))