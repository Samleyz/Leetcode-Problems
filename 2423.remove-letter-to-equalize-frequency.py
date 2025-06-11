def createDictionary(word):
        dictionary = {}
        for letter in word:
            
            if letter in dictionary:
                dictionary[letter] += 1
            else:
                dictionary[letter] = 1
        return dictionary

class Solution(object):
    

    def equalFrequency(self, word):
        """
        :type word: str
        :rtype: bool
        """
      
        
        
        alpha = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

        frequency = dict()
        for char in word:
            alpha[char] += 1
        
        for key in alpha:
            if key !=0:
                alpha[key] -= 1

                for check in alpha:
                    if alpha[check] != 0:
                        if alpha[check] not in frequency:
                            frequency[alpha[check]] = 0
                        frequency[alpha[check]] += 1

                if len(frequency) == 1:
                    return True
                    
                alpha[key] += 1
                frequency = dict()

        return False
