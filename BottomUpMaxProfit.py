'''p contains the profits of cutting the rod in inches i.e.,1 inch-p[0],2inch-p[1],3 inch-p[2]
    length of the rod is n,we need to cut the rod in inches so that we get the maximum profit'''
#Bottom Up approach
d={0:0}
def mp(p,n):
    for j in range(1,n+1):
        r=-999999999
        for i in range(1,len(p)+1):
            if j>=i:
                r=max(r,p[i-1]+d[j-i])
        d[j]=r
    return d[n]

if __name__=='__main__':
    n=int(input())#Number of rods 
    p=eval(input())#list containing the profits of each rod
    import timeit
    start=timeit.default_timer()
    print(mp(p,n))
    end=timeit.default_timer()
    print("Time:",end-start)