def read_numbers_from_file(filename):
    """Reads integers from a file and returns them as a list."""
    numbers = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line:  # Ensure line is not empty
                numbers.append(int(line))
    return numbers


def calculate_statistics(numbers):
    """Calculates and returns total, sum, average, min, and max of the numbers."""
    total = len(numbers)
    if total == 0:
        return 0, 0, 0, None, None  # Handle empty list safely
    sum_values = sum(numbers)
    average = round(sum_values / total)
    min_value = min(numbers)
    max_value = max(numbers)
    return total, sum_values, average, min_value, max_value


def display_statistics(total, sum_values, average, min_value, max_value):
    """Displays the calculated statistics."""
    print(f"Total = {total}")
    print(f"Summation = {sum_values}")
    print(f"Average = {average}")
    if min_value is not None and max_value is not None:
        print(f"Minimum = {min_value}")
        print(f"Maximum = {max_value}")
    else:
        print("Minimum = N/A")
        print("Maximum = N/A")


def compute_stats(filename):
    """Main function to execute the full process."""
    try:
        numbers = read_numbers_from_file(filename)
        total, sum_values, average, min_value, max_value = calculate_statistics(numbers)
        display_statistics(total, sum_values, average, min_value, max_value)
    except FileNotFoundError:
        print("Error: File not found.")
    except ValueError:
        print("Error: Invalid data in file. Please ensure all lines are integers.")


if __name__ == "__main__":
    compute_stats("random_nums.txt")
