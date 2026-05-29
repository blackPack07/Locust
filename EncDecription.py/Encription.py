from cryptography.fernet import Fernet

# generating a key kyuki isi m store karna hai
key = Fernet.generate_key()
with open("secret.key", "wb") as file_key:
    file_key.write(key)

# ab krunga file encrypt,
# isme bs ek method bnao jo filename as argument lega
def encrypt_the_file(filename):
    with open("secret.key", "rb") as key_file:
        key = key_file.read()

        meri_key = Fernet(key) 
        with open(filename, "rb") as f:
            file_data = f.read()
        
        # ab file to ban gyi, now hume new encrypted file ko store krayge
        encrypted_data = meri_key.encrypt(file_data)

        with open(filename + ".encrypted", "wb") as f:
            f.write(encrypted_data)
        
        print("Mene file encrypt kar di hai")

encrypt_the_file("Gtm.py")