from tools import PortScanner, SiteRecon, PasswordChecker

def main():
    while True:
        print("\n" + "="*30)
        print("🛡️  CYBER TOOLBOX v1.0")
        print("="*30)
        print("1. Сканер портов")
        print("2. Аудитор безопасности сайта")
        print("3. Проверка пароля")
        print("4. Выход")
        print("="*30)

        choice = input("Выбери (1-4): ")

        if choice == "1":
            ip = input("Введите IP: ")
            scanner = PortScanner(ip)
            scanner.scan_range([80, 443, 22, 135, 445])

        elif choice == "2":
            url = input("Введите URL: ")
            recon = SiteRecon(url)
            recon.analyze()

        elif choice == "3":
            pwd = input(("Введите пароль для проверки: "))
            checker = PasswordChecker()
            checker.check(pwd)

        elif choice == "4":
            print("Выход")
            break

if __name__ == "__main__":
    main()