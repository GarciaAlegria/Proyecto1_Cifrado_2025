from Crypto.Cipher import ARC4
import binascii

# Datos
hex_cifrado = "6d4080499d48a3ab0ac7e965ca7eb90510b84006d09a0c5f75b491c5c5245a42b06b36337d"
clave = "21285"  # Número de carné

# Convertir la clave a bytes
clave_bytes = clave.encode()

# Convertir el hexadecimal a bytes
cifrado_bytes = binascii.unhexlify(hex_cifrado)

# Crear el descifrador RC4
rc4 = ARC4.new(clave_bytes)

# Descifrar
mensaje_descifrado = rc4.decrypt(cifrado_bytes)

# Mostrar el resultado
def es_texto_legible(texto):
    try:
        texto.decode('utf-8')
        return True
    except UnicodeDecodeError:
        return False

if es_texto_legible(mensaje_descifrado):
    print("Mensaje descifrado:", mensaje_descifrado.decode('utf-8'))
else:
    print("Mensaje descifrado en bytes:", mensaje_descifrado)
