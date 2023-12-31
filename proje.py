import tkinter as tk
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64
import time
import psutil
import os

# Anahtar Üretimi
def generate_key():
    return get_random_bytes(32)  # 256-bit anahtar üretimi

# Şifreleme Fonksiyonu
def encrypt(message, key):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    encrypted = cipher.encrypt(pad(message.encode(), AES.block_size))
    return base64.b64encode(iv + encrypted).decode()

# Şifre Çözme Fonksiyonu
def decrypt(encrypted, key):
    encrypted = base64.b64decode(encrypted)
    iv = encrypted[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(encrypted[16:]), AES.block_size)
    return decrypted.decode()

# Performans Ölçümü Fonksiyonu
def perform_performance_measurement():
    key = generate_key()
    message = "Test Mesajı" * 100  # Performans testi için büyük bir metin

    # Şifreleme süresi ölçümü
    start_time = time.time()
    encrypted_message = encrypt(message, key)
    end_time = time.time()
    encryption_time = end_time - start_time

    # Şifre çözme süresi ölçümü
    start_time = time.time()
    decrypt(encrypted_message, key)
    end_time = time.time()
    decryption_time = end_time - start_time

    # Bellek kullanımı ölçümü
    process = psutil.Process(os.getpid())
    memory_usage = process.memory_info().rss / (1024 * 1024)  # MB cinsinden

    # Sonuçların gösterilmesi
    performance_result.set(f"Şifreleme Süresi: {encryption_time:.5f} saniye\n"
                           f"Şifre Çözme Süresi: {decryption_time:.5f} saniye\n"
                           f"Bellek Kullanımı: {memory_usage:.2f} MB")

# Anahtar ve Şifrelenmiş Mesajın Sıfırlanması
def reset_key_and_encrypted_message():
    entry_key.delete(0, tk.END)
    entry_encrypted.delete(0, tk.END)
    entry_result.delete(0, tk.END)

# Şifreleme ve Şifre Çözme İşlemleri
def perform_encryption_decryption(is_encrypt):
    key_hex = entry_key.get()
    message = entry_message.get()
    
    if not key_hex or not message:
        entry_result.delete(0, tk.END)
        entry_result.insert(0, "Anahtar ve mesaj gerekli.")
        return
    
    key = bytes.fromhex(key_hex)
    
    if is_encrypt:
        encrypted_message = encrypt(message, key)
        entry_encrypted.delete(0, tk.END)
        entry_encrypted.insert(0, encrypted_message)
    else:
        encrypted_message = entry_encrypted.get()
        decrypted_message = decrypt(encrypted_message, key)
        entry_result.delete(0, tk.END)
        entry_result.insert(0, decrypted_message)

def generate_and_display_key():
    new_key = generate_key()
    entry_key.delete(0, tk.END)
    entry_key.insert(0, new_key.hex())
    entry_encrypted.delete(0, tk.END)  # Şifrelenmiş mesajı sıfırla

# Arayüz Oluşturma
root = tk.Tk()
root.title("Şifreleme Arayüzü")

# Performans sonucunu saklamak için StringVar
performance_result = tk.StringVar()

# Giriş Alanları
tk.Label(root, text="Mesaj:").grid(row=0, column=0)
entry_message = tk.Entry(root, width=50)
entry_message.grid(row=0, column=1)

tk.Label(root, text="Anahtar:").grid(row=1, column=0)
entry_key = tk.Entry(root, width=50)
entry_key.grid(row=1, column=1)

tk.Label(root, text="Şifrelenmiş Mesaj:").grid(row=2, column=0)
entry_encrypted = tk.Entry(root, width=50)
entry_encrypted.grid(row=2, column=1)

tk.Label(root, text="Şifresi Çözülmüş Mesaj:").grid(row=3, column=0)
entry_result = tk.Entry(root, width=50)
entry_result.grid(row=3, column=1)

# Performans Etiketi
label_performance = tk.Label(root, text="Performans Ölçümü:")
label_performance.grid(row=4, column=0, columnspan=2)

# Düğmeler
button_encrypt = tk.Button(root, text="Şifrele", command=lambda: perform_encryption_decryption(True))
button_encrypt.grid(row=5, column=0)

button_decrypt = tk.Button(root, text="Şifre Çöz", command=lambda: perform_encryption_decryption(False))
button_decrypt.grid(row=5, column=1)

button_generate_key = tk.Button(root, text="Anahtar Üret", command=generate_and_display_key)
button_generate_key.grid(row=5, column=2)

button_reset = tk.Button(root, text="Sıfırla", command=reset_key_and_encrypted_message)
button_reset.grid(row=6, column=0, columnspan=2)

# Performans Ölçümü Düğmesi
button_performance = tk.Button(root, text="Performans Ölçümleri", command=perform_performance_measurement)
button_performance.grid(row=7, column=0, columnspan=2)

# Performans Sonuçları Etiketi
label_performance_results = tk.Label(root, textvariable=performance_result)
label_performance_results.grid(row=8, column=0, columnspan=2)

# Ana Döngü
root.mainloop()
