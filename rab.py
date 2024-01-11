d= {0:'e', 1:'n', 2:'w', 3:'s'}
l=[1,2,3,4]
def rab(n):
    for i, y in n.items():
        print(i, y, end=' ')


def rab(n):
    for i, in n:
        print(i, end=' ')
rab(d)