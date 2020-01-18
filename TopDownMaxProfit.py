'''p contains the profits of cutting the rod in inches i.e.,1 inch-p[0],2inch-p[1],3 inch-p[2]
    length of the rod is n,we need to cut the rod in inches so that we get the maximum profit'''
#Top down approach
d={}
def mp(p,n):
    if d.get(n,-1)!=-1:
        return d[n]
    else:
        if n==0:
            r=0
        else:
            r=-9999999999999
            for i in range(0,len(p)):
                if i<=n:
                    r=max(r,p[i]+mp(p,n-(i+1)))
    d[n]=r
    return d[n]

if __name__=='__main__':
    n=int(input())#Number of rods 
    p=eval(input())#list containing the profits of each rod
    import timeit
    start=timeit.default_timer()
    print(mp(p,n))
    end=timeit.default_timer()
    print("Time:",end-start)