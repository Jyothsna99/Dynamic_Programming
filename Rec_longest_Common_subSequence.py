# A recursive Python implementation of LCS problem
'''The Longest Common Subsequence. A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. Longest common subsequence (LCS) of 2 sequences is a subsequence, with maximal length, which is common to both the sequences.'''
'''   “ABCDGH” and “AEDFHR” is “ADH” of length 3.    '''
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
