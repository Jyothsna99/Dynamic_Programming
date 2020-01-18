td={}    #table to memorize the newly computed values
td[0]=0  #storing new value in table
td[1]=1  #storing new in table
def tdfib(n):
    if td.get(n,-1)!=-1:#intially checking table contains this value or not
        return td[n]
    else:   #if not present computing the value
        td[n]=tdfib(n-1)+tdfib(n-2)
        return td[n]

if __name__=='__main__':
    '''this code is used to calculate time taken by the tdfib() function'''
    import timeit
    n=int(input())
    start=timeit.default_timer()
    print(tdfib(n))
    end=timeit.default_timer()
    print("Time taken in seconds is:",end-start)
    

        