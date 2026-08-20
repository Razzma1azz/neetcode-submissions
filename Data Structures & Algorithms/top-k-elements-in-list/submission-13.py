class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        
        freq_list = list(seen.items())
        sorted_list = sorted(freq_list, key=lambda pair: pair[1], reverse=True)
        new_list = []
        for highest in sorted_list[:k]:
            piece = highest[0]
            new_list.append(piece)

        return new_list



    

            
        
        

            



