import clipboard
import os
import signal
import sys
import time
from infi.systray import SysTrayIcon
from urllib.parse import urlparse

is_running = True


def signal_handler(sig, frame):
    is_running=False
    
def quit_now(systray):
    is_running=False

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    menu_options = (("Quit", None, quit_now),)
    systray = SysTrayIcon("./icon/Aha-Soft-Desktop-Halloween-Web.ico", "UrlCatcher", menu_options)
    systray.start()

    if not os.path.isdir("caught"):
        os.makedirs("caught")
    last_text=""
    while is_running:
        time.sleep(1)
        text = clipboard.paste()
        if(text!=last_text):
            if text.startswith("https:") or text.startswith("http:")or text.startswith("www."):
                parsed_uri = urlparse(text)
                result = '{uri.netloc}'.format(uri=parsed_uri)
                file_name=f"./caught/{result}.txt"
                with open(file_name, "a") as file:
                    file.write(text+"\n")
            last_text=text
        

