class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        def split_array(n, m, n2, m2):
            temp = []

            if n > n2 or m > m2:
                return temp

            up = []
            lower = []
            left = []
            right = []

            for i in range(m, m2 + 1):
                up.append(matrix[n][i])

            if n2 != n:
                for i in range(m, m2 + 1):
                    lower.append(matrix[n2][i])
                    
            for i in range(n, n2 + 1):
                    right.append(matrix[i][m2])

            if m != m2:
                for i in range(n, n2 + 1):
                    left.append(matrix[i][m])

                left = left[1:-1]

                

            right = right[1:-1]

            temp += (up + right + lower[::-1] + left[::-1])

            return temp + split_array(n+1, m+1, n2 - 1, m2 - 1)

        return split_array(0, 0, len(matrix) - 1, len(matrix[0]) - 1)
