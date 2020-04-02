import psutil
import socket
from time import sleep

THRESHOLD_PCT = 30
PAUSE_SECONDS = 15 * 60

host = socket.gethostname()

while True:
    mem = psutil.virtual_memory()
    available_pct = 100 * mem.available / mem.total
    if available_pct > THRESHOLD_PCT:
        print(f'{available_pct:.0f} % of memory available on {host}!')
    sleep(PAUSE_SECONDS)
