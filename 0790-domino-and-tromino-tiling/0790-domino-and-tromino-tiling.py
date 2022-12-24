class Solution:
    def numTilings(self, n: int) -> int:

        if n <= 1:
            return 1
        if n == 2:
            return 2

        thr = 1
        two = 1
        one = 2
        add = 2*thr
        while n > 3:
            nxt = one + two + add # 2 + 1 + 2 = 5
            thr = two # 1
            two = one # 2
            one = nxt # 5
            add += 2*thr
            n -= 1

        return (one + two + add) % (10**9 + 7)
