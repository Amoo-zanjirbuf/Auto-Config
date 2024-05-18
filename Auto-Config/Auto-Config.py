from core import special, cls, clientDownload, VPNDownload, turorial, ac, serverList, IPV4
from colorama import Fore, init
from time import sleep
import os

init(autoreset=True)

cyan = Fore.CYAN
plus = f"{Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.LIGHTYELLOW_EX}"
err = f"{Fore.RED}[-]{Fore.LIGHTYELLOW_EX}"

antiCheat = "if u can see this in console please DM me \"Amoo_zanjirbuf\""

try:
    os.remove("requirements.py")
except:
    pass

cls()

while True:
    try:
        command = int(input(f"{plus} Auto-Config>{cyan} "))

        if command == 1:
            antiCheat = "Polar"
            ac(antiCheat=antiCheat, command=command)
        elif command == 2:
            antiCheat = "Intave"
            ac(antiCheat=antiCheat, command=command)
        elif command == 3:
            antiCheat = "Grim"
            ac(antiCheat=antiCheat, command=command)
        elif command == 4:
            antiCheat = "NCP"
            ac(antiCheat=antiCheat, command=command)
        elif command == 5:
            antiCheat = "Vulcan"
            ac(antiCheat=antiCheat, command=command)
        elif command == 6:
            antiCheat = "Verus"
            ac(antiCheat=antiCheat, command=command)      
        elif command == 7:
            antiCheat = "Matrix"
            ac(antiCheat=antiCheat, command=command)
        elif command == 8:
            antiCheat = "AGC"
            ac(antiCheat=antiCheat, command=command)
        elif command == 9:
            antiCheat = "Watchdog"
            ac(antiCheat=antiCheat, command=command)
        elif command == 10:
            antiCheat = "Sentinel"
            ac(antiCheat=antiCheat, command=command)
        elif command == 11:
            antiCheat = "Negativity"
            ac(antiCheat=antiCheat, command=command)
        elif command == 12:
            antiCheat = "AAC"
            ac(antiCheat=antiCheat, command=command)
        elif command == 13:
            clientDownload()
        elif command == 14:
            VPNDownload()
        elif command == 15:
            turorial()
        elif command == 16:
            special()
        elif command == 17:
            serverList()
        elif command == 18:
            IPV4()
        elif command == 0:
            print(f"{plus} No Way You Saw This :3")
            cls()
        elif command == 99:
            cls()
            print(f"{plus} Exiting...")
            sleep(1)
            break
        else:
            print(f"{err} Unknown Option... ")
    except:
        print(f"{err} Something Went Wrong...")

Fore.RESET

exit()