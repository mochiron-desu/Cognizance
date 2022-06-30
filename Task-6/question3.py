import string

file = open("about.txt", "r")
data = file.read()
text = str.split(data, " ")

big_words = []
word_count = dict()
for word in text:
    for letters in word:
        if letters in string.punctuation:
            letters = None
    if len(word) >= 6:
        big_words.append(word)
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
counts = sorted(word_count.items(), key=lambda kv: kv[1])

print(big_words)
print(counts[-1])