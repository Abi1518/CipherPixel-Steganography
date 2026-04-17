import streamlit as st
from PIL import Image
from stego import *

st.title("🔐 CipherPixel - Secure Image Steganography")

option = st.radio("Choose Option", ["Encode", "Decode"])

key_input = st.text_input("Enter Key", type="password")

# Ensure key is always valid
key = str(key_input) if key_input else "secret"
key = key.strip()

uploaded_file = st.file_uploader("Upload Image (PNG only)", type=["png"])


# 🔐 ENCODE
if option == "Encode" and uploaded_file is not None:
    message = st.text_area("Enter Secret Message")

    if st.button("Encode"):
        image = Image.open(uploaded_file)

        encrypted = encrypt_message(message, key)
        encoded_img = encode_image(image, encrypted)

        encoded_img.save("encoded.png")

        st.image(encoded_img, caption="Encoded Image")
        st.success("✅ Message hidden successfully!")


# 🔓 DECODE
elif option == "Decode" and uploaded_file is not None:
    if st.button("Decode"):
        image = Image.open(uploaded_file)

        try:
            data = decode_image(image)
            decrypted = decrypt_message(data, key)

            st.success("🔓 Decoded Message: " + decrypted)
        except:
            st.error("❌ Wrong key or invalid image!")
