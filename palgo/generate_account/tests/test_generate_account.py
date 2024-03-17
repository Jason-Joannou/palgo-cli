import pytest
from unittest.mock import Mock, patch
from ...accounts import Account
from ..generate_account import generate_account, InvalidAddressError

@pytest.fixture
def mock_algo_gen_account():

    with patch("algosdk.account.generate_account") as mock_gen:
        mock_instance = mock_gen
        mock_instance.return_value = ("private_key","address")

        yield mock_instance

@pytest.fixture
def mock_mnemonic():

    with patch("algosdk.mnemonic.from_private_key") as mock_mn:
        mock_instance = mock_mn
        mock_instance.return_value = "mnemonic"

        yield mock_instance

@pytest.fixture
def mock_encoding():

    with patch("algosdk.encoding.is_valid_address") as mock_mn:
        mock_instance = mock_mn
        mock_instance.return_value = True

        yield mock_instance

def test_generate_account(mock_algo_gen_account, mock_mnemonic, mock_encoding):

    # These asserts can be split into their own methods
    wf = False
    n_accounts = 1
    test_pk, test_address = ("private_key","address")

    test_account = generate_account(to_file=wf,n_accounts=n_accounts)
    mock_algo_gen_account.assert_called_once()
    private_key, address = mock_algo_gen_account.return_value
    assert test_pk == private_key, f"Validation failed, test private key '{test_pk}' is not matching returned private key '{private_key}'"
    assert test_address == address, f"Validation failed, test address '{test_address}' is not matching returned address '{address}'"

def test_mnemonic(mock_algo_gen_account, mock_mnemonic, mock_encoding):
    # These asserts can be split into their own methods
    wf = False
    n_accounts = 1
    test_mnemonic = "mnemonic"

    test_account = generate_account(to_file=wf,n_accounts=n_accounts)
    mock_mnemonic.assert_called_once()
    mnemonic = mock_mnemonic.return_value
    assert test_mnemonic == mnemonic, f"Validation failed, test mnemonic '{test_mnemonic}' is not matching returned mnemonic '{mnemonic}'"


def test_encoding(mock_algo_gen_account, mock_mnemonic, mock_encoding):

    # These asserts can be split into their own methods
    wf = False
    n_accounts = 1

    test_account = generate_account(to_file=wf,n_accounts=n_accounts)

    mock_encoding.assert_called_once()
    mock_encoding.return_value = False
    with pytest.raises(InvalidAddressError):
        test_account = generate_account(to_file=wf,n_accounts=n_accounts)

def test_account_return(mock_algo_gen_account, mock_mnemonic, mock_encoding):

    wf = False
    n_accounts = 1

    test_account = generate_account(to_file=wf,n_accounts=n_accounts)

    assert isinstance(test_account, list), f"Validation failed, type of test account {type(test_account)} did not match list type"
    assert isinstance(test_account[0], Account), f"Validation failed, type of test account {type(test_account)} did not match Account type"


