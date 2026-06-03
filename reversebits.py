def reverse_bits(n):
    binary = bin(n)[2:]        # convert to binary, strip '0b'
    reversed_binary = binary[::-1]   # reverse the string
    result = int(reversed_binary, 2) # convert back to decimal

    print(f"\nDecimal         : {n}")
    print(f"Binary          : {binary}")
    print(f"Reversed binary : {reversed_binary}")
    print(f"New decimal     : {result}")

try:
    number = int(input("Enter a number: "))
    if number < 0:
        print("Please enter a non-negative integer.")
    else:
        reverse_bits(number)
except ValueError:
    print("Invalid input. Please enter a whole number.")