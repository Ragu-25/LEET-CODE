class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer=prices[:]
        stack=[]
        for i in range(len(prices)):
            while stack and prices[i]<=prices[stack[-1]]:
                index=stack.pop()
                answer[index]=prices[index]-prices[i]
            stack.append(i)
        return answer        