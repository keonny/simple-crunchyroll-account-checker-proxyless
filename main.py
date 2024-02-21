from api import Crunchyroll
import os

def main():
    os.system('cls')

    checker = Crunchyroll()

    f = input("your database file:\n")

    users = []

    os.system('cls')
    with open(f, 'r', encoding='utf=8') as f:
        for lines in set(map(str.strip, f.read().splitlines())):
            users.append(lines.split(":"))

    for user, senha in users:
        print(checker.request(user, senha))

if __name__ == "__main__":
    main()
        
        