words = text.split()  # Split the text into a list of words
        result = []  # To store the third words
        
        # Iterate through the words, stopping before the last two words
        for i in range(len(words) - 2):
            # Check if the current word is first, the next word is second, and the word after that is third
            if words[i] == first and words[i + 1] == second:
                result.append(words[i + 2])  # Add the third word to the result list
                
        return result
