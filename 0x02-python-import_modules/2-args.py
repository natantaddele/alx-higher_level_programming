#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    args = sys.argv[1:]
    num_args = len(args)

    print(f"Number of argument(s): {num_args}", end="")
    if num_args == 0:
        print(".")
    elif num_args == 1:
        print(f", argument: {args[0]}.")
    else:
        print(", arguments:", end="")
        for i, arg in enumerate(args):
            print(f"\n{i + 1}: {arg}")

