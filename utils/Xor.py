def xor_decrypt(hex_string, key):
    # Convertir la cadena hexadecimal en bytes
    encrypted_bytes = bytes.fromhex(hex_string)
    
    # Convertir el número de carné en bytes y repetirlo para que tenga la misma longitud que la cadena hexadecimal
    key_bytes = str(key).encode()
    key_length = len(key_bytes)
    
    # Aplicar XOR
    decrypted_bytes = bytes(b ^ key_bytes[i % key_length] for i, b in enumerate(encrypted_bytes))
    
    # Convertir el resultado a una cadena ASCII
    return decrypted_bytes.decode(errors='ignore')

hex_string = "747d737f6a0308030a0706045400030a08010d0d0503510c065700575e020007505b060a55"
carnet = 21285

decrypted_text = xor_decrypt(hex_string, carnet)
print("Texto desencriptado:", decrypted_text)