import random

def generate_random_numbers(count, min_val, max_val):
    """Generates a list of random numbers within a specified range."""
    numbers = []
    for _ in range(count):
        numbers.append(random.randint(min_val, max_val))
    return numbers

def calculate_average(numbers):
    """Calculates the average of a list of numbers."""
    if not numbers:
        return 0  # Avoid division by zero
    return sum(numbers) / len(numbers)

def find_max_and_min(numbers):
  """Finds the maximum and minimum values in a list."""
  if not numbers:
    return None, None
  return max(numbers), min(numbers)


def greet(name):
    """Greets the person passed in as a parameter."""
    print(f"Hello, {name}!")

def process_data(data):
    """Processes a list of data and performs some operations."""
    results = []
    for item in data:
        if isinstance(item, int):
            results.append(item * 2)  # Double integers
        elif isinstance(item, str):
            results.append(item.upper())  # Convert strings to uppercase
        else:
            results.append(item)  # Keep other data types as they are
    return results

def main():
    """Main function to demonstrate the other functions."""
    random_numbers = generate_random_numbers(10, 1, 100)
    print("Random Numbers:", random_numbers)

    average = calculate_average(random_numbers)
    print("Average:", average)

    max_num, min_num = find_max_and_min(random_numbers)
    print("Maximum:", max_num)
    print("Minimum:", min_num)

    greet("Alice")

    mixed_data = [10, "hello", 3.14, "world", 20, True]
    processed_data = process_data(mixed_data)
    print("Processed Data:", processed_data)

if __name__ == "__main__":
    main()

import random

def generate_random_numbers(count, min_val, max_val):
    """Generates a list of random numbers within a specified range."""
    numbers = []
    for _ in range(count):
        numbers.append(random.randint(min_val, max_val))
    return numbers

def calculate_average(numbers):
    """Calculates the average of a list of numbers."""
    if not numbers:
        return 0  # Avoid division by zero
    return sum(numbers) / len(numbers)

def find_max_and_min(numbers):
  """Finds the maximum and minimum values in a list."""
  if not numbers:
    return None, None
  return max(numbers), min(numbers)


def greet(name):
    """Greets the person passed in as a parameter."""
    print(f"Hello, {name}!")

def process_data(data):
    """Processes a list of data and performs some operations."""
    results = []
    for item in data:
        if isinstance(item, int):
            results.append(item * 2)  # Double integers
        elif isinstance(item, str):
            results.append(item.upper())  # Convert strings to uppercase
        else:
            results.append(item)  # Keep other data types as they are
    return results

def main():
    """Main function to demonstrate the other functions."""
    random_numbers = generate_random_numbers(10, 1, 100)
    print("Random Numbers:", random_numbers)

    average = calculate_average(random_numbers)
    print("Average:", average)

