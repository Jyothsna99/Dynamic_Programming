import sys
bu={0:0}
def mincoins(l,v):
    for i in range(1,v+1):
        bu[i]=sys.maxsize
    for value in range(1,v+1):
        for x in l:
            if x<=value:
                s=bu[value-x]
                if s+1<bu[value]:
                    bu[value]=s+1
    print(bu)
    return bu[v]

if __name__=='__main__':
    v=int(input())
    l=eval(input())
    import timeit
    start=timeit.default_timer()
    print(mincoins(l,v))
    end=timeit.default_timer()
    print("Time:",end-start)