def list_operations(numbers):
    result = {}

    result["length"] = len(numbers)
    result["first_element"] = numbers[0] if numbers else None
    result["last_element"] = numbers[-1] if numbers else None

    return result


def tuple_operations(numbers):
    data = tuple(numbers)

    return {
        "tuple": data,
        "length": len(data),
        "first_element": data[0] if data else None,
        "last_element": data[-1] if data else None
    }


def set_operations(numbers):
    data = set(numbers)

    return {
        "set": data,
        "unique_count": len(data)
    }


def dictionary_operations(numbers):
    frequency = {}

    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1

    return frequency


if __name__ == "__main__":
    numbers = [2, 4, 2, 7, 4, 9]

    print("List:", list_operations(numbers))
    print("Tuple:", tuple_operations(numbers))
    print("Set:", set_operations(numbers))
    print("Dictionary:", dictionary_operations(numbers))
