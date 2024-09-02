Function: "add_numbers"
def add_numbers(num1, num2):
    """Returns the sum of num1 and num2."""
    return num1 + num2

result = add_numbers(5, 4)
print(result)  # Output: 9


Function: "is_even"
def is_even(number):
    """Returns True if number is even, otherwise False."""
    return number % 2 == 0

Function: "reverse_string"
def reverse_string(text):
    """Returns the reversed version of text."""
    return text[::-1]


Function: "count_vowels"
def count_vowels(text):
    """Counts the number of vowels in the given text."""
    vowels = 'aeiou'
    text = text.lower()
    return sum(1 for char in text if char in vowels)


Function: "calculate_factorial"
def calculate_factorial(n):
    """Returns the factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

Function: "apply_decorator"
def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

def apply_decorator(func):
    return decorator_func(func)


Function: "sort_by_age"
def sort_by_age(lst):
    """Sorts a list of tuples by age in ascending order."""
    return sorted(lst, key=lambda x: x[1])

Function: "merge_dicts"
def merge_dicts(dict1, dict2):
    """Merges two dictionaries, summing values for common keys."""
    merged = dict(dict1)  # Start with a copy of dict1
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged


Class: "Car"
class Car:
    def __init__(self, make, model, year):
        """Initializes a new Car object with make, model, and year."""
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        """Displays information about the car."""
        print(f"{self.year} {self.make} {self.model}")











