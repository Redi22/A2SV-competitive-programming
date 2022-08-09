class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        dp = {num: 1 for num in arr}
        mod = 10 ** 9 + 7
        
        for i in range(len(arr)):
            for j in range(i):
                if arr[i] % arr[j] == 0  and arr[i] // arr[j] in dp:
                    dp[arr[i]] += dp[arr[j]] * dp[arr[i] // arr[j]]
                    
        return sum(dp.values()) % mod