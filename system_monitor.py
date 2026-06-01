
#This script monitors the system's CPU, memory, disk usage, and uptime using the psutil library.
import psutil
import socket
import time


def get_stats():

    hostname = socket.gethostname()

    boot_time = psutil.boot_time()
    uptime_seconds = time.time() - boot_time

    return {
        "hostname": hostname,
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent,
        "uptime_hours": round(uptime_seconds / 3600, 2)
    }

import subprocess

status = subprocess.run(
    ["systemctl", "is-active", "--quiet", "sshd"],
    capture_output=True,
    text=True
)







