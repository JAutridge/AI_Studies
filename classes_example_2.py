# --- SERVER CLASS ---
# A class is a blueprint for creating objects
# This class represents a server with basic management methods
class Server:

    # Constructor - runs automatically when a new Server object is created
    # Takes three arguments: hostname, ip, and status
    def __init__(self, hostname, ip, status):
        self.hostname = hostname  # Name of the server (e.g. "LunchRoom")
        self.ip = ip              # IP address of the server (e.g. 10.0)
        self.status = status      # Current status (e.g. "active", "inactive")

    # Method to simulate rebooting the server
    def reboot(self):
        print(f"Server->{self.hostname} has been rebooted")

    # Method to display the server's IP address
    def ipcheck(self):
        print(f"Server->{self.hostname} has a ip address of {self.ip}")

    # Method to display the server's current health/status
    def check_health(self):
        print(f"Server->{self.hostname} status is {self.status}")


# --- CREATING SERVER INSTANCES ---
# Each line creates a new Server object using the class blueprint above
s1 = Server("LunchRoom", 10.0, "active")       # Server 1 - active
s2 = Server("ClassRoom", 10.1, "inactive")     # Server 2 - inactive
s3 = Server("BathRoom", 10.2, "maintenance")   # Server 3 - maintenance


# --- STORING SERVERS IN A LIST ---
# Put all server objects into a list so we can loop through them easily
servers = [s1, s2, s3]


# --- LOOPING THROUGH ALL SERVERS ---
# For each server in the list, run all three methods
# This avoids having to call each method manually on every server
for server in servers:
    server.reboot()       # Reboot the server
    server.ipcheck()      # Check its IP address
    server.check_health() # Check its health status