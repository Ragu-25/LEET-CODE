class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_counts = {0: 1}
        curr_sum = 0
        total_subarrays = 0
        
        for num in nums:
            curr_sum += num
            if (curr_sum - goal) in prefix_counts:
                total_subarrays += prefix_counts[curr_sum - goal]
            prefix_counts[curr_sum] = prefix_counts.get(curr_sum, 0) + 1
            
        return total_subarrays