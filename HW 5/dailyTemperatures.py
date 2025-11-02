class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, j in enumerate(temperatures):
            while (stack and j > stack[-1][0]):
                stack1, stack2 = stack.pop()
                result[stack2] = i - stack2
            stack.append([j, i])
        return result 