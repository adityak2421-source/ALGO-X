history_records = []


def add_history(operation, details):
    record = f"{operation} | {details}"
    history_records.append(record)


def get_history():
    return history_records


def set_history(records):
    history_records.clear()
    history_records.extend(records)


def clear_history():
    history_records.clear()