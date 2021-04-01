from typing import List, Any


def remove_duplicates(num: List[str]) -> List[str]:
    list_to_set = set(num)
    output_list = list(list_to_set)

    return output_list


numbers = [1, 23, 235, 12, 1, 1, 12]
print(numbers)

numbers = remove_duplicates(numbers)
print(numbers)
