def binary_search(array: list[int], target: int) -> int | None:
    min_array = 0
    max_array = len(array) - 1
    while min_array <= max_array:
        half = (max_array + min_array)//2
        if target == array[half]:
            return half
        elif target > array[half]:
            min_array = half + 1
        elif target < array[half]:
            max_array = half - 1
    return None
