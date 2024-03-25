from algosdk.v2client import algod
from algosdk import transaction, mnemonic
from base64 import b64decode
import json
from ..accounts import Account
from typing import Dict
import os

class InsufficientFunds(Exception):

    def __init__(self, message) -> None:
        super().__init__(message)

class Transact():

    def __init__(self, to_file: bool = False) -> None:
        self.api_key = ''
        self.algod_address = "https://testnet-api.algonode.cloud"
        self.algod_client = algod.AlgodClient(self.api_key, self.algod_address)
        self.params = self.algod_client.suggested_params()
        self.to_file = to_file

    def single_sig_transaction(self, sender_account: Account, receiver_account: Account, amount: float, note: str) -> Dict:
        # Have to make sure that sender address has cash to send, if not they must fund
        if sender_account.check_balance()<amount:
            raise InsufficientFunds(f"Transaction Declined. Account {sender_account.address} has insufficient funds to perform the transaction")
        # Have to validate the addresses as well
        unsigned_txn = transaction.PaymentTxn(
        sender=sender_account.address,
        sp=self.params,
        receiver=receiver_account.address,
        amt=amount, # Amount variable is measured in MicroAlgos. i.e. 1 ALGO = 1,000,000 MicroAlgos
        note=note,)

        private_key_sender = mnemonic.to_private_key(sender_account.pass_phrase)
        # sign the transaction
        signed_txn = unsigned_txn.sign(private_key_sender)

        # submit the transaction and get back a transaction id
        txid = self.algod_client.send_transaction(signed_txn)
        self.write_message("Successfully submitted transaction with txID: {}".format(txid))

        # wait for confirmation
        txn_result = transaction.wait_for_confirmation(self.algod_client, txid)

        self.write_message(f"Transaction information: {json.dumps(txn_result, indent=4)}")
        self.write_message(f"Decoded note: {b64decode(txn_result['txn']['txn']['note'])}")

        return txn_result
    
    def write_message(self,message: str) -> None:
        if self.to_file:
            self.write_to_file(message=message)
        else:
            self.write_to_console(message=message)

    def write_to_file(self, message: str, file_name: str = "./test_accounts.txt") -> None:
        mode = "w" if not os.path.exists(file_name) else "a"
        with open(file_name, mode) as file:
            file.write("\n" if mode == "a" else "")  # Add a newline before appending new data
            file.write(message)
        print("Data written to" if mode == "w" else "Data appended to", file_name)


    def write_to_console(self, message: str) -> None:
        print(message)
