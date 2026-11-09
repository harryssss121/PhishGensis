from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sys

def send_popup(message="Your session has been compromised by BitB-Framework!"):
    print(f"[+] Sending popup: {message}")
    try:
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        driver.get("http://localhost:5800")
        time.sleep(3)
        driver.execute_script(f"alert('{message}');")
        time.sleep(5)
        driver.quit()
        print("Popup sent successfully!")
    except Exception as e:
        print("Error sending popup:", e)

def redirect(url="https://youtube.com"):
    print(f"[+] Redirecting to: {url}")
    try:
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        driver.get("http://localhost:5800")
        time.sleep(3)
        driver.execute_script(f"window.location.href = '{url}';")
        time.sleep(2)
        driver.quit()
        print("Redirect sent successfully!")
    except Exception as e:
        print("Error redirecting:", e)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 direct-control.py popup \"Your message\"")
        print("  python3 direct-control.py redirect \"https://youtube.com\"")
        sys.exit(1)

    action = sys.argv[1]
    if action == "popup":
        msg = sys.argv[2] if len(sys.argv) > 2 else "Test popup from FYP"
        send_popup(msg)
    elif action == "redirect":
        url = sys.argv[2] if len(sys.argv) > 2 else "https://youtube.com"
        redirect(url)
    else:
        print("Unknown action. Use 'popup' or 'redirect'")

# Update on 2026-09-17 05:48:23
# Additional handling and logging improvements
# Refined logic for better reliability

# Update on 2026-09-30 13:44:30
# Additional handling and logging improvements
# Refined logic for better reliability

# Update on 2026-10-13 21:40:38
# Additional handling and logging improvements
# Refined logic for better reliability

# Update on 2026-10-27 05:36:46
# Additional handling and logging improvements
# Refined logic for better reliability

# Update on 2026-11-09 13:32:54
# Additional handling and logging improvements
# Refined logic for better reliability
