# Пользователь вводит данные о количестве предприятий, их наименования и
# прибыль за четыре квартала для каждого предприятия. Программа должна
# определить среднюю прибыль (за год для всех предприятий) и
# отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

import collections

companies_count = int(input("Введите количество предприятий "))

if companies_count < 0:
    quit()

# custom_dict = dict()
# так делать не стоит, так как найти и обработать ошибку проблематично
# но интересно!
custom_dict = collections.defaultdict(lambda: int(input("Введите выручку за 4 квартала ")))

for i in range(companies_count):
    while True:
        try:
            #    company_name = input("Введите название предприятия")
            #    company_profit = input("Введите выручку за 4 квартала ")
            custom_dict[input("Введите название предприятия ")]  # = company_profit
            break
        except ValueError:
            print("uncorrect input datatype. Try again")

sorted_dict = collections.OrderedDict(sorted(custom_dict.items()))
average_profit = sum(custom_dict.values()) / len(custom_dict)
print(f"Средняя прибыль за год составляет {average_profit}")


up_done, mid_done, down_done = [False], [False], [False]
mark_name = "Title mark"


def print_factory(mark: bool, title: str, name: str, bool_val: list):
    if mark:
        if not bool_val[0]:
            print(title)
            bool_val[0] = True
        print(name)


# порядок сохраняется!
for factory, profit in sorted_dict.items():
    print_factory(profit > average_profit, "Предприятия с прибылью выше среднего:", factory, up_done)
    print_factory(profit == average_profit, "Предприятия со средней прибылью:", factory, mid_done)
    print_factory(profit < average_profit, "Предприятия с прибылью ниже среднего:", factory, down_done)
