# 013: Top K Frequent Elements
#
# Given a non-empty list of integers nums, return the k most frequent elements.
# You must not use any built-in sorting functions like sorted() or .sort().
import heapq

nums = [2, 2, 1, 1, 1, 3]
k = 2

def solve(nums: list[int], k: int) -> list[int]:
    freqs = {}
    for i in nums:
        if i not in freqs:
            freqs[i] = 1
        else:
            freqs[i] += 1

    freq_heap = [(-val, key) for key, val in freqs.items()]
    heapq.heapify(freq_heap) # modifies the list in place.
    top_k = [heapq.heappop(freq_heap)[1] for _ in range(k)]

    return top_k

solution = solve(nums=nums, k=k)
print(solution)