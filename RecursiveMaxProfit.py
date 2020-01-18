def mp(p,n):
    '''p contains the profits of cutting the rod in inches i.e.,1 inch-p[0],2inch-p[1],3 inch-p[2]
    length of the rod is n,we need to cut the rod in inches so that we get the maximum profit'''
    if n==0:
        return n
    else:
        r=-9999999999
        for x in range(0,len(p)):
            if x<=n:
                r=max(r,p[x]+mp(p,n-(x+1)))
        return r

if __name__=='__main__':
    n=int(input())
    p=eval(input())
    import timeit
    start=timeit.default_timer()
    print(mp(p,n))
    end=timeit.default_timer()
    print("Time:",end-start)