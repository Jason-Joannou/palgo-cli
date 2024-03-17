from algosdk import account, encoding, mnemonic
import os
from ..accounts import Account
from datetime import datetime
from typing import List

class InvalidAddressError(Exception):
    """
    Custom exception raised when an invalid address is encountered.
    """
    def __init__(self, message="The address is invalid, please try creating a new account.") -> None:
        """
        Initialize InvalidAddressError with a custom message.

        Parameters:
            message (str): Error message to be displayed. Defaults to a generic message.
        """
        self.message = message
        super().__init__(self.message)

def load_account(address: str, private_key: str, pass_phrase: str, to_file: bool) -> Account:
    """
    Load an account with the provided address, private key, passphrase, and save it to file if specified.

    Parameters:
        address (str): The address of the account.
        private_key (str): The private key associated with the account.
        pass_phrase (str): The passphrase generated from the private key.
        to_file (bool): Flag indicating whether to save the account to a txt file.

    Returns:
        Account: An instance of the Account class representing the loaded account.
    """
    return Account(address=address, private_key=private_key, pass_phrase=pass_phrase, to_file=to_file)

def generate_account(to_file: bool, n_accounts: int) -> List[Account]:
    """
    Generate a list of new accounts with the specified number and optionally save them to file.

    Parameters:
        to_file (bool): Flag indicating whether to save the generated accounts to file.
        n_accounts (int): The number of accounts to generate.

    Returns:
        List[Account]: A list of Account instances representing the generated accounts.
    Raises:
        InvalidAddressError: If an invalid address is encountered during account generation.
    """
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

