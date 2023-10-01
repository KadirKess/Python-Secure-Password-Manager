from cryptography.fernet import Fernet
from hash_manager import read_key, encode_hash, valid_password
import pyperclip as pc

def get_cipher(username, service_name) :
	'''
    This function retrieves the cipher object for a user and a particular service.
    :param username: (string) The username.
    :param service_name: (string) The name of the service.
    :return: (object) The cipher object used for decryption or (bool) False if it does not exist.
	'''
	with open(username + ".credentials","r") as credentials :
		line = credentials.readline()
		while line :
			data = line.split('\t')
			if data[0] == service_name:
				return data[2]
			line = credentials.readline()
		return False

def decrypt_cipher(username, password):
	'''
    This function decrypts the cipher to retrieve the user's data.
    :param username: (string) The username.
    :param password: (string) The password.
    :return: (string) The decrypted data.
	'''
	hash = read_key(username)
	if valid_password(hash, password) :
		service_name = input("Service name : ")
		pwd_encrypted = get_cipher(username, service_name)

		encoded_hash = encode_hash(hash)
		decryptor = Fernet(encoded_hash)

		if pwd_encrypted :
			pwd_encrypted = pwd_encrypted.encode()
			pwd_decrypted = decryptor.decrypt(pwd_encrypted)
			pwd_decrypted = pwd_decrypted.decode()
			pc.copy(pwd_decrypted)
			return pwd_decrypted
		else :
			return False