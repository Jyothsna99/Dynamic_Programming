'''Given n different coins with n different denominations,we need to choose minimim number of coins that sums the given value'''
#Recursive solution
import sys
def mincoins(l,v):
    if v==0:
        return 0
    else:
        r=sys.maxsize
        for x in l:
            if x<=v:
                r=min(r,1+mincoins(l,v-x))
        return r
"""def mc(l,v):
    if v==0:
        return 0
    else:
        return min([1+mc(l,v-i) for i in l if i<v])"""

if __name__=='__main__':
    v=int(input())
    #l=[int(x) for x in input().split()]
    l=eval(input())
    import timeit
    start=timeit.default_timer()
    print(mincoins(l,v))
    end=timeit.default_timer()
    print("Time:",end-start)
    
    