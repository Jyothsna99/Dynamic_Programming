# A recursive Python implementation of LCS problem
def lcs(X, Y, m, n): 
    if m == 0 or n == 0: 
        return 0 
    elif X[m-1] == Y[n-1]: 
        return 1 + lcs(X, Y, m-1, n-1) 
    else: 
        return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n)) 


if __name__=='__main__':
    X =input()
    Y =input() 
    print("Length of Least common subsequence is ", lcs(X , Y, len(X), len(Y)))
