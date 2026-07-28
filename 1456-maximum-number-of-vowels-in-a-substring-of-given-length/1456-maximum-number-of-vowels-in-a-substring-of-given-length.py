class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "u", "o"}
        vowel_count = 0

        for i in range(k):
            if s[i] in vowels:
                vowel_count += 1

        max_vowel = vowel_count

        left = 0

        for right in range(k, len(s)):
            if s[left] in vowels:
                vowel_count -= 1
            left += 1

            if s[right] in vowels:
                vowel_count += 1

            max_vowel = max(max_vowel, vowel_count)

        return max_vowel        



                    