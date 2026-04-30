import requests
url = "https://raw.githubusercontent.com/Anasvirat18/Jio_mpd/refs/heads/main/jiotv.m3u"
r = requests.get(url)
content = r.text
lines = content.splitlines()
for i, line in enumerate(lines):
    if "4sites" in line:
        print(f"Line {i}: {line}")
        # Print surrounding lines
        for j in range(max(0, i-5), min(len(lines), i+5)):
            print(f"  {j}: {lines[j]}")
