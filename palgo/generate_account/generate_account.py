from algosdk import account, encoding, mnemonic
import os

def generate_account() -> None:
    # generate an account
    private_key, address = account.generate_account()
    pass_phrase = mnemonic.from_private_key(private_key)
    print("Private key: ", private_key)
    print("Address: ", address)
    print("Mnemonic phrase: ",pass_phrase)

    # check if the address is valid
    if encoding.is_valid_address(address):
        print("The address is valid!")
        write_to_file(data=(private_key, address, pass_phrase))
    else:
        print("The address is invalid.")

def write_to_file(data: tuple, file_name: str = "test_accounts.txt") -> None:
    private_key, address, pass_phrase = data
    if not os.path.exists(file_name):
        with open(file_name, "w") as file:
            file.write("Private key: {}\n".format(private_key))
            file.write("Address: {}\n".format(address))
            file.write("Mnemonic phrase: {}\n".format(pass_phrase))
        print("Data written to", file_name)
    else:
        with open(file_name, "a") as file:
            file.write("\n")  # Add a newline before appending new data
            file.write("Private key: {}\n".format(private_key))
            file.write("Address: {}\n".format(address))
            file.write("Mnemonic phrase: {}\n".format(pass_phrase))
        print("Data appended to", file_name)
