class Server:
    def __init__(self, hostname, ip, status):
        self.hostname = hostname
        self.ip = ip
        self.status = status

    def reboot(self):
        print(f"Server->{self.hostname} has been rebooted")

    def ipcheck(self):
        print(f"Server->{self.hostname} has a ip address of {self.ip}")

    def check_health(self):
        print(f"Server->{self.hostname} status is {self.status}")

s1 = Server("LunchRoom", 10.0, "active")
s2 = Server("ClassRoom", 10.1, "inactive")
s3 = Server("BathRoom", 10.2, "maintenance")

servers = [s1, s2, s3]

for server in servers:
    server.reboot()
    server.ipcheck()
    server.check_health()


