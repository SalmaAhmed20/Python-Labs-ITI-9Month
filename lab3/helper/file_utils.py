def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = []
            for line in file:
                lines.append(line)
            return lines
    except IOError:
        print("Something went wrong")


def append_file(file_path, content):
    try:
        with open(file_path, 'a') as file:
            file.write(content)
    except IOError:
         print("Something went wrong")


def write_file(filename, data):
    try:
        with open(filename, 'w') as f:
            f.write(data)
    except IOError:
         print("Something went wrong")