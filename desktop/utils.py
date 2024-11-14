import socket
import subprocess
import re
from conf import RASPBERRYPI_IPv4
import platform


def get_wifi_signal_strength():
    system_platform = platform.system()

    if system_platform == "Darwin":
        result = subprocess.run(
            ["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-I"],
            capture_output=True, text=True
        )
        output = result.stdout
        match = re.search(r"agrCtlRSSI:\s*(-?\d+)", output)
        if match:
            return int(match.group(1))

    elif system_platform == "Linux":
        try:
            result = subprocess.run(["iwconfig"], capture_output=True, text=True)
            output = result.stdout
            match = re.search(r"Signal level=(-?\d+)", output)
            if match:
                return int(match.group(1))
        except FileNotFoundError:
            try:
                result = subprocess.run(["nmcli", "-t", "-f", "IN-USE,SIGNAL", "device", "wifi"], capture_output=True, text=True)
                output = result.stdout
                match = re.search(r"(\d+)$", output.strip())
                if match:
                    return int(match.group(1))
            except FileNotFoundError:
                return None

    elif system_platform == "Windows":
        try:
            result = subprocess.run(
                ["netsh", "wlan", "show", "interfaces"],
                capture_output=True, text=True
            )
            output = result.stdout
            match = re.search(r"Signal\s*:\s*(\d+)", output)
            if match:
                return int(match.group(1))
        except FileNotFoundError:
            return None

    return None


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((RASPBERRYPI_IPv4, 80))
    addr = s.getsockname()[0]
    s.close()
    return addr
