import subprocess
import platform


# 1 - Створити метод який виводить в консоль пінг сайтів, як параметри функція отримує
# список сайтів(пінг яких треба перевірити) та кількість запитів як у прикладі.
# Метод універсальний відпрацьовує на будь якій ОС.

def ping_websites(websites_list, numb):
    system = platform.system()
    if system == "Windows":
        using_command = ["ping", "-n", str(numb)]
    elif system == "Linux" or "Darwin":  # For Linux and Mac
        using_command = ["ping", "-c", str(numb)]
    else:
        print("Unidentified OS")
        return

    for website in websites_list:
        using_command.append(website)
        print(f"Ping website {numb} times")
        try:
            result = subprocess.run(using_command, check=True, capture_output=True, text=True)
            print(result.stdout)
        except subprocess.CalledProcessError as error:
            print(f"Ping error: {error}")
        using_command.pop()  # Remove website to use next one


if __name__ == '__main__':
    websites = ["www.google.com", "rozetka.com.ua", "intertop.ua"]
    ping_numb = 3
    ping_websites(websites, ping_numb)
