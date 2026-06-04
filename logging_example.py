import logging

logging.basicConfig(filename="logging_example.txt",level="INFO", format="%(asctime)s - %(levelname)s - %(message)s")

class Server:
    def __init__(self, hostname, ip, status):
        self.hostname = hostname
        self.ip = ip
        self.status = status

    def __str__(self):
        return f"HOSTNAME:{self.hostname} | IP:{self.ip} | STATUS:{self.status}"

s1 = Server("LunchRoom", 10.0, "active")
s2 = Server("ClassRoom", 10.1, "inactive")
s3 = Server("BathRoom", 10.2, "maintenance")

logging.info(s1)
logging.info(s2)
logging.info(s3)

