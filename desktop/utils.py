import socket
import subprocess
import re
from conf import RASPBERRYPI5_IP


def get_wifi_signal_strength():
    result = subprocess.run(["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-I"], capture_output=True, text=True)
    output = result.stdout

    match = re.search(r"agrCtlRSSI:\s*(-?\d+)", output)
    if match:
        return int(match.group(1))
    else:
        return None


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((RASPBERRYPI5_IP, 80))
    addr = s.getsockname()[0]
    s.close()
    return addr
