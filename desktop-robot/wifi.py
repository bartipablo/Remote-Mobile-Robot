import subprocess
import re


def get_wifi_signal_strength():
    result = subprocess.run(["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-I"], capture_output=True, text=True)
    output = result.stdout

    match = re.search(r"agrCtlRSSI:\s*(-?\d+)", output)
    if match:
        return int(match.group(1))
    else:
        return None
