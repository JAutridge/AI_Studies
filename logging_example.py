import logging

# --- LOGGING SETUP ---
# basicConfig sets up the logging system with:
# filename  = where to save the logs (logging_example.txt)
# level     = minimum level to log (INFO logs INFO, WARNING, ERROR, CRITICAL)
# format    = how each log line looks: timestamp - level - message
logging.basicConfig(
    filename="logging_example.txt",  # Saves logs to this file
    level="INFO",                     # Log everything at INFO level and above
    format="%(asctime)s - %(levelname)s - %(message)s"  # Log format
)


# --- SERVER CLASS ---
# Represents a server with a hostname, IP address, and status
class Server:

    # Constructor - runs every time a new Server object is created
    def __init__(self, hostname, ip, status):
        self.hostname = hostname  # Name of the server (e.g. "LunchRoom")
        self.ip = ip              # IP address of the server (e.g. 10.0)
        self.status = status      # Current status (e.g. "active", "inactive")

        # Create a logger specifically for the Server class
        # This logger is named "Server" and will appear in the log file
        self.logger = logging.getLogger("Server")

        # Log an INFO message every time a new server is created
        # This gets written to logging_example.txt automatically
        self.logger.info(
            f"Server {hostname} has been created | ip:{self.ip} | status:{self.status}"
        )

    # __str__ controls what prints when you print() a Server object
    def __str__(self):
        return f"HOSTNAME:{self.hostname} | IP:{self.ip} | STATUS:{self.status}"


# --- CREATING SERVER INSTANCES ---
# Each server creation automatically logs an INFO entry to the file

s1 = Server("LunchRoom", 10.0, "active")       # Logs: Server LunchRoom has been created
s2 = Server("ClassRoom", 10.1, "inactive")     # Logs: Server ClassRoom has been created
s3 = Server("BathRoom", 10.2, "maintenance")   # Logs: Server BathRoom has been created