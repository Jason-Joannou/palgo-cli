from algosdk import account, encoding, mnemonic
import os
from accounts import Account
from datetime import datetime
from typing import List

# TODO
# Once account is created
# Load with algoes ( optional )
# If yes, automatically load with algoes
# If no, prompt the user to fill the account with algoes and continously check in intervals if done so

class InvalidAddressError(Exception):
    def __init__(self, message="The address is invalid, please try creating a new account.") -> None:
        self.message = message
        super().__init__(self.message)

def load_account(address: str, private_key: str, pass_phrase: str, to_file: bool) -> Account:
    return Account(address=address, private_key=private_key, pass_phrase=pass_phrase, to_file=to_file)

def generate_account(to_file: bool, n_accounts: int) -> List[Account]:
    accounts = []
    for _ in range(1,n_accounts+1):
        # generate an account
        private_key, address = account.generate_account()
        pass_phrase = mnemonic.from_private_key(private_key)

        # check if the address is valid
        if not encoding.is_valid_address(address):
            raise InvalidAddressError()
        
        user_account = load_account(address=address,private_key=private_key,pass_phrase=pass_phrase,to_file=to_file)
        user_account.write_message(message=f"Account successfuly created on {datetime.today()}")
        accounts.append(user_account)
    return accounts

