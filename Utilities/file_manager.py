def save_history(records, filename="data/history.txt"):
    with open(filename, "w") as file:
        for record in records:
            file.write(record + "\n")


def load_history(filename="data/history.txt"):
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]

    except FileNotFoundError:
        return []