def wordBk(s, wDict):
    wSet = set(wDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True  
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wSet:
                dp[i] = True
                break
    return dp[len(s)]

s = "leetcode"
wDict = ["leet", "code"]
print(wordBk(s, wDict))  