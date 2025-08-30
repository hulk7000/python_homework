import subprocess

websites = [
    "google.com",
    "youtube.com",
    "facebook.com",
    "twitter.com",
    "wikipedia.org",
    "hoefhef.com"
]

def ping_website(host):
    try:
        # Use '-n' instead of '-c' on Windows
        output = subprocess.run(
            ["ping", "-n", "1", host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if output.returncode == 0:
            print(f"[✅] {host} is reachable")
        else:
            print(f"[❌] {host} is not reachable")
    except Exception as e:
        print(f"[⚠️] Error pinging {host}: {e}")

for site in websites:
    ping_website(site)
