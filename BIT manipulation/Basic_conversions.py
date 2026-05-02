def decimal_to_binary(num):
    if num == 0:
        return "0"

    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2

    return binary

# Example
print(decimal_to_binary(13))



def binary_to_decimal(binary):
    decimal = 0
    power = 0

    for bit in reversed(binary):
        decimal += int(bit) * (2 ** power)
        power += 1

    return decimal

# Example
print(binary_to_decimal("1011"))
