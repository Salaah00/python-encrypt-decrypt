from tkinter import *
from tkinter import filedialog, messagebox
from maskpass import *
from cryptography.fernet import Fernet
from main import check_face
from main2 import *

#def run_face_recognition():
    #root = Tk()
    #root.withdraw()
    #check_face()
    #root.destroy()
def encrypt_images():
    file_paths = filedialog.askopenfilenames(filetypes=[('all files','.*')],multiple=True)
    if file_paths:
        key = entry1.get("1.0", END).strip()
        try:
            if not key:
                raise ValueError("Please enter a key.")

            for file_path in file_paths:
                with open(file_path, 'rb') as f:
                    image = bytearray(f.read())

                for index, value in enumerate(image):
                    image[index] = value ^ int(key)

                with open(file_path, 'wb') as f:
                    f.write(image)

            print("Encryption successful!")
            messagebox.showinfo("Success", "Encryption successful!")

        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror("Error", f"Error: {e}")
def decrypt_images():
    file_paths = filedialog.askopenfilenames(filetypes=[('all files','.*')],multiple=True)
    if file_paths:
        key = entry1.get("1.0", END).strip()

        try:
            if not key:
                raise ValueError("Please enter a key.")

            for file_path in file_paths:
                with open(file_path, 'rb') as f:
                    image = bytearray(f.read())

                for index, value in enumerate(image):
                    image[index] = value ^ int(key)

                with open(file_path, 'wb') as f:
                    f.write(image)
            print("Decryption successful!")
            messagebox.showinfo("Success", "Decryption successful!")

        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror("Error", f"Error: {e}")
# Function to encrypt and write a password to a file
def generate_key():
    key = Fernet.generate_key()
    with open("key.txt", 'wb') as key_file:
        key_file.write(key)
    return key

# Function to read the key from a file
def read_key():
    try:
        with open("key.txt", 'rb') as key_file:
            key = key_file.read()
        return key
    except FileNotFoundError:
        raise ValueError("No key file found.")

#Encrypt and write to file
def write_encrypted_password(password):
    key = read_key()
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(password.encode('utf-8')) 

    with open("encrypted_password.txt", 'wb') as file:
        file.write(cipher_text)

#decrypt the password from a file
def read_decrypted_password():
    key = read_key()
    cipher_suite = Fernet(key)

    try:
        with open("encrypted_password.txt", 'rb') as file:
            encrypted_password = file.read()
    except FileNotFoundError:
        raise ValueError("No encrypted password file found.")

    decrypted_password = cipher_suite.decrypt(encrypted_password)
    return decrypted_password.decode('utf-8')

def main_():
    password = read_decrypted_password()
    while True:
        ch = askpass(mask="")
        if ch == password:
            print("Welcome  \\n")
            #stegno()
            #run_face_recognition()
            break
        else:
            print("Please check the password ")
try:
    main_()
except ValueError as e:
    print(f"Error: {e}")
    password = askpass(mask="")
    generate_key()
    write_encrypted_password(password)
root = Tk()
root.geometry("290x180")
root.title("Image Encryptor")
root.resizable(False, False)
root.configure(bg='#263D42')
entry1 = Text(root, height=0, width=15, bg='#C5C8C6', fg='#1D1F21', font=('Helvetica', 10))
entry1.place(x=150, y=50)
label1 = Label(root, text="Enter Key:", bg='#263D42', fg='#C5C8C6', font=('Helvetica', 10))
label1.place(x=50, y=50)
b1 = Button(root, text="Encrypt", command=encrypt_images, bg='#B31312', fg='#1D1F21', font=('Helvetica', 12, 'bold'))
b1.place(x=50, y=80)
b2 = Button(root, text="Decrypt", command=decrypt_images, bg='#005B41', fg='#1D1F21', font=('Helvetica', 12, 'bold'))
b2.place(x=50, y=125)
root.mainloop()
