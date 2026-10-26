import socket
import requests
import datetime
import threading

class PortScanner:
    def __init__(self, target_ip):
        self.target_ip = target_ip

    def check_port(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        try:
            s.connect((self.target_ip, port))
            print(f"🟢 Порт {port} ОТКРЫТ!")
        except:
            pass
        s.close()

    def scan_range(self, ports_list):
        print(f"\n🔍 Сканирую {self.target_ip}...")
        start_time = datetime.datetime.now()

        threads = []

        for port in ports_list:
            t = threading.Thread(target=self.check_port, args=(port,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()
        end_time = datetime.datetime.now()
        print(f"⏱️ Сканирование завершено в {end_time.strftime('%H:%M:%S')}")

class SiteRecon():
    def __init__(self, url):
        self.url = url

    def analyze(self):
        print(f"🕒 Время проверки: {datetime.datetime.now().strftime('%H:%M:%S')}")
        try:
            response = requests.get(self.url, timeout=3)
            print(f"Статус: {response.status_code}")
            server = response.headers.get("Server", "Неизвестно")
            print(f"Сервер: {server}")
            hsts = response.headers.get("Strict-Transport-Security", "Неизвестно")
            if hsts != "Неизвестно":
                print("✅ HSTS присутствует")
            else:
                print("⚠️ HSTS отсутствует (уязвимость!)")
        except:
            print("Ошибка подключения!")
