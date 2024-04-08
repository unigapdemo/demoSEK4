def remove_even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            numbers.remove(number)
    return numbers

# Intended to remove all even numbers from the list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'asd']