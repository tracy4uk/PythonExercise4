def count_letters(text, letter):
    count = 0
    for char in text:
        if char == letter:
            count += 1
    return count
fruit = "banana"
letter_to_count = "a"
count = count_letters(fruit, letter_to_count)
print(count)
