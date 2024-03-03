def count_even_numbers(numbers):
    count = 0  # Initialize a counter for even numbers
    for num in numbers:
        if num % 2 == 0:  # Check if the number is even
            count += 1
    return count

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Count of even numbers: {count_even_numbers(numbers)}")
