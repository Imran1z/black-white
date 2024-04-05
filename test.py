from PIL import Image
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


def binary_to_image(binary_data, width, height):
    """Converts binary data to a black and white image."""
    image = Image.new('1', (width, height))  # Create black and white image
    pixels = image.load()
    for i, bit in enumerate(binary_data):
        x = i % width  # Calculate pixel coordinates
        y = i // width
        pixels[x, y] = int(bit)  # Set pixel to white for '1', black for '0'
    return image


# Example usage
file_path = 'text.txt'
key = '1010'  # Shorter XOR encryption key

# Retrieve binary content
binary_content = file_to_binary(file_path)
encrypted_content = xor_encrypt(binary_content, key)

# Compress the encrypted content
compressed_content = zlib.compress(encrypted_content.encode())

# Convert bytes to binary string representation
binary_representation = bin(int.from_bytes(compressed_content, byteorder='big'))[2:]  # Remove '0b' prefix

# Set image dimensions
image_width = 256  # Adjust these values as needed
image_height = 256

# Convert binary data to image and save
image = binary_to_image(binary_representation, image_width, image_height)
image.save('binary_image.png')

print("Binary image saved to 'binary_image.png'")