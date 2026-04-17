from PIL import Image

# 🔐 XOR Encryption (Stable)
def encrypt_message(message, key):
    message = str(message)
    key = str(key)

    encrypted = []
    for i in range(len(message)):
        m = ord(message[i])
        k = ord(key[i % len(key)])
        encrypted.append(chr(m ^ k))

    return ''.join(encrypted).encode()


# 🔓 XOR Decryption
def decrypt_message(encrypted_message, key):
    encrypted_text = encrypted_message.decode()
    key = str(key)

    decrypted = []
    for i in range(len(encrypted_text)):
        m = ord(encrypted_text[i])
        k = ord(key[i % len(key)])
        decrypted.append(chr(m ^ k))

    return ''.join(decrypted)


# 🖼 Encode data into image
def encode_image(image, secret_data):
    binary_data = ''.join(format(byte, '08b') for byte in secret_data)
    binary_data += '1111111111111110'  # End marker

    img = image.copy()
    pixels = img.load()

    data_index = 0

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixel = list(pixels[i, j])

            for k in range(3):
                if data_index < len(binary_data):
                    pixel[k] = pixel[k] & ~1 | int(binary_data[data_index])
                    data_index += 1

            pixels[i, j] = tuple(pixel)

    return img


# 🖼 Decode data from image
def decode_image(image):
    binary_data = ""
    pixels = image.load()

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pixel = pixels[i, j]

            for k in range(3):
                binary_data += str(pixel[k] & 1)

                # Stop early when end marker found
                if binary_data.endswith('1111111111111110'):
                    binary_data = binary_data[:-16]  # remove marker

                    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]

                    decoded = ""
                    for byte in all_bytes:
                        decoded += chr(int(byte, 2))

                    return decoded.encode()

    return b""

