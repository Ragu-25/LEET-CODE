class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        current = blocks[:k].count('W')
        minimum = current
        for i in range(1, len(blocks) - k + 1):
            if blocks[i - 1] == 'W':
                current -= 1
            if blocks[i + k - 1] == 'W':
                current += 1
            minimum = min(minimum, current)
            
        return minimum