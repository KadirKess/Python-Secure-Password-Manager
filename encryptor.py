from os import path
from cryptography.fernet import Fernet
from getpass import getpass
from hash_manager import read_key, encode_hash, valid_password
from file_manager import decrypt_file


def encrypt_data(username, password):
    '''
    This function encrypts the user's data using a generated cipher.
    :param username: (string) The username.
    :param password: (string) The password.
    '''
    hash = read_key(username)
    if valid_password(hash, password):
        service_name = input("Service name : ")
        username_service = input(f'Your username for {service_name} is : ')
        pwd_service = getpass(prompt=f'Your password for {service_name} is : ')

        encoded_hash = encode_hash(hash)
        encryptor = Fernet(encoded_hash)
        cipher = encryptor.encrypt(pwd_service.encode())
        store_credentials(username, password, service_name, username_service, cipher)


def store_credentials(username, password, service_name, username_service, cipher):
    '''
    This function stores the encrypted credentials of a user for a particular service.
    :param username: (string) The username.
    :param password: (string) The password.
    :param service_name: (string) The name of the service.
    :param username_service: (string) The username for the service.
    :param cipher: (object) The cipher object used for encryption.
    '''
    if path.exists(username + ".credentials"):
        decrypt_file(username, password)
    with open(username + ".credentials", "a") as credentials:
        credentials.write(service_name + "\t" + username_service + "\t" + cipher.decode() + "\n")
        print("Your data has been stored successfully !")