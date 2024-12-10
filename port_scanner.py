import socket

class Scanner:
    def __init__(self, ip):
        self.ip = ip
        self.open_ports = []

    def __str__(self):
        return 'Scanner(ip={})'.format(self.ip)
    
    def add_port(self, port):
        self.open_ports.append(port)

    def scan(self, lower, upper):
        for port in range(lower, upper + 1):
            if self.is_open(port):
                self.add_port(port)

    def is_open(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        try:
            result = s.connect_ex((self.ip, port))
        except socket.error:
            result = 1
        s.close()
        return result == 0

def main():
    ip = 'scanme.nmap.org'
    scanner = Scanner(ip)
    scanner.scan(1, 5000)
    print(scanner.open_ports)

if __name__ == '__main__':
    main()