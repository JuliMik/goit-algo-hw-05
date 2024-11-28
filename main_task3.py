import sys

from colorama import Fore


# Функція для парсингу рядків логу
def parse_log_line(line: str) -> dict:
    try:
        component = line.split()
        components_dict = {
            'date': ''.join(component[0]),
            'time': ''.join(component[1]),
            'level': ''.join(component[2]),
            'info': ''.join(component[3:])
        }

        return components_dict
    except Exception as e:
        print(Fore.RED + f'Error: {e}')


# Функція для завантаження логів з файлу
def load_logs(file_path: str) -> list:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return [parse_log_line(line.strip()) for line in file if line.strip()]
    except FileNotFoundError:
        print(Fore.RED + f"File {file_path} not found")


# Функція для фільтрації логів за рівнем
def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log['level'].upper() == level.upper(), logs))


# Функція для підрахунку записів за рівнем логування.
def count_logs_by_level(logs: list) -> dict:
    count_logs_dict = {}
    try:
        for log in logs:
            if log['level'] in count_logs_dict.keys():
                count_logs_dict[str(log['level'])] += 1
            else:
                count_logs_dict[str(log['level'])] = 1
        return count_logs_dict
    except Exception:
        ...


# Функція яка форматує та виводить результати
def display_log_counts(counts: dict):
    if len(counts) > 0:
        print(Fore.CYAN + f'''Рівень логування | Кількість
        ---------------|----------
        {list(counts.keys())[0]:15}| {counts[list(counts.keys())[0]]:<10} 
        {list(counts.keys())[1]:15}| {counts[list(counts.keys())[1]]:<10}
        {list(counts.keys())[2]:15}| {counts[list(counts.keys())[2]]:<10}
        {list(counts.keys())[3]:15}| {counts[list(counts.keys())[3]]:<10}
        ''')
    else:
        print(Fore.YELLOW + 'File is empty!')


def display_level_logs(logs: list, level: str):
    level = level.upper()
    logs_mark = 0
    print(f"\nДеталі логів для рівня '{level}':")
    for log in logs:
        if log['level'] == level:
            logs_mark = 1
            print(Fore.BLUE + f"{log['date']} {log['time']}- {log['info']}")
    if logs_mark == 0:
        print(Fore.BLUE + 'Logs not found!')



file_path = sys.argv[1]
display_log_counts(count_logs_by_level(load_logs(file_path)))
if len(sys.argv) > 2:
    display_level_logs(load_logs(file_path), sys.argv[2])

