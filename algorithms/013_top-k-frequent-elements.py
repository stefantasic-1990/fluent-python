# 013: Top K Frequent Elements
#
# Given a non-empty list of integers nums, return the k most frequent elements as a list.
# You must not use any built-in sorting functions like sorted() or .sort().
import heapq

nums = [2, 2, 1, 1, 1, 3]
k = 2

def solve(nums: list[int], k: int) -> list[int]:
    freqs = {}
    
    for n in nums:
        freqs[n] = freqs.get(n, 0) + 1

    freq_list = [(-val, key) for key, val in freqs.items()]
    heapq.heapify(freq_list)
    top_k = [heapq.heappop(freq_list)[1] for _ in range(k)]

    return top_k

print(solve(nums=nums, k=k))