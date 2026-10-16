"""Helper functions for safe user input."""


def get_non_empty(prompt):
    """Keep asking until the user types something non-empty."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def get_int(prompt, min_value=None, max_value=None):
    """Keep asking until the user enters a valid whole number in range."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue
        if min_value is not None and value < min_value:
            print(f"Value must be at least {min_value}.")
        elif max_value is not None and value > max_value:
            print(f"Value must be at most {max_value}.")
        else:
            return value


def get_float(prompt, min_value=None, max_value=None):
    """Keep asking until the user enters a valid number in range."""
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if min_value is not None and value < min_value:
            print(f"Value must be at least {min_value}.")
        elif max_value is not None and value > max_value:
            print(f"Value must be at most {max_value}.")
        else:
            return value


def confirm(prompt):
    """Ask a yes/no question. Returns True for yes."""
    while True:
        answer = input(prompt + " (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please type y or n.")
