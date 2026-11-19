text = input("enter any text ")
text_len = len(text)

print(text_len)
# countinhg words ...well use .split function
word_count = len(text.split())
print(word_count)

characters_without_spaces = len(text.replace(" ", ""))
print(characters_without_spaces)


####   OUTPUT
# enter any text: i love to eat apple because it is veryu healthy.
# 48
# 10
# 39
