#Implementation of Finding Length of Longest Common Substring 
def LCSubStr(X, Y, m, n): 
	# Create a table to store lengths of 
	# longest common suffixes of substrings. 
	# LCS is the table with zero value initially in each cell 
	LCS = [[0 for k in range(n+1)] for l in range(m+1)] 
	result = 0
	for i in range(m + 1): 
		for j in range(n + 1): 
			if (i == 0 or j == 0): 
				LCS[i][j] = 0
			elif (X[i-1] == Y[j-1]): 
				LCS[i][j] = LCS[i-1][j-1] + 1
				result = max(result, LCS[i][j]) 
			else: 
				LCS[i][j] = 0
	return result 

if __name__=='__main__': 
    X = input()
    Y = input()
    m = len(X) 
    n = len(Y) 
    print('Length of Longest Common Substring is', 
					LCSubStr(X, Y, m, n)) 

