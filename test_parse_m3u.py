import requests
import re
import json

url = "https://raw.githubusercontent.com/Anasvirat18/Jio_mpd/refs/heads/main/jiotv.m3u"
try:
    response = requests.get(url, timeout=10)
    lines = response.text.splitlines()
    print("Fetched nicely. Total lines:", len(lines))
except Exception as e:
    print("Failed to fetch via original URL:", e)
    url = "https://cdn.jsdelivr.net/gh/Anasvirat18/Jio_mpd@main/jiotv.m3u"
    response = requests.get(url)
    lines = response.text.splitlines()
    print("Fetched via proxy. Total lines:", len(lines))

count = 0
current_key_id = "default_id"
current_key = "default_key"

for line in lines[800:1000]:  # Check a specific range
    line = line.strip()
    if not line: continue
    if 'adaptive.license_key=' in line:
        print("KEY:", line)
    elif line.startswith("https://"):
        print("URL:", line)
        print("----")
    elif line.startswith("#EXTINF"):
        print("INF:", line)
    else:
        # print("OTH:", line)
        pass
            