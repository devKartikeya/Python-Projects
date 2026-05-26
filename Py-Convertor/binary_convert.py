def binary_convert(num):
    if num < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif num == 0:
        return "0"
    
    binary_str = ""
    while num > 0:
        binary_str = str(num % 2) + binary_str
        num //= 2
    
    # binary_str = format(num, 'b') # Alternative method using built-in function
    
    print(f"The binary representation of the number is: {binary_str}") 