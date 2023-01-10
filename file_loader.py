def get(filename):
    with open(filename, 'r') as file:
        contents = file.read()

    return contents