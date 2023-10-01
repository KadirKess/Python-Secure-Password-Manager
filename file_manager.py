from os import path
from cryptography.fernet import Fernet
from hash_manager import read_key, encode_hash, valid_password


def read_file(username):
    '''
    This funciton will read the .crendentials file associated to the user as a single sequence of bytes.
    :param username: (string) The username.
    :return: (bytes) The data stored in the file.
    '''
    with open(username + ".credentials", "rb") as file:
        lines = file.read()
        return lines


def write_file(username, data):
    '''
    This function will write data in bytes in the .credentials file associated to the user.
    :param username: (string) The username.
    :param data: (Any) The data that will be written.
    '''
    with open(username + ".credentials", "wb") as file:
        file.write(data)


def encrypt_file(username, password):
    '''
    This function encrypts the file associated with username using the given password.
    :param username: (string) The username.
    :param password: (string) The password.
    '''
    hash = read_key(username)
    if valid_password(hash, password):
        encoded_hash = encode_hash(hash)
        encryptor = Fernet(encoded_hash)

        lines = read_file(username)
        cipher = encryptor.encrypt(lines)

        write_file(username, cipher)


def show_data_file(username):
    '''
    This function prints the data written in the .credentials file.
    :param username: (string) The username.
    '''
    with open(username + ".credentials", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line)


def decrypt_file(username, password):
    '''
    This function decrypts the file associated with username using the given password.
    :param username: (string) The username.
    :param password: (string) The password.
    :return: (bool) True if it was done successfully, False if the file path doesn't exist.
    '''
    if path.exists(username + ".credentials"):
        hash = read_key(username)
        if valid_password(hash, password):
            encoded_hash = encode_hash(hash)
            decryptor = Fernet(encoded_hash)

            lines = read_file(username)
            data = decryptor.decrypt(lines)

            write_file(username, data)
            return True
    else:
        return False