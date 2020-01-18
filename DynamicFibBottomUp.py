'''dymanic  bottom up approach to find fibanocci series'''
d={}    #table to memorize the newly computed values
d[0]=0  #storing new value in table
d[1]=1  #storing new in table
#lookups in dictionary are very fast

def bufib(n):   #bottom up approach
    for i in range(2,n+1):
        r=d[i-1]+d[i-2]  #d[i-1] and d[i-2] means looking the values in table
        d[i]=r
    ret=d[n]
    print(d)
    return ret

if __name__=='__main__':
    import timeit
    n=int(input())
    start=timeit.default_timer()
    print(bufib(n))
    end=timeit.default_timer()
    print("Time taken in seconds is:",end-start)