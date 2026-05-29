from cryptography.fernet import Fernet

def decrypt_krio_file(file_name):
    with open("secret.key", "rb") as chaabhi:
        local_chaabhi = chaabhi.read()

    cypher = Fernet(local_chaabhi)
    with open(file_name, "rb") as f:
        encrypted_data = f.read()

    decrypted_file_hai = cypher.decrypt(encrypted_data)
    with open("decrypt_kr_di_" + file_name.replace(".encrypted", ""), "wb") as f:
        f.write(decrypted_file_hai)

    print("kar di yrr file decrypt!")

decrypt_krio_file("Gtm.py.encrypted")