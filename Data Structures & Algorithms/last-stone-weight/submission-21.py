class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            num1 = heapq.heappop(maxHeap)
            num2 = heapq.heappop(maxHeap)
            if num1 == num2:
                pass
            else:
                heapq.heappush(maxHeap, num1 - num2)
        if len(maxHeap) == 0:
            return 0
        else:
            return -maxHeap[0]