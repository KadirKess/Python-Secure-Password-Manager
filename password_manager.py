from user_manager import *
from hash_manager import generate_hash, store_key
from encryptor import encrypt_data
from decryptor import decrypt_cipher
from file_manager import encrypt_file, decrypt_file, show_data_file

def first_menu():
    '''
    First menu, launched at the beggining.
    :return: (int) The choice made by the user.
    '''
    choice = int(input("""
    Options
		----------------------------------------------------------------------
		1. New user, REGISTER, GENERATE, STORE master password 
		2. Registered user, LOGIN
		3. Exit
		----------------------------------------------------------------------
    """))

    if choice == 1:
        print(f"Your choice is : {choice} | ------REGISTER------")
    elif choice == 2:
        print(f"Your choice is : {choice} | ------LOGIN------")
    elif choice == 3:
        print(f"Your choice is : {choice} | ------BYE !------")
    else:
        print(f"Your choice is : {choice} | ------!!!------")

    return choice

def second_menu():
    '''
    Second menu, appears when the user is logged in.
    :return: (int) Choice of the user.
    '''
    choice = int(input("""
    	Options
    	----------------------------------------------------------------------
    	1. CRYPT some passwords 
    	2. VISUALIZE my data
    	3. DECRYPT my password
    	4. Exit
    	----------------------------------------------------------------------
    	"""))

    if choice == 1:
        print(f"Your choice is : {choice} | ------CRYPT------")
    elif choice == 2:
        print(f"Your choice is : {choice} | ------VISUALIZE------")
    elif choice == 3:
        print(f"Your choice is : {choice} | ------DECRYPT------")
    elif choice == 4:
        print(f"Your choice is : {choice} | ------BYE !------")
    else:
        print(f"Your choice is : {choice} | ------!!!------")

    return choice


def main():
    '''
    Main function of the program.
    '''
    print('')
    print(15 * ' ', 25 * '*', 'PASSWORD MANAGER', 27 * '*')

    # First menu
    choice_1 = first_menu()

    # Register
    if choice_1 == 1:
        username, password = new_user()
        hash = generate_hash(username, password)
        store_key(username, hash)

    # Login - Second menu
    elif choice_1 == 2:
        username = input("Your name : ")
        password = getpass(prompt="Your password : ")

        # Login successfull
        if check_user(username, password):
            choice = second_menu()
            while choice != 4:

                # Crypt
                if choice == 1:
                    encrypt_data(username, password)
                    encrypt_file(username, password)

                # Visualize
                elif choice == 2:
                    if decrypt_file(username, password):
                        show_data_file(username)
                    else:
                        print("No data stored yet")
                    encrypt_file(username, password)

                # Decrypt
                elif choice == 3:
                    if decrypt_file(username, password):
                        pwd_decrypted = decrypt_cipher(username, password)
                        if pwd_decrypted:
                            print(pwd_decrypted, "is copied to clipboard ! ")
                        else:
                            print("No such service recorded")
                        encrypt_file(username, password)
                    else:
                        print("No data stored yet")

                else:
                    exit()
                choice = second_menu()
            exit()
        else:
            exit()

    elif choice_1 == 3:
        exit()
    else:
        exit()


if __name__ == '__main__':
    main()