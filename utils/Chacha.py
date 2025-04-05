from nami_chacha import chacha20_decrypt
from binascii import unhexlify

# La cadena hexadecimal cifrada
hex_ciphertext = "3fc06ae08a1fadebd28e6fd903756702673de26a2bd05affcf4ba3c0b630d438336db15436"

try:
    # Convertir la cadena hexadecimal a bytes
    ciphertext_bytes = unhexlify(hex_ciphertext)
    
    # Tu user_id (en este caso usamos "21285" como en la función original)
    user_id = "21285"
    
    # Desencriptar
    plaintext = chacha20_decrypt(ciphertext_bytes, user_id)
    print("Mensaje desencriptado:", plaintext)
except Exception as e:
    print(f"Error al desencriptar: {str(e)}")