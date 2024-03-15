from algosdk import account, encoding, mnemonic
import os
from accounts import Account
from datetime import datetime

# TODO
# Once account is created
# Load with algoes ( optional )
# If yes, automatically load with algoes
# If no, prompt the user to fill the account with algoes and continously check in intervals if done so

class InvalidAddressError(Exception):
    def __init__(self, message="The address is invalid, please try creating a new account.") -> None:
        self.message = message
        super().__init__(self.message)

def load_account(address, private_key, pass_phrase) -> Account:
    return Account(address=address, private_key=private_key, pass_phrase=pass_phrase)

def generate_account() -> Account:
    # generate an account
    private_key, address = account.generate_account()
    pass_phrase = mnemonic.from_private_key(private_key)

    # check if the address is valid
    if not encoding.is_valid_address(address):
        raise InvalidAddressError()
    
    user_account = load_account(address=address,private_key=private_key,pass_phrase=pass_phrase)
    user_account.write_to_console(message=f"Account successfuly created on {datetime.today()}")
    return user_account

