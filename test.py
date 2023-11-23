from des import *

print("DES Python Implementation v1.0")
print("==============================")

user_input = input("'e' to encrypt a message, 'd' to decrypt a message, or 'exit' to exit")

while user_input != "exit":

    if user_input == "e":
        user_input = input("Enter your message: ")
        message = user_input
        key = ""
        while len(key) != 8:
            if(len(key) != 0):
                print("Invalid key length.")
            user_input = input("Enter your key (8 characters): ")
            key = user_input
        print("Your encrypted message is: \n" + encrypt(message, key))
        user_input = input("\n 'e' to encrypt another message, 'd' to decrypt a message, or 'exit' to exit")

    elif user_input == "d":
        user_input = input("Enter your message: ")
        message = user_input
        key = ""
        while len(key) != 8:
            if(len(key) != 0):
                print("Invalid key length.")
            user_input = input("Enter your key (8 characters): ")
            key = user_input
        print("Your decrypted message is: \n" + decrypt(message, key))
        user_input = input("\n 'e' to encrypt a message, 'd' to decrypt another message, or 'exit' to exit")

    elif user_input == "exit":
        pass

    else:
        user_input = input("Not a valid command.")