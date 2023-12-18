# python-encrypt-decrypt
 Python application that incorporates three-factor authentication for file encryption and decryption 
 This application employs the following methods to ensure data security:

    Facial Recognition:
        The initial security layer of our application relies on facial recognition. Users must submit a capture of their image for verification. We utilize a facial recognition library to compare the capture with pre-registered models, ensuring accurate identification.

    Steganography:
        Steganography is integrated to enhance the security of encrypted files. Before the encryption process, sensitive data is concealed within an image using steganographic algorithms. This technique adds an additional layer of obscurity, reinforcing the confidentiality of information.

    Password Authentication:
        In addition to the methods mentioned above, the application also requires password authentication. Users must provide a strong password that will be hashed using the SHA-256 algorithm. This hash is then compared with the stored hash to verify the user's authenticity.

Application Operation:

    The user launches the application and chooses between file encryption and decryption.
    For encryption, the user submits a facial capture, enters their password, and selects the file to encrypt.
    Before encryption, sensitive data is hidden within an image using steganography.
    The file is then encrypted using a robust algorithm.
    For decryption, the user submits another facial capture and enters their password.
    Steganographic data is extracted from the image.
    The encrypted file is decrypted only if facial authentication and the password are valid.

Our application provides a high level of security through three-factor authentication. The combination of facial recognition, steganography, and password authentication ensures robust protection of confidential data. We welcome any suggestions for improvement and are committed to maintaining the security of our application at the highest level.
