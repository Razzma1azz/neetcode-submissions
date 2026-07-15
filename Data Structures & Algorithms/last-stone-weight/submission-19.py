class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            num1 = heapq.heappop(maxHeap)
            num2 = heapq.heappop(maxHeap)
            survivor = num1 - num2
            if num1 == num2:
                heapq.heapify(maxHeap)
            else:
                heapq.heappush(maxHeap, survivor)
        if len(maxHeap) == 0:
            return 0
        else:
            return -maxHeap[0]