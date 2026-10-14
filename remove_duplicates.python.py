def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

numbers = [1, 2, 3, 2, 4, 3, 5]

print(remove_duplicates(numbers))