import os
import time
import sys
import ctypes
from colorama import init, Fore, Style

init(autoreset=True)

os.system("title VanGuard Control (BY HJCS_HC)")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    if not is_admin():
        script = os.path.abspath(sys.argv[0])
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, f'"{script}"', None, 1
        )
        sys.exit()

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


ascii_art = r"""
██    ██  █████  ███    ██  ██████  ██    ██  █████  ██████  ██████       ██████  ██████  ███    ██ ████████ ██████   ██████  ██      
██    ██ ██   ██ ████   ██ ██       ██    ██ ██   ██ ██   ██ ██   ██     ██      ██    ██ ████   ██    ██    ██   ██ ██    ██ ██      
██    ██ ███████ ██ ██  ██ ██   ███ ██    ██ ███████ ██████  ██   ██     ██      ██    ██ ██ ██  ██    ██    ██████  ██    ██ ██      
 ██  ██  ██   ██ ██  ██ ██ ██    ██ ██    ██ ██   ██ ██   ██ ██   ██     ██      ██    ██ ██  ██ ██    ██    ██   ██ ██    ██ ██      
  ████   ██   ██ ██   ████  ██████   ██████  ██   ██ ██   ██ ██████       ██████  ██████  ██   ████    ██    ██   ██  ██████  ███████ 
                                                                                                                                      
     Vanguard Control  - by HJCS_HC
"""

def print_ascii():
    print(Fore.BLUE + Style.BRIGHT + ascii_art + Style.RESET_ALL)

def start_vangard():
    slow_print("Starting Vanguard services...")
    os.system("net start vgk")
    os.system("net start vgc")
    slow_print("Vanguard services should be started (if installed correctly).")

def stop_vangard():
    slow_print("Stopping Vanguard services...")
    os.system("net stop vgc")
    os.system("net stop vgk")
    slow_print("Vanguard services stopped.")

def uninstall_vangard():
    slow_print("Uninstalling Vanguard completely...")
    os.system("sc stop vgc")
    os.system("sc stop vgk")
    os.system("sc delete vgc")
    os.system("sc delete vgk")
    os.system("rmdir /S /Q \"C:\\Program Files\\Riot Vanguard\"")
    slow_print("Vanguard uninstalled. You should reboot your PC.")

def config_startup():
    clear_screen()
    print_ascii()
    print("""
[1] Enable Vanguard at Windows startup
[2] Disable Vanguard at startup
[3] Back to main menu
""")
    choice = input("Choose an option: ")
    if choice == "1":
        slow_print("Setting Vanguard to auto-start...")
        os.system("sc config vgk start= system")
        os.system("sc config vgc start= system")
        slow_print("Vanguard will now start automatically with Windows.")
    elif choice == "2":
        slow_print("Disabling Vanguard auto-start...")
        os.system("sc config vgk start= disabled")
        os.system("sc config vgc start= disabled")
        slow_print("Vanguard won't auto-start anymore.")
    else:
        return

    input("\nPress ENTER to return to menu...")

def main_men():
    while True:
        clear_screen()
        print_ascii()
        print("""
╔════════════════════════════════════════════════╗
║                MAIN MENU OPTIONS               ║
╠════════════════════════════════════════════════╣
║ 1. Start Vanguard                              ║
║ 2. Stop Vanguard                               ║
║ 3. Uninstall Vanguard                          ║
║ 4. Configure Vanguard startup behavior         ║
║ 5. Exit                                        ║
╚════════════════════════════════════════════════╝
""")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            start_vangard()
        elif choice == "2":
            stop_vangard()
        elif choice == "3":
            uninstall_vangard()
        elif choice == "4":
            config_startup()
        elif choice == "5":
            slow_print("Goodbye!", 0.05)
            sys.exit()
        else:
            slow_print("Invalid option, please try again.")

        input("\nPress ENTER to return to menu...")

if __name__ == "__main__":
    run_as_admin()
    main_men()
