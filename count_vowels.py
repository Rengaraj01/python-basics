word = "hello"

count = 0

for letter in word:
    if letter in "aeiouAEIOU":
        count += 1

print(count)
