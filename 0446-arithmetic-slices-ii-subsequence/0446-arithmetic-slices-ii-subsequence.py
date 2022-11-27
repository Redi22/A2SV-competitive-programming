class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        total = 0
        dp = [defaultdict(int) for item in A]
        for i in range(len(A)):
            for j in range(i):
                dp[i][A[i] - A[j]] += 1
                if A[i]-A[j] in dp[j]:
                    dp[i][A[i] - A[j]] += dp[j][A[i]-A[j]]
                    total += dp[j][A[i]-A[j]]
        return total