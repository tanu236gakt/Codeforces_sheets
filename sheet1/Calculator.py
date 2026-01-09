exp = input()
if ('+' in exp):
    A,B=map(int,exp.split('+'))
    ans=A+B
elif ('-' in exp):
    A,B=map(int,exp.split('-'))
    ans=A-B
if ('*' in exp):
    A,B=map(int,exp.split('*'))
    ans=A*B
if ('/' in exp):
    A,B=map(int,exp.split('/'))
    ans=A//B
print(ans)
    