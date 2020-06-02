def minStepsTo1DP(n,dp):
    ''' Return Mini35mum no of steps required to reach 1 using using Dynamic Prog'''
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if n == 1: 
        return 0 
    
    if n in dp: 
        return dp[n]
    
    if (n-1) in dp: 
        ans = dp[n-1]
    else: 
        ans = minStepsTo1DP(n-1,dp)
        dp[n-1] = ans
    
    if n % 2 == 0: 
        if (n/2) in dp: 
            ans2 = dp[n/2]
        else: 
            ans2 = minStepsTo1DP(n/2,dp)
            dp[n/2] = ans2
        ans = min(ans,ans2)
    
    if n % 3 == 0: 
        if (n/3) in dp: 
            ans3 = dp[n/3]
        else: 
            ans3 = minStepsTo1DP(n/3,dp)
            dp[n/3] = ans3
        ans = min(ans,ans3)
    
    return 1 + ans 

# Main
n=int(input())
dp = {}
for i in range(2,n):
    print(i,',',minStepsTo1DP(i,dp))
