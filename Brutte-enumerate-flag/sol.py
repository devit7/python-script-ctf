import itertools
""" from secrets import flag,kunci

def enkripsi(flag, kunci):
    enkripsi = []
    for i, j in enumerate(flag):
        enkripsi.append((j + ord(kunci[i % len(kunci)])) % 127)#ord() mengembalikan nilai integer dari sebuah karakter
    return enkripsi


print(f'Output = {enkripsi(flag, kunci)}') """
Output = [45, 48, 41, 61, 65, 20, 34, 95, 86, 83, 82, 76, 78, 94, 76, 73, 80, 89, 85, 65, 90, 83, 85, 67, 97, 82, 85, 78, 80, 95, 82, 75, 96, 65, 88, 79, 83, 97]

def decrypt(ciphertext, kunci):
    decrypted = []
    for i, j in enumerate(ciphertext):
        decrypted_char = (j - ord(kunci[i % len(kunci)])) % 127
        decrypted.append(decrypted_char)
    return decrypted

encrypted_data = [79, 56, 115, 38, 105]  # Contoh data terenkripsi
known_prefix = "cicilan"  # Bagian dari kunci yang sudah diketahui
desired_suffix = "}"  # Bagian dari hasil dekripsi yang diinginkan
# Daftar karakter yang akan digunakan dalam kunci (a-z)
character_set = 'abcdefghijklmnopqrstuvwxyz0123456789'

max_possible_key_length = 8  # Maksimal panjang kunci yang Anda ingin coba

for key_length in range(1, max_possible_key_length + 1):
    # Menghasilkan semua kemungkinan kombinasi karakter kunci
    key_combinations = itertools.product(character_set, repeat=key_length)
    
    for key_combination in key_combinations:
        key = known_prefix + ''.join(key_combination)
        decrypted_result = decrypt(Output, key)

        # Cek apakah hasil dekripsi adalah teks yang masuk akal (hanya karakter ASCII yang dicetak)
        if all(0 <= char <= 126 for char in decrypted_result):
            decrypted_text = ''.join(chr(char) for char in decrypted_result)
            
            """ # Periksa apakah string "IFEST23{" ada dalam hasil dekripsi
            if "IFEST23{" in decrypted_text:
                print(f"Key: {key}, Decrypted Text: {decrypted_text}")
             """# Periksa apakah string yang diinginkan ada di akhir hasil dekripsi
            if decrypted_text.endswith(desired_suffix) and '|' not in decrypted_text and '/' not in decrypted_text and '[' not in decrypted_text and ']' not in decrypted_text and '{' not in decrypted_text :
                if "IFEST23{" in decrypted_text:
                    print(f"Key: {key}, Decrypted Text: {decrypted_text}")

""" for i in range(0, 127):
    print(f"Key = {chr(i)}")
    print(f"Output = {decrypt([45, 48, 41, 61, 65, 20, 34, 95, 86, 83, 82, 76, 78, 94, 76, 73, 80, 89, 85, 65, 90, 83, 85, 67, 97, 82, 85, 78, 80, 95, 82, 75, 96, 65, 88, 79, 83, 97], chr(i))}")
    print("=====================================") """



