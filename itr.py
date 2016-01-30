word = raw_input("Enter a word in English").lower()
for c in word:
    if c == ' ':
        first = word1[:1]
        print (word1[1:] + first + "ay ")    
    else:
        word1 = word1 + c
    