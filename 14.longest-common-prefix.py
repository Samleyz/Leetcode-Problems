def longestCommonPrefix(self, strs: List[str]) -> str:
        if "" in strs:
            return ""
        if all(i == strs[0] for i in strs):
            return ''.join(strs[0])
        prefix = ''
        seen= set()
        first_word = min(strs,key= len)
        
        strs.remove(first_word)
        num = 0
        for i in strs:
            try:    
                while i[num] == first_word[num]:

                    prefix += i[num]
                    num +=1
                    if num == len(first_word) :
                        break
            except IndexError:
                prefix == first_word   
            seen.add(prefix)
            num = 0
            prefix = ''
        return min(seen)
