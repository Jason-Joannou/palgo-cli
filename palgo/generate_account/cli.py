import argparse
from generate_account import generate_account

def main() -> None:
    account = generate_account()
    account.fund_address()


if __name__ == "__main__":
    main()