# Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
#  Примечания:
# - в сумму не включаем пустую строку и строку целиком;
# * задача считается решённой, если в коде использована
# функция вычисления хеша (hash(), sha1() или любая другая из модуля hashlib)

import hashlib
import sys

def test_substring_count(sub_func):
    print_res = lambda booltest: print("OK" if booltest else "Not OK")
    print_res(sub_func("") == 0)
    print_res(sub_func(" ") == 0)
    print_res(sub_func("dd") == 1)
    print_res(sub_func("ds") == 2)
    print_res(sub_func("d s") == 5)
    print_res(sub_func("d d") == 4)
    print_res(sub_func("da$") == 5)
    print_res(sub_func("dd$") == 4)
    print_res(sub_func("ddd") == 2)
    print_res(sub_func("daes") == 9)
    print_res(sub_func("da s") == 9)
    print_res(sub_func("dd s") == 8)
    print_res(sub_func("sd d") == 8)
    print_res(sub_func("ddds") == 6)
    print_res(sub_func("dddd") == 3)
    print_res(sub_func("adda") == 7)
    print_res(sub_func("adad") == 6)

def substring_count(string: str):
    unique_list = []
    get_hash = lambda stringg: hashlib.sha1(stringg.encode('utf-8')).hexdigest()
    str_len = len(string)
    if str_len == 0 or str_len == 1:
        return 0
    for i in range(str_len):
        for j in range(i+1, str_len+1):
            if i == 0 and j == str_len:
                continue
            substring = string[i:j]
            if not substring:
                continue
            string_hash = get_hash(substring)
#            if sys.getsizeof(substring) > sys.getsizeof(string_hash):
#                print("Yeeeee")
            if string_hash in unique_list:
                continue
            unique_list.append(string_hash)
    return len(unique_list)


test_substring_count(substring_count)
#print(substring_count("Avada kedavravrara Amadeulincamadeusliamad Avada kedavra"))

# На простых строках (типа как в тесте) нет экономии памяти. То ли дело сложные подстроки...