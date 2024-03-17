from algosdk.v2client import algod
from typing import Dict, Any, Optional
import webbrowser
import time
import os

class Account:

    algod_address = "https://testnet-api.algonode.cloud"
    algod_client = algod.AlgodClient('', algod_address)
    algo_conversion = 0.000001

    def __init__(self, address: str, private_key: Optional[str] = "-", pass_phrase: Optional[str] = "-", to_file: bool = False) -> None:
        self.address = address
        self.private_key = private_key
        self.pass_phrase = pass_phrase
        self.to_file = to_file
    
    def account_info(self) -> Dict[str, Any]:
        try:
            return self.algod_client.account_info(self.address)
        except Exception as e:
            self.write_message(f"Error fetching account info: {e}")
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
                print(f"Waiting for address {self.address} to be funded...")
                time.sleep(5)
            
            
            self.write_message(f"Address {self.address} has been funded and has {self.check_balance()} algoes!")
        else:
            self.write_message(f"Address {self.address} has been funded and has {self.check_balance()} algoes!")

    
    def write_message(self,message: str) -> None:
        formatted_message = f"Private key: {self.private_key}\nAddress: {self.address}\nMnemonic phrase: {self.pass_phrase}\nMessage: {message}\n"
        if self.to_file:
            self.write_to_file(message=formatted_message)
        else:
            self.write_to_console(message=formatted_message)

    def write_to_file(self, message: str, file_name: str = "./test_accounts.txt") -> None:
        mode = "w" if not os.path.exists(file_name) else "a"
        with open(file_name, mode) as file:
            file.write("\n" if mode == "a" else "")  # Add a newline before appending new data
            file.write(message)
        print("Data written to" if mode == "w" else "Data appended to", file_name)


    def write_to_console(self, message: str) -> None:
        print(message)


