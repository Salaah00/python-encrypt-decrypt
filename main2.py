import hashlib
from PIL import Image
import os
# fonction hash_password permet de Calculer Le Hash du mot de passe
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
# fonction embed hash in image permet d'injecter le mot de passe dans une image
def embed_hash_in_image(image_path, hashed_password):
    img = Image.open(image_path).convert('RGB')
    binary_hash = ''.join(format(ord(char), '08b') for char in hashed_password)

    pixels = bytearray(img.tobytes())

    for i in range(len(binary_hash)):
        pixels[i] = (pixels[i] & 0b11111110) | int(binary_hash[i])

    embedded_img = Image.frombytes('RGB', img.size, bytes(pixels))

    save_path = os.path.splitext(image_path)[0] + "_embedded.png"
    embedded_img.save(save_path)

    return save_path
#fonction extract hashed password from image permet d'extraire le hash du l'image
def extract_hashed_password_from_image(embedded_image_path, hash_length):
    embedded_img = Image.open(embedded_image_path).convert('RGB')

    extracted_binary_hash = ''

    pixels = bytearray(embedded_img.tobytes())

    for i in range(len(pixels)):
        extracted_binary_hash += str(pixels[i] & 1)

    extracted_hash = ''
    for i in range(0, len(extracted_binary_hash), 8):
        byte = extracted_binary_hash[i:i+8]
        extracted_hash += chr(int(byte, 2))
    extracted_hash = extracted_hash[:hash_length]
    print("\n"+extracted_hash+"\n")
    return extracted_hash
emb_path= "cat_embedded.png"
length = 64
if os.path.exists("cat_embedded.png"):
    extract_hashed_password_from_image(emb_path, length)
    password = input("Entrer Votre Mot De Passe : ")
    if hash_password(password) == extract_hashed_password_from_image(emb_path,length):
        print("authentication Granted")
    else:
        print("authentication Failed")
        exit()
else:
    password = input("Enter Your password: ")
    hashed_password = hash_password(password)
    user_input = input("What's Your Password : ")
    embed_hash_in_image(r"cat.png", hashed_password)
    if extract_hashed_password_from_image(emb_path, length) == user_input:
        print("Authentication Granted")
    else:
        print("Authentication Failed")
        exit()



















