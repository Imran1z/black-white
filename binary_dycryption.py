def binary_to_text(binary_representation, file_path):
    # Remove the '0b' prefix and any spaces
    binary_representation = binary_representation.replace(' ', '')[2:]

    # Convert binary string to integer
    integer_value = int(binary_representation, 2)

    # Convert integer to bytes
    byte_data = integer_value.to_bytes((integer_value.bit_length() + 7) // 8, 'big')

    # Write bytes to a file
    with open(file_path, 'wb') as file:
        file.write(byte_data)

# Read the binary representation from the text file
with open('binary_representation.txt', 'r') as file:
    binary_representation = file.read()

# Convert binary representation back to text
binary_to_text(binary_representation, 'original_text.txt')
