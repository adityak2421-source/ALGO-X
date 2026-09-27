def reverse_array(arr):
    return arr[::-1]


def count_element(arr, target):
    count = 0

    for element in arr:
        if element == target:
            count += 1

    return count


def find_maximum(arr):
    if len(arr) == 0:
        return None

    maximum = arr[0]

    for element in arr:
        if element > maximum:
            maximum = element

    return maximum


def remove_duplicates(arr):
    result = []

    for element in arr:
        if element not in result:
            result.append(element)

    return result


def partition_array(arr, pivot):
    smaller = []
    greater_or_equal = []

    for element in arr:
        if element < pivot:
            smaller.append(element)
        else:
            greater_or_equal.append(element)

    return smaller + greater_or_equal


def kth_smallest(arr, k):
    if k < 1 or k > len(arr):
        return None

    sorted_arr = sorted(arr)

    return sorted_arr[k - 1]

if __name__ == "__main__":
    numbers = [5, 2, 8, 2, 1, 5]

   
