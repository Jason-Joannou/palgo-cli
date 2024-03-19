# Generate Account CLI

The generate_account command-line interface (CLI) is a sub-command of the palgo CLI. You can access this CLI using the following command:

`python -m palgo.generate_account.cli -h`

Executing the above command will display the help menu, which outlines the available commands for this CLI.

# CLI commands

The generate_account CLI provides several commands that allow you to interact with it. Here are the available commands:

## Usage

The CLI is structured with the following usage format:

`usage: cli [-h] [-m NumAccounts] [-wf] [-v] CHOICE`

**CHOICE**

CHOICE is a positional argument and must be specified before any other optional arguments. The available choices are:

- Fund
- fund
- Create
- create

If you choose Fund, the CLI will create an account and prompt you to fund it with algoes. If you choose Create, the CLI will only create an account.

Example usage:

`python -m palgo.generate_account.cli Fund`

This command will create an account and prompt the user to fund it.

**`-m`**

The -m (short) or --multiple (long) is an optional argument that allows you to specify the number of accounts to create or fund. Example usage:

`python -m palgo.generate_account.cli Create -m 5`

This command will create 5 new accounts.

**`-wf`**

The -wf (short) or --write-file (long) is a boolean argument that specifies whether information about the newly created account(s) should be written to a file. By default, the CLI outputs results to the console, but specifying this argument will write the results to a file named test_accounts.txt.

Example usage:

`python -m palgo.generate_account.cli Create -wf`

**`-v`**

The -v (short) or --version (long) will return the current version number of the CLI. This command can be run independently of the positional argument. Example usage:

`python -m palgo.generate_account.cli -v`

**`-h`**

The -h (short) or --help (long) will display a help menu for the user to see the available commands in the CLI. This command can be run independently of the positional argument. Example usage:

`python -m palgo.generate_account.cli -h`





