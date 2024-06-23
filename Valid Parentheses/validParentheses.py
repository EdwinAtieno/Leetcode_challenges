class Solution(object):
    def isValid(self, s: str) -> bool:
        stack = []  # only use append and pop
        pairs = {"(": ")", "{": "}", "[": "]"}
        for bracket in s:
            if bracket in pairs:
                print(bracket)
                stack.append(bracket)
            elif len(stack) == 0 or bracket != pairs[stack.pop()]:
                return False

        return len(stack) == 0


s = Solution()
print(s.isValid(")"))
