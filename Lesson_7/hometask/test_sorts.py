import random

def test_sort(algo, reversal: bool = False):
    def array_gen(minimum: int, maximum: int, size: int) -> list:
        return [random.randint(minimum, maximum) for _ in range(size)]

    def compare_sorted(array):
        new_array = array.copy()
        algo(new_array)
        return sorted(array, reverse=reversal) == new_array

    print(("Not OK", "OK")[compare_sorted(array_gen(-100, 100, 10))])
    print(("Not OK", "OK")[compare_sorted(array_gen(-100, 100, 100))])
    print(("Not OK", "OK")[compare_sorted(array_gen(-100, 100, 1000))])
    print(("Not OK", "OK")[compare_sorted(array_gen(-100, 100, 10000))])
