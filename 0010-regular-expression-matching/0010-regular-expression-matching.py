class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # memo = {}
        # def dfs(i, j):
        #     if (i, j) in memo:
        #         return memo[(i, j)]
        #     # both string and pattern finished
        #     if i >= len(s) and j >= len(p):
        #         return True

        #     # pattern finished but string not finished
        #     if j >= len(p):
        #         return False

        #     # check current character match
        #     match = i < len(s) and (s[i] == p[j] or p[j] == '.')

        #     # handle '*'
        #     if j + 1 < len(p) and p[j + 1] == '*':
        #         # 1) skip x*   OR   2) use x* (if match)
        #         ans = dfs(i, j + 2) or (match and dfs(i + 1, j))
        #     else:
        #         # no '*', must match current char
        #         ans = match and dfs(i + 1, j + 1)

        #     memo[(i, j)] = ans
        #     return ans

        # return dfs(0, 0)
        memo = {}

        def dfs(i, j):
            # Check if result is memoized
            if (i, j) in memo:
                return memo[(i, j)]

            # If both string and pattern are finished
            if i == len(s) and j == len(p):
                return True

            # If pattern finished but string not
            if j == len(p):
                return False

            # Check if current characters match
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            # Handle '*' operator
            if j + 1 < len(p) and p[j + 1] == '*':
                # Try zero occurrence or one/more occurrences if first_match
                memo[(i, j)] = (dfs(i, j + 2) or
                                (first_match and dfs(i + 1, j)))
                return memo[(i, j)]
            else:
                # Move both pointers if current characters match
                if first_match:
                    memo[(i, j)] = dfs(i + 1, j + 1)
                    return memo[(i, j)]
                else:
                    memo[(i, j)] = False
                    return False

        return dfs(0, 0)
