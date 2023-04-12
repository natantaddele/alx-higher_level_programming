#!/usr/bin/python3
"""
This module contains a function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename: str = "") -> None:
    """
    Reads a text file (UTF8) and prints it to stdout

    Args:
        filename (str): name of the file to read (default "")

    Returns:
        None

    Raises:
        FileNotFoundError: if the file is not found
    """
    try:
        with open(filename, encoding="utf-8") as file:
            for line in file:
                print(line, end="")
    except FileNotFoundError:
        print(f"Error: File not found: {filename}")


if __name__ == "__main__":
    import doctest
    import os

    # Run the doctests in the README.md file
    doctest.testfile("README.md")

    # Run additional tests from files in the ./tests/ directory
    test_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tests")
    for test_file in os.listdir(test_dir):
        if test_file.endswith(".txt"):
            print(f"Running test from {test_file}")
            doctest.testfile(os.path.join(test_dir, test_file))

