class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        vowels = ['a', 'e', 'i', 'o', 'u']

        # Step 1: Precompute if each word starts and ends with a vowel
        is_vowel_word = [1 if word[0] in vowels and word[-1] in vowels else 0 for word in words]

        # Step 2: Build the prefix sum array
        prefix_sum = [0] * len(words)
        prefix_sum[0] = is_vowel_word[0]

        for i in range(1, len(words)):
            prefix_sum[i] = prefix_sum[i-1] + is_vowel_word[i]

        # Step 3: Process each query using the prefix sum array
        values = []
        for query in queries:
            li, ri = query
            if li > 0:
                result = prefix_sum[ri] - prefix_sum[li-1]
            else:
                result = prefix_sum[ri]
            values.append(result)

        return values
