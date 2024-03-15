from algosdk.v2client import algod
from typing import Dict, Any
import webbrowser
import time
import os

class Account:

    algod_address = "https://testnet-api.algonode.cloud"
    algod_client = algod.AlgodClient('', algod_address)
    algo_conversion = 0.000001

    def __init__(self, address: str, private_key: str, pass_phrase: str) -> None:
        self.address = address
        self.private_key = private_key
        self.pass_phrase =pass_phrase
    
    def account_info(self) -> Dict[str, Any]:
        try:
            return self.algod_client.account_info(self.address)
        except Exception as e:
            print(f"Error fetching account info: {e}")
            return {}

    def check_balance(self) -> int:
        account_info = self.account_info()
        return account_info['amount'] * self.algo_conversion
    
    def fund_address(self) -> None:
        
        if self.check_balance() <= 1:
            print(f"The address {self.address} has not been funded and will not be able to transact with other accounts.")
            print(f"Please fund address {self.address} using the algorand test dispensor.")
            try:
                webbrowser.open_new_tab("https://bank.testnet.algorand.network/")
            except webbrowser.Error:
                print("Failed to open URL in browser. Please manually open the URL provided.")
                print("URL:", "https://bank.testnet.algorand.network/")

            while self.check_balance() <= 1:
                print(f"Waiting for address {self.address} to be funding...")
                time.sleep(5)

            print(f"Address {self.address} has been funded and has {self.check_balance()} algoes!")

            return
        
        print(f"Address {self.address} has been funded and has {self.check_balance()} algoes!")
        return
    
    def write_to_file(self, file_name: str = "test_accounts.txt", message: str = "None") -> None:
        if not os.path.exists(file_name):
            with open(file_name, "w") as file:
                file.write("Private key: {}\n".format(self.private_key))
                file.write("Address: {}\n".format(self.address))
                file.write("Mnemonic phrase: {}\n".format(self.pass_phrase))
                file.write("Message: {}\n".format(message))
            print("Data written to", file_name)
        else:
            with open(file_name, "a") as file:
                file.write("\n")  # Add a newline before appending new data
                file.write("Private key: {}\n".format(self.private_key))
                file.write("Address: {}\n".format(self.address))
                file.write("Mnemonic phrase: {}\n".format(self.pass_phrase))
                file.write("Message: {}\n".format(message))
            print("Data appended to", file_name)

    def write_to_console(self, message: str) -> None:
        print("Private key: {}".format(self.private_key))
        print("Address: {}".format(self.address))
        print("Mnemonic phrase: {}".format(self.pass_phrase))
        print("Message: {}".format(message))
        print("")


