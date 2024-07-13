def min_distance(s1, s2):
    m = len(s1)
    n = len(s2)
    
    # Create a DP table to store the results of subproblems
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize the DP table
    for i in range(m + 1):
        dp[i][0] = i  # If s2 is empty, remove all characters from s1
    for j in range(n + 1):
        dp[0][j] = j  # If s1 is empty, insert all characters of s2
    
    # Compute the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # If the characters are the same, no operation needed
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],    # Deletion
                                   dp[i][j - 1],    # Insertion
                                   dp[i - 1][j - 1])  # Substitution
    
    # The value at dp[m][n] is the minimum number of operations required
    return dp[m][n]

# Test case
s1 = "kitten"
s2 = "sitting"
print(f"Minimum conversions to transform '{s1}' to '{s2}' is {min_distance(s1, s2)}")
