from algosdk.v2client import algod
from algosdk import transaction, mnemonic
from base64 import b64decode
import json
from ..accounts import Account
from typing import Dict

class InsufficientFunds(Exception):

    def __init__(self, message) -> None:
        super().__init__(message)

class Transact():

    def __init__(self) -> None:
        self.api_key = ''
        self.algod_address = "https://testnet-api.algonode.cloud"
        self.algod_client = algod.AlgodClient(self.api_key, self.algod_address)
        self.params = self.algod_client.suggested_params()

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
        print("Successfully submitted transaction with txID: {}".format(txid))

        # wait for confirmation
        txn_result = transaction.wait_for_confirmation(self.algod_client, txid)

        print(f"Transaction information: {json.dumps(txn_result, indent=4)}")
        print(f"Decoded note: {b64decode(txn_result['txn']['txn']['note'])}")

        return txn_result
