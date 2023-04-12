def read_file(filename=""):
    contents = ""
    if filename:
        with open(filename) as file:
            contents = file.read()
    return contents
