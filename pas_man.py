from cryptography.fernet import Fernet

"""
key + password + text to encrypt = random text
random text + key + password = text to encrypt 
"""

"""
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()
"""


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)



def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print(f"User: {user}, Password: {fer.decrypt(passw).decode()}")

def add():
    """
    I create a new file if the file storing our password is does'nt exist already and add the password into it
    first get the user account and then the password and then add it into the file
    """
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")



while True: 

    mode = input("Would you like to add a new password or view existing ones (view, add)? Press q to quit ").lower()
    if mode == "q":
        break

    elif mode == "view":
        view()
        break

    elif mode == "add":
        add()
        break

    else:
        print("Invalid Mode")
        continue