class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}
        max_odd = 0
        
        for i in s:
            if i not in freq:
                freq[i] = 1
            else:freq[i] +=1
        min_even = max(freq.values())
        for i in freq.values():
            if i % 2 == 0 :
                if i < min_even:
                    min_even = i
            else:
                if i > max_odd:
                    max_odd = i

        return (max_odd - min_even)
