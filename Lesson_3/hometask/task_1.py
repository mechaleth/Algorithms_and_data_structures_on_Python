# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

numbers_array = [x for x in range(2, 100)]
counters_dict = {x: 0 for x in range(2, 10)}
# bonus
# values_dict = {x: [] for x in range(2, 10)}

for number in numbers_array:
    for key in counters_dict:
        if not number % key:
            counters_dict[key] += 1
            # bonus
            # values_dict[key].append(number)

for number, count in counters_dict.items():
    print(f"{number} встречается раз: {count}")
# bonus
# for key, value in values_dict.items():
#     print(key, value)