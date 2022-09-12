import unittest

class Solution(unittest.TestCase):
    def isValid(self, s: str) -> bool:
        queue = list(s)
        failed_stack: list[str] = []
        while queue:
            if len(failed_stack) == 0:
                failed_stack.append(queue.pop(0))
                continue

            cur_parenthese = queue.pop(0)
            prev_parenthese = failed_stack.pop()
            if self.isCorrectWord(prev_parenthese, cur_parenthese):
                continue
            else:
                failed_stack.append(prev_parenthese)
                failed_stack.append(cur_parenthese)


        return len(failed_stack) == 0
    
    # more optimize
    def isValid2(self, s: str) -> bool:
        bracket_map = {"(" : ")", "[" : "]", "{" : "}"}
        open_par = set(["(", "[", "{"])
        stack = []
        for i in s:
            if i in open_par:
                stack.append(i)
            elif stack and i == bracket_map[stack[-1]]:
                stack.pop()
            else:
                return False
        return len(stack) == 0

    def isCorrectWord(self, target: str, curr: str) -> bool:
        if target == '(' and curr == ')':
                return True
        if target == '{' and curr == '}':
                return True
        if target == '[' and curr == ']':
                return True
        return False


    #boilerplate code
    def doTest(self):
        self.assertTrue(self.isValid2('()'))
        self.assertFalse(self.isValid2(')()('))
        self.assertFalse(self.isValid2('({[)}]'))
        self.assertTrue(self.isValid2('([])'))

if __name__ == '__main__':
    unittest.main()
