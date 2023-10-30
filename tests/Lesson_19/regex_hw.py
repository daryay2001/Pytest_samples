import re

# 1 - В прикріпленому файлі (regex_hw.py) реалізувати пошукові патерни використовуючі regex
# (не використовуючи назви того що шукаємо)
#
# Результат виконання, це друк словника
# {'country': 'Ukraine', 'region': 'Lviv Region', 'city': 'Stebnyk', 'postal': '82172',
# 'address': 'str. Doroshenko, 1', 'deadline': '31.12.2023'}

my_string = ("Place of delivery of goods or place of performance of work or provision"
             " of services: 82172, Ukraine, Lviv Region, Stebnyk, str. Doroshenko, 1 Deadline"
             " for delivery of goods, performance of works or provision of services: 31.12.2023")

if __name__ == '__main__':
    data = {
        'country': re.search(r'U[a-z]+e', my_string).group(),
        'region': re.search(r'L[a-z]+\sR[a-z]{5}', my_string).group(),
        'city': re.search(r'S[a-z]+k', my_string).group(),
        'postal': re.search(r'\d{5}', my_string).group(),
        'address': re.search(r'(?P<address>(?P<str_name>\w{3}\.\s[A-Z][a-z]+,)(?P<house_numb>\s1))',
                             my_string).group(),
        'deadline': re.search(r'\d{2}.\d{2}.\d{4}', my_string).group(),
    }
    print(data)
