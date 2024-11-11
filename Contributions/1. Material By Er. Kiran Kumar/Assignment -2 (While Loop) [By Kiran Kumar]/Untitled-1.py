


# Function to convert binary to decimal
def binary_to_decimal(binary_str):
    # Using int() with base 2 to convert binary to decimal
    decimal_number = int(binary_str, 2)
    return decimal_number 

# Taking binary input from the user
binary_str = input("Enter a binary number: ")






# Checking if input is valid binary
if all(char in '01' for char in binary_str):
    # Converting binary to decimal
    decimal_number = binary_to_decimal(binary_str)
    print("Decimal equivalent:", decimal_number)
else:
    print("Invalid input! Please enter a binary number (only 0s and 1s).")







def print_series(n):
    term = "2"  # Start with the first term as "2"
    for i in range(1, n + 1):
        print(term, end=", " if i < n else "\n")
        term += "2"  # Add another "2" to the term for the next iteration

# Example usage:
n = int(input("Enter the number of terms: "))
print_series(n)
