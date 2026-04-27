import time
import sys

def send_popup(message="Your session has been compromised by BitB-Framework!"):
    print(f"[+] Sending popup: {message}")
    print("\nManual Step:")
    print("1. In Docker Firefox, press Ctrl+Shift+K to open Console")
    print("2. Paste this and press Enter:")
    print(f"   alert('{message}');")
    print("\nPress Enter in this terminal when done...")

def redirect(url="https://youtube.com"):
    print(f"[+] Redirecting to: {url}")
    print("\nManual Step:")
    print("1. In Docker Firefox, press Ctrl+L to focus address bar")
    print("2. Type the URL and press Enter:")
    print(f"   {url}")
    print("\nOr paste this in Console:")
    print(f"   window.location.href = '{url}';")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 simple-control.py popup \"Message\"")
        print("  python3 simple-control.py redirect \"URL\"")
        sys.exit(1)

    action = sys.argv[1]
    if action == "popup":
        msg = sys.argv[2] if len(sys.argv) > 2 else "Test popup from FYP"
        send_popup(msg)
    elif action == "redirect":
        url = sys.argv[2] if len(sys.argv) > 2 else "https://youtube.com"
        redirect(url)
    else:
        print("Unknown action")
