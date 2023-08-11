def findSubstring(s, k):
    a = []
    text = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(s)-k+1):
        b = ""
        for j in range(i, i+k):
            b += s[j].lower()
        a.append(b)
    c = []
    for i in a:
        count = 0
        for j in i:
            if j in text:
                count += 1
            else:
                break
        c.append(count)
    max_count = max(c)
    max_string = a[c.index(max_count)]
    return max_string

def count_vowels(substring):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return sum(1 for char in substring if char in vowels)

def findSubstring(s, k):
    if not any(char in {'a', 'e', 'i', 'o', 'u'} for char in s):
        return 'Not found!'

    max_vowel_count = 0
    max_vowel_substring = ''

    for i in range(len(s) - k + 1):
        substring = s[i:i+k]
        vowel_count = count_vowels(substring)

        if vowel_count > max_vowel_count:
            max_vowel_count = vowel_count
            max_vowel_substring = substring

    return max_vowel_substring
    
s = 'azerdii'
k = 5

findSubstring(s, k)
print(findSubstring(s, k))