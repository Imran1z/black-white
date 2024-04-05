import zlib

def xor_decrypt(encrypted_content, key):
    key_length = len(key)
    decrypted_content = ''
    for i, bit in enumerate(encrypted_content):
        decrypted_bit = str(int(bit) ^ int(key[i % key_length]))
        decrypted_content += decrypted_bit
    return decrypted_content

# Read the compressed and encrypted content from the file
input_file_path = 'original_text.txt'
with open(input_file_path, 'rb') as input_file:
    compressed_content = input_file.read()

# Decompress the content
encrypted_content = zlib.decompress(compressed_content).decode()

# Decrypt the content
key = '1010'  # Same XOR encryption key used for encryption
decrypted_content = xor_decrypt(encrypted_content, key)

# Convert binary content back to text
def binary_to_text(binary_content):
    text = ''
    for i in range(0, len(binary_content), 8):
        byte = binary_content[i:i+8]
        text += chr(int(byte, 2))
    return text

original_text = binary_to_text(decrypted_content)

print("Decrypted content:")
print(original_text)


