# changing to binary

# def file_to_binary(file_path):
#     with open(file_path, 'r') as file:
#         content = file.read()
#         binary_content = ' '.join(format(ord(char), '08b') for char in content)
#     return binary_content

# # Assuming text.txt is in the same folder as the script
# file_path = 'text.txt'
# binary_content = file_to_binary(file_path)
# print(binary_content)





# changing to binary without space

# def file_to_binary(file_path):
#     with open(file_path, 'r') as file:
#         content = file.read()
#         binary_content = ' '.join(format(ord(char), '08b') for char in content)
#         binary_content = binary_content.replace(' ', '00100000')  # Replacing space with its binary representation
#     return binary_content

# # Example usage
# file_path = 'text.txt'
# binary_content = file_to_binary(file_path)
# print(binary_content)




# encrypting working
import zlib

def file_to_binary(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        binary_content = ''.join(format(ord(char), '08b') for char in content)
        return binary_content

def xor_encrypt(binary_content, key):
    key_length = len(key)
    encrypted_content = ''
    for i, bit in enumerate(binary_content):
        encrypted_bit = str(int(bit) ^ int(key[i % key_length]))
        encrypted_content += encrypted_bit
    return encrypted_content

# Example usage
file_path = 'text.txt'
key = '1010'  # Shorter XOR encryption key
binary_content = file_to_binary(file_path)
encrypted_content = xor_encrypt(binary_content, key)

# Compress the encrypted content
compressed_content = zlib.compress(encrypted_content.encode())

# Convert bytes to binary representation
binary_representation = bin(int.from_bytes(compressed_content, byteorder='big'))

# Save the binary representation to a text file
with open('binary_representation.txt', 'w') as file:
    file.write(binary_representation)

# Print confirmation message
print("Binary representation saved to 'binary_representation.txt'")














































































# with file savingclear
# import zlib

# def file_to_binary(file_path):
#     with open(file_path, 'r') as file:
#         content = file.read()
#         binary_content = ''.join(format(ord(char), '08b') for char in content)
#         return binary_content

# def xor_encrypt(binary_content, key):
#     key_length = len(key)
#     encrypted_content = ''
#     for i, bit in enumerate(binary_content):
#         encrypted_bit = str(int(bit) ^ int(key[i % key_length]))
#         encrypted_content += encrypted_bit
#     return encrypted_content

# # Example usage
# file_path = 'text.txt'
# key = '1010'  # Shorter XOR encryption key
# binary_content = file_to_binary(file_path)
# encrypted_content = xor_encrypt(binary_content, key)

# # Compress the encrypted content
# compressed_content = zlib.compress(encrypted_content.encode())

# # Save the compressed and encrypted content into a new file
# output_file_path = 'encrypted_text.txt'
# with open(output_file_path, 'wb') as output_file:
#     output_file.write(compressed_content)

# print("File saved successfully:", output_file_path)




