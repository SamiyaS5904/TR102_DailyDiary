# Bitwise Shift Operators for encryption/decryption

num1 = 8
num2 = 2

# Right shift: Equivalent to integer division by 2^num2
result1 = num1 >> num2

# Left shift: Equivalent to multiplication by 2^num2
result2 = num1 << num2

print("result1:", result1)
print("result2:", result2)

# Encrypting using right shift
data = 8
key = 2
encrypted_data = data >> key
print('encrypted_data:', encrypted_data)

# Decrypting by reversing shift
original_data = encrypted_data << key
print('original_data:', original_data)
