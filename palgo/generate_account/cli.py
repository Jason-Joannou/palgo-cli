import argparse
from generate_account import generate_account

def main(choice: str, to_file: bool) -> None:
    if choice == "fund":
        account = generate_account(to_file=to_file)
        account.fund_address()
    else:
        account = generate_account(to_file=to_file)
        account.account_info()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="cli",
        description="A CLI tool that allows a user to generate algorand accounts and optionally fund them.",
        epilog="Thanks for using the palgo generate account cli!")
    
    parser.add_argument("generate", metavar="CHOICE", help="Generate a new account based on the specified choice. "
                                                            "Use 'Create' to create an account only, or 'Fund' to create "
                                                            "and fund the account.", type=str, choices=["Create", "Fund", "create", "fund"])
    parser.add_argument("-wf", "--write-file", help="Write the contents of the accounts to a text file named 'test_accounts.txt'. By default %(prog)s writes to console",
                        action="store_true")
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 0.0.1")


    args = parser.parse_args()

    choice = args.generate.lower()
    to_file = args.write_file
    main(choice=choice, to_file=to_file)