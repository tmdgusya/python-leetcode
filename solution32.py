import unittest

class Solution(unittest.TestCase):

    def longestValidParentheses(self, s: str) -> int:
        max_len = 0

        # brute-force solution
        for i in range(0, len(s)):
            for j in range(i + 2, len(s) + 1, 2):
                if self.isValid(s[i:j]):
                    max_len = max(max_len, j - i)
        return max_len

    # leet code solution
    def longestValidParentheses2(self, s:str) -> int:
        left = 0
        right = 0
        max_len = 0

        for c in s:
            if c == "(":
                left += 1
            else:
                right += 1
            if left == right:
                max_len = max(max_len, 2 * right)
            elif right >= left:
                left = 0
                right = 0

        left = 0
        right = 0

        for i in range(len(s) - 1, 0, -1):
            if s[i] == "(":
                left += 1
            else:
                right += 1

            if left == right:
                max_len = max(max_len, 2 * left)
            elif left >= right:
                left = 0
                right = 0

        return max_len

    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(":
                stack.append(c)
            elif stack and c == ")":
                stack.pop()
            else:
                return False

        return len(stack) == 0

    def doTest(self):

        self.assertEqual(self.longestValidParentheses2("(()"), 2)
        self.assertEqual(self.longestValidParentheses2(")()())"), 4)
        self.assertEqual(self.longestValidParentheses2("()(()"), 2)
