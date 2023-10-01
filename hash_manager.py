from argon2 import PasswordHasher
import base64


def generate_hash(username, password):
    '''
    This function generates a hash (what a suprise) of the password linked to the username.
    :param username: (string) The username.
    :param password: (string) The password.
    :return: (string) The hash of the password.
    '''
    hash = PasswordHasher().hash(password)
    print(f"Your profile was created ! A key  {username} has been successfully generated !.")
    print("Restarting the manager")
    return hash


def encode_hash(hash):
    '''
    This function encodes the first 32 bytes of a given string hash into a URL-safe Base64 string.
    :param hash: (string) The hash value it will encode.
    :return: (string) The encoded hash value.
    '''
    encoded_hash = hash.encode()
    encoded_hash = base64.urlsafe_b64encode(encoded_hash[:32])
    return encoded_hash


def store_key(username, key):
    '''
    This function stores user's information in a .key file.
    :param username: (string) The username will be the name of the file.
    :param key: (string) The key will be written in the file.
    '''
    with open(username + ".key","w") as master_pwd:
        master_pwd.write(key)


def read_key(username):
    '''
    This function reads user's key stored in the associated .key file.
    :param username: (string) The username that will be used to find the file.
    :return: (string) The key stored in the file.
    '''
    with open(username + ".key","r") as master_pwd:
        key = master_pwd.read()
    return key


def valid_password(hash, password):
    '''
    This function will check if the given password and its hash corresponds.
    :param hash: (string) The real hash value of the password.
    :param password: (string) The password the user tries.
    :return: (bool) True if the password is correct, false otherwise.
    '''
    try:
        PasswordHasher().verify(hash, password)
        return True
    except:
        return False
