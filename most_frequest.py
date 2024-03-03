def most_frequent(s):
    # Creating a dictionary to hold the frequency of each letter
    freq = {}
    for letter in s:
        if letter.isalpha():  # considering only alphabetic characters
            freq[letter] = freq.get(letter, 0) + 1

    # Sorting the dictionary by frequency in descending order
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # Printing the letters in decreasing order of frequency
    for letter, frequency in sorted_freq:
        print(f"{letter}: {frequency}")

most_frequent("example string")
