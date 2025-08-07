def count_words(text):
    words=text.split()
    freq={}
    for character in words:
        freq[character]=freq.get(character,0)+1
    return freq
print(count_words("hello hello world"))


