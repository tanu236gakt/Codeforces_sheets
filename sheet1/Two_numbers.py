import math 
A,B = map(int,input().split())
def c_round(x):
    return int(x + 0.5) if x >= 0 else int(x - 0.5)
print("floor",A,"/",B,"=",math.floor(A/B))
print("ceil",A,"/",B,"=",math.ceil(A/B))
print("round",A,"/",B,"=",c_round(A/B ))
