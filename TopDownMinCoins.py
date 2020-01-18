import sys
d={}
def mincoins(l,v):
    if d.get(v,-1)!=-1:
        return d[v]
    if v==0:
        r=0
    else:
        r=sys.maxsize
        for x in l:
            if x<=v:
                r=min(r,1+mincoins(l,v-x))
    d[v]=r
    return r

if __name__=='__main__':
    v=int(input())
    l=eval(input())
    import timeit
    start=timeit.default_timer()
    print(mincoins(l,v))
    end=timeit.default_timer()
    print("Time:",end-start)