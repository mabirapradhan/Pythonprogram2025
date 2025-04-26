# 1. Check if a string contains only alphabetic characters
def is_only_alpha(s):
    return s.isalpha()

# 2. Check if a string is a palindrome (without direct reverse method)
def is_palindrome(s):
    s = s.lower()
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True

# 3. Find the longest word in a sentence
def longest_word(sentence):
    words = sentence.split()
    longest = max(words, key=len)
    return longest

# 4. Find frequency of each character
def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

# 5. Remove all duplicate words from a sentence
def remove_duplicate_words(sentence):
    words = sentence.split()
    seen = set()
    result = []
    for word in words:
        if word not in seen:
            seen.add(word)
            result.append(word)
    return ' '.join(result)

# 6. Check if two words are anagrams
def are_anagrams(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())

# 7. WAP to compress a string (e.g., "aaabbc" → "a3b2c1")
word='aaabbc'
result=""
i=0
while i<len(word): # 0<6
    count=1
    while (i+1<len(word)) and (word[i]==word[i+1]):
        count+=1
        i+=1
    result+=word[i]+str(count)
    i+=1
print(result)
