from os import path
from getpass import getpass
from hash_manager import read_key, valid_password


def new_user():
    '''
    This function creates a new user.
    :return: (string, string) The username and its password.
    '''
    username = input("Enter your username : ")
    while path.exists(username + ".key"): # While the user keeps entering an existing username...
        print("This user already exists...Please chose another one !")
        username = input("Enter your username : ")
    password = getpass(prompt="Your master password : ")
    return username, password


def check_user(username, password):
    '''
    This function checks if the entered username and password match.
    :param username: (string) The username.
    :param password: (string) The password.
    :return: (bool) True if the entered username and password match, False otherwise.
    '''
    if path.exists(username + ".key"): # The function first checks if the user exists
        hash = read_key(username)
        if valid_password(hash, password): # It then checks if the hash value matches the password
            print(f"User : {username} (the password is right, you are connected)")
            return True
        else:
            print("The password is wrong") # And tells the user if it's not the case
            return False
    else:
        print("There is no user with this name") # If no user is found with this name, the function also returns False
        return False