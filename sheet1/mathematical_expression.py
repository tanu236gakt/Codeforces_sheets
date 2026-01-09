A,S,B,Q,C = input().split()
A = int(A)
B = int(B)
C = int(C)
if S == '+':
    print("Yes" if A+B == C else A + B)
elif S == '*':
    print("Yes" if A*B == C else A * B)
elif S == '-':
    print("Yes" if A-B == C else A - B)
 