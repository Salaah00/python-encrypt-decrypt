import tkinter as tk 
from tkinter import *
from tkinter import filedialog, messagebox
import face_recognition


#def callImageProgram():
    #subprocess.call(["python", "app.py"])

# Function to check if the face matches
def check_face():
    known_image = face_recognition.load_image_file("known_face.jpg")
    known_face_encoding = face_recognition.face_encodings(known_image)[0]
    file_path = filedialog.askopenfilename(filetypes=[('Image files', '*.png;*.jpg;*.jpeg')])
    if file_path:
        unknown_image = face_recognition.load_image_file(file_path)
        unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
        results = face_recognition.compare_faces([known_face_encoding], unknown_face_encoding)

        if results[0]:
            messagebox.showinfo("Success", "Face recognition successful!")
            #callImageProgram()
            root.destroy()
        else:
            messagebox.showerror("Error", "Face recognition failed!")
            exit()

# GUI setup
root = Tk()
root.geometry("290x180")
root.title("Face recognition")
root.resizable(False, False)

# Background color
root.configure(bg='#263D42')

# Face Lock button
b3 = Button(root, text="Face Lock", command=check_face, bg='#1255B3', fg='#1D1F21', font=('Helvetica', 12, 'bold'))
b3.place(x=150, y=80)
root.mainloop()
