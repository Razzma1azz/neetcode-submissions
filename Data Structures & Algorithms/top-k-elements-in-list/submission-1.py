class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        freq_list = list(dict.items())
        freq_list.sort(key=lambda pair: pair[1], reverse=True)

        return [num for num, count in freq_list[:k]]