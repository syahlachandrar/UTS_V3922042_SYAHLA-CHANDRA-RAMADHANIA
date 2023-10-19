#!/usr/bin/env python
# coding: utf-8

# In[15]:


# Fungsimengenkripsi teks dengan Caesar Cipher
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()  # Cek apakah karakter adalah huruf besar
            char = char.lower()  # Konversi huruf ke huruf kecil
            encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))  # Enkripsi karakter dengan Caesar Cipher
            if is_upper:
                encrypted_char = encrypted_char.upper()  # Konversi kembali ke huruf besar jika semula huruf besar
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Tambahkan karakter non-huruf langsung

    return encrypted_text

# Fungsi untuk mendekripsi teks dengan Caesar Cipher
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)  # Mendekripsi dengan menggeser mundur sebanyak shift

# Fungsi untuk mengenkripsi teks dengan Vigenere Cipher
def vigenere_encrypt(text, key):
    encrypted_text = ""
    key_length = len(key)
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            is_upper = char.isupper()  # Cek apakah karakter adalah huruf besar
            char = char.lower()  # Konversi huruf ke huruf kecil
            key_char = key[i % key_length]  # Ambil karakter kunci yang sesuai dengan indeks saat ini
            key_shift = ord(key_char) - ord('a')  # Hitung pergeseran berdasarkan karakter kunci
            encrypted_char = caesar_encrypt(char, key_shift)  # Enkripsi karakter dengan Caesar Cipher menggunakan pergeseran dari kunci
            if is_upper:
                encrypted_char = encrypted_char.upper()  # Konversi kembali ke huruf besar jika semula huruf besar
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Tambahkan karakter non-huruf langsung

    return encrypted_text

# Fungsi untuk mendekripsi teks dengan Vigenere Cipher
def vigenere_decrypt(text, key):
    decrypted_text = ""
    key_length = len(key)
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            is_upper = char.isupper()  # Cek apakah karakter adalah huruf besar
            char = char.lower()  # Konversi huruf ke huruf kecil
            key_char = key[i % key_length]  # Ambil karakter kunci yang sesuai dengan indeks saat ini
            key_shift = ord(key_char) - ord('a')  # Hitung pergeseran berdasarkan karakter kunci
            decrypted_char = caesar_decrypt(char, key_shift)  # Mendekripsi karakter dengan Caesar Cipher menggunakan pergeseran dari kunci
            if is_upper:
                decrypted_char = decrypted_char.upper()  # Konversi kembali ke huruf besar jika semula huruf besar
            decrypted_text += decrypted_char
        else:
            decrypted_text += char  # Tambahkan karakter non-huruf langsung

    return decrypted_text

# Teks yang akan dienkripsi
plaintext = "Success is not final, failure is not fatal, it is the courage to continue that counts"
vigenere_key = "syahla"
caesar_shift = 65

# Enkripsi teks menggunakan Vigenere Cipher, kemudian Caesar Cipher
vigenere_encrypted_text = vigenere_encrypt(plaintext, vigenere_key) # Enkripsi Vigener lebih dulu
final_encrypted_text = caesar_encrypt(vigenere_encrypted_text, caesar_shift) #hasil vigener dienkrip menggunakan caesar

print("Teks Asli:", plaintext)
print("Hasil Enkripsi:", final_encrypted_text)

# Mendekripsi teks
decrypted_text = caesar_decrypt(final_encrypted_text, caesar_shift) # Dekrip menggunakan caesar cipher
vigenere_decrypted_text = vigenere_decrypt(decrypted_text, vigenere_key) #Dekrip hasil caesar dengan vigener

print("Hasil Dekripsi:", vigenere_decrypted_text)


# In[ ]:





# In[ ]:




