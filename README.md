# 🔐 CipherPixel - Secure Image Steganography System

## 📌 Overview

CipherPixel is a secure image steganography system that hides secret messages inside images.
It combines **encryption and steganography** to ensure that data is both hidden and protected.

---

## 🚀 Features

* 🔐 Encrypts message using key-based encryption
* 🖼 Hides encrypted data inside images (LSB technique)
* 🔓 Decodes message using correct key
* 📥 Download encoded image
* 🌐 Deployed as a web application using Streamlit

---

## 🧠 How It Works

1. User enters a secret message and key
2. Message is encrypted using XOR encryption
3. Encrypted data is embedded into image pixels using LSB
4. Encoded image is generated (looks identical to original)
5. Receiver uploads encoded image and enters key
6. Message is decrypted and displayed

---

## 🛠 Technologies Used

* Python
* Streamlit
* Pillow (PIL)
* Steganography (LSB technique)

---

## 🌐 Live Demo

👉 https://cipherpixel-steganography-lcq4yntpwpvzeusl5kpfvy.streamlit.app/

---

## 📁 Project Structure

```
CipherPixel/
│── app.py
│── stego.py
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation (Local Setup)

```bash
pip install streamlit pillow
```

Run the app:

```bash
streamlit run app.py
```

---

## 🔐 Security Note

* Only users with the correct key can decode the message
* Incorrect key will fail decryption
* PNG images are used to avoid data loss

---

## 🎯 Applications

* Secure communication
* Military data transfer
* Cybersecurity
* Privacy protection

---

## 🏆 Future Enhancements

* Stronger encryption algorithms
* Support for multiple file types
* User authentication system
* Mobile app integration

---

## 👩‍💻 Author

Developed as part of a hackathon project 🚀
