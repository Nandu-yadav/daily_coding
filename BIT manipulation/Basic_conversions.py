


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


#3. 1s compliment, 


#4. 2s compliment



#Operators  AND OR XOR     


#5. SWAP numbers 
def swapNumBit(a,b):
    a=a^b
    b=a^b
    a=a^b
    return a,b
print(swapNumBit(4,5))

#6. Extract i th bit




#7.   set i-th bit




#8.   Toggle the i-th bit





#9.    Check if power of 2





#10 .    Count the set bits

