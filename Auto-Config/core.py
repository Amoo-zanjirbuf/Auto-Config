from colorama import Fore, init
from time import sleep
import webbrowser
import socket
import os

red = Fore.RED
yellow = Fore.LIGHTYELLOW_EX
cyan = Fore.CYAN
green = Fore.GREEN
plus = f"{red}[{green}+{red}]{yellow}"
err = f"{red}[-]{yellow}"

antiCheat = "No Anti-Cheat Is Chosen" # Anti-Cheat
pop = "None" # Best Paid Option
fop = "None" # Best Free Option
about = "Something Went Wrong..." # About AC
popConfig = "" # Paid Client Config
fopConfig = "" # Free Client Config


svList = f"""
{plus} POLAR
{plus} \tPikaNetwork - Polar
{plus} \tJartexNetwork - Polar
{plus} \tHycraft - Polar
{plus} \tCraftPlay - Polar
{plus} \tLuckynetwork - Polar
{plus} \tUniversocraft (Pit) - Polar
{plus} \tGamster (bw) - Polar
{plus} \tTrexMine - Polar
{plus} \tMadCraft - Polar
{plus} INTAVE
{plus} \tMineblaze - Inatve + Matrix
{plus} \tCheatmine - Intave + Matrix
{plus} \tDexland - Intave + Matrix
{plus} \tGommeHD - Intave
{plus} \tMineberry - Intave
{plus} \tLunaMC - Intave
{plus} \tHypeMC - Intave
{plus} GRIM
{plus} \tMineStar.pl - Grim + Vulcan
{plus} \tRapy.pl - Grim + Vulcan
{plus} \tUniversocraft - Grim + Vulcan
{plus} \tHylex - Grim
{plus} \tZonecraft - Grim
{plus} \tnssv.pl - Grim
{plus} \tAeon - Grim
{plus} \tZenticc - Grim
{plus} \tTwerion - Grim
{plus} \t3fmc - Grim
{plus} \tHerobrine - Grim
{plus} \tHoplite.gg - Grim
{plus} \tMineMalia - Grim
{plus} VULCAN
{plus} \tJartexNetwork (practice) - OldVulcan
{plus} \tSuperCraft - Vulcan + NCP (only scaffold checks)
{plus} \tGhostly - Vulcan
{plus} \tGodSpunky - Vulcan
{plus} \tPurplePrison - Vulcan
{plus} \tRedesky - Vulcan
{plus} \tMadCraft (Kitpvp) - Vulcan
{plus} \tTeamholy.de - Vulcan
{plus} \tMineLatino - Vulcan
{plus} \tRegorLand - Vulcan
{plus} VERUS
{plus} \tLibrecraft - Verus + OldNCP
{plus} \tColdPVP - Spike (Verus)
{plus} \tBlocksMC - Verus + UNCP
{plus} \tLibrecraft (LuckyWars) - Verus
{plus} NCP
{plus} \tBlockDrop - UNCP
{plus} MATRIX
{plus} \tacmc - Matrix + Vulcan
{plus} \tVoidpixel - Latest Matrix (Intave on some lobby's)
{plus} OTHER
{plus} \tMMC - AGC
{plus} \tHypixel - Watchdog
{plus} \tCubeCraft (Java/Bedrock) - Sentinel
{plus} \tPVP.land - LandBOT
{plus} \tEstaland - Karhu + Vulcan
{plus} \tMushmc - Negativity V2 + Custom
{plus} \tHive (Bedrock) - Flareon
{plus} \tGamster - Venus (Custom Grim)
{plus} \tFlameMC - No anticheat
{plus} \tNethergames (Bedrock) - Radon
{plus} \tLifeBoat (Bedrock) - Custom
{plus}{red} NOTICE : THIS LIST MIGH BE A BIT OUTDATED PLEASE DM ME ON DISCORD IF IT NEEDS ANY CHANGES OR YOU WANT TO ADD A SERVER TO IT
"""

Tutorial = f"""{yellow}
    _____________________
    |{red}[{green}0{red}]{yellow} Clear           |
    |{red}[{green}1{red}]{yellow} Ip Ban Bypass   |
    |{red}[{green}2{red}]{yellow} Vulcan Force-OP |
    |{red}[{green}9{red}]{yellow} Main Menu       |
    |____________________|

"""

clientList = f"""{yellow}
    _____________________________________
    |{plus} FREE:            {plus}  PAID:     |
    |{red}[{green}0{red}]{yellow} Clear            {red}[{green}6{red}]{yellow}  Augustus  |
    |{red}[{green}1{red}]{yellow} LiquidBounce     {red}[{green}7{red}]{yellow}  Rise      |
    |{red}[{green}2{red}]{yellow} CrossSine        {red}[{green}8{red}]{yellow}  Moon      |
    |{red}[{green}3{red}]{yellow} NightX           {red}[{green}9{red}]{yellow}  NurSultan |
    |{red}[{green}4{red}]{yellow} FDP              {red}[{green}10{red}]{yellow} Adapt     |
    |{red}[{green}5{red}]{yellow} Impact           {red}[{green}99{red}]{yellow} Main Menu |
    |____________________________________|

"""

def cls():
    os.system("cls")
    gui = f"""{yellow}
    _________________________________________________________________
    |{red}[{green}0{red}]{yellow} Clear       {red}[{green}5{red}]{yellow} Vulcan     {red}[{green}10{red}]{yellow} Sentinel   {red}[{green}15{red}]{yellow} Tutorials   |
    |{red}[{green}1{red}]{yellow} Polar       {red}[{green}6{red}]{yellow} Verus      {red}[{green}11{red}]{yellow} Negativity {red}[{green}16{red}]{yellow} Special     |
    |{red}[{green}2{red}]{yellow} Intave      {red}[{green}7{red}]{yellow} Matrix     {red}[{green}12{red}]{yellow} AAC        {red}[{green}17{red}]{yellow} AC List     |
    |{red}[{green}3{red}]{yellow} Grim        {red}[{green}8{red}]{yellow} AGC        {red}[{green}13{red}]{yellow} Clients    {red}[{green}18{red}]{yellow} IPV4 Finder |
    |{red}[{green}4{red}]{yellow} NCP         {red}[{green}9{red}]{yellow} Watchdog   {red}[{green}14{red}]{yellow} VPN        {red}[{green}99{red}]{yellow} Exit        |
    |________________________________________________________________|


{plus} Made With {red}<3 {yellow}BY :{red} Amoo_zanjirbuf
{plus} Version : {red}0.1
    """
    print(gui)

def special():
    cls()
    special = f"""{yellow}
    _______________
    |{red}[{green}0{red}]{yellow} Clear     |
    |{red}[{green}1{red}]{yellow} BlocksMC  |
    |{red}[{green}2{red}]{yellow} Karhu     |
    |{red}[{green}3{red}]{yellow} Sparky    |
    |{red}[{green}9{red}]{yellow} Main Menu |
    |______________|

    """
    print(special)
    while True:
        command = int(input(f"{plus} Auto-Config>{cyan} "))
        if command == 0:
            cls()
            print(special)
        elif command == 1:
            antiCheat = "NCP + Verus"
            ac(antiCheat=antiCheat, command=69420)
        elif command == 2:
            antiCheat = "Karhu"
            ac(antiCheat=antiCheat, command=69420)
        elif command == 3:
            antiCheat = "Sparky"
            ac(antiCheat=antiCheat, command=69420)
        else:
            cls()
            break

def clientDownload():
    cls()
    print(clientList)
    while True:
        command = int(input(f"{plus} Auto-Config>{cyan} "))
        if command == 0:
            cls()
            print(clientList)
        elif command == 1:
            webbrowser.open("https://liquidbounce.net/download")
        elif command == 2:
            webbrowser.open("https://github.com/shxp3/CrossSine/releases")
        elif command == 3:
            webbrowser.open("https://github.com/Aspw-w/NightX-Client/releases")
        elif command == 4:
            webbrowser.open("https://github.com/SkidderMC/FDPClient/releases")
        elif command == 5:
            webbrowser.open("https://impactclient.net/#download")
        elif command == 6:
            webbrowser.open("https://spezz.exchange/store/store/product/191-augustus-client-lifetime/")
        elif command == 7:
            webbrowser.open("https://riseclient.com/")
        elif command == 8:
            webbrowser.open("https://moonx.gg/#pricing")
        elif command == 9:
            webbrowser.open("https://nursultan.fun/products")
        elif command == 10:
            print(f"{err} You Can't Buy Adapt Anymore :(")
        else:
            cls()
            break

def VPNDownload():
    cls()
    print(f"{plus} Name: Soft Ether")
    print(f"{plus} Free: Yes")
    print(f"{plus} Hypixel Bypass: Yes(Not Recommended)")
    print(f"{plus} BlocksMC Bypass: Yes")
    open = input(f"{plus} Do You Want To Download? [y/n] \n>{cyan}").lower().strip()
    if open == "y":
        webbrowser.open("https://www.softether.org/5-download")
    else:
        pass
    cls()

def turorial():
    cls()
    print(Tutorial)
    while True:
        command = int(input(f"{plus} Auto-Config>{cyan} "))
        if command == 0:
            cls()
            print(Tutorial)
        elif command == 1:
            webbrowser.open("https://www.youtube.com/watch?v=VFAI5g5QOzA")
            sleep(18)
            webbrowser.open("https://www.youtube.com/watch?v=yXmr3mW7Vr8")
        elif command == 2:
            webbrowser .open("https://www.youtube.com/watch?v=lv1mCT8cR04")
        else:
            cls()
            break

def ac(antiCheat, command):
    cls()
    if antiCheat == "Polar":
        pop = "Augustus"
        fop = "LiquidBounce"
        about = "Polar Is A Very Good AntiCheat With Good Support Owned By \"Lucky\" This Anti Cheat Is Really Hard To Bypass, But Sometimes A New Fly Or Disabler Will Be Released. Augustus Is Around 80$ I'm Pretty Sure. Augustus Is Really Expensive But It Can Bypass Every Anti-Cheat Flawlessly. But If You Want A Good Free Client LiquidBounce Can Bypass Too"
    elif antiCheat == "Intave":
        pop = "Augustus"
        fop = "LiquidBounce"
        about = "Intave Is A Good AntiCheat With Good Support Owned By \"Richy\" This Anti Cheat Is Decently Hard To Bypass, But Sometimes A New Fly Will Be Released. Augustus Is Around 80$ I'm Pretty Sure. Augustus Is Really Expensive But It Can Bypass Every Anti-Cheat Flawlessly. But If You Want A Good Free Client LiquidBounce Can Bypass Too"
    elif antiCheat == "Grim":
        pop = "Nursultan"
        fop = "LiquidBounce"
        about = "Grim Is A Decent Free AntiCheat With Not That Good Support Team Owned By I Think \"MWHunter\" This Anti Cheat Is Not That Hard To Bypass, And4 Sometimes A New Fly Or Disabler Will Be Released. Nursultan Is Around 15$ For Lifetime Access. Nursultan Is Really Cheap But It's Mostly Used For Grim Anti-Cheat And It Can Bypass Flawlessly. But If You Want A Good Free Client LiquidBounce Can Bypass Too And Its Really Good"
    elif antiCheat == "NCP":
        pop = "Rise"
        fop = "CrossSine"
        popConfig = "https://workupload.com/file/EbKLUDNy3X4"
        fopConfig = "https://workupload.com/file/HMgpqMdqafu"
        about = "NCP Is A Decent Free AntiCheat With Not That Good Support Team Owned By \"asofold\" This Anti Cheat Is Not That Hard To Bypass, But Sometimes A New Fly Will Be Released And Usually Takes A Long Time To Be Fixed. Rise Is Around 25$. Rise Is Not That Expensive And It Can Bypass Many Anti-Cheats Flawlessly. But If You Want A Good Free Client CrossSine Can Bypass Too And Its Really Good"
    elif antiCheat == "Vulcan":
        pop = "Moon"
        fop = "FDP"
        popConfig = "https://workupload.com/file/qyGfBE3xtXr"
        fopConfig = "https://workupload.com/file/g7KVt8rzhbZ"
        about = f"Vulcan Is A Terrible Anti-Cheat With Awful Support Team, This Anti Cheat Is Very Easy To Bypass, And Sometimes A New Fly And Full Disabler Will Be Released. Moon Is Around 20€. Moon Is Not That Expensive And It Can Bypass Some Anti-Cheats Flawlessly, Moon Has A Fast Fly. But If You Want A Good Free Client FDP Can Bypass Too And Its Good.\n\n{plus} NOTICE :{red} This Anti-Cheat Has A Critical Exploit In The Version 2.8.3 And Older Which Allow Player To Gain Access To Vulcan Gui From There They Can Disable And Enable Every Check Or Set New Punishment Commands You Can Abuse That To Gain Full Access To Every Command."
    elif antiCheat == "Verus":
        pop = "Rise"
        fop = "FDP"
        about = "Verus Is One Of The Worst Anti-Cheat With Awful Support Team And A High Price, This Anti Cheat Is Super Easy To Bypass,  And There Is More Than 10 Full Disablers, In Fact Verus Is So Bad That It Doesn't Even Worth The Time To Code A New Working Fly And Client Developers Just Make A Full Disabler. Rise Is Around 25$. Rise Is Not That Expensive And It Can Bypass Many Anti-Cheats Flawlessly, Rice Has A Full Disabler For Verus. But There Is No Point Of Buying It For Verus, You Can Disable it With FDP And Many More Clients."
    elif antiCheat == "Matrix":
        pop = "Rise"
        fop = "LiquidBounce"
        about = "Matrix Is A Good Anti-Cheat With Decent Support Team, This Anti-Cheat Was Easy To Bypass But After Pika And Jartex Stoped Using Matrix No One Care About Matrix And Only Few Servers Use It So There Is Not Many Bypasses I Don't Recommend Cheating On Matrix, Also Matrix Has One Of The Best Scaffold Checks But It False Flags A LOT."
    elif antiCheat == "AGC":
        pop = "Rise \ Moon"
        fop = "LiquidBounce"
        about = "AGC Is A Decent(Not That Good) Anti-Cheat, This Anti-Cheat Is Not That Hard To Bypass AGC Is The Anti-Cheat That Minemen Club(MMC) Uses, Recently There Was A Masive Leak In MMC Which Made The Whole Anti-Cheat To Be Fcked. Rise Is 25$ And Moon Is 20 Euros I Recomend Rise If You Want To Cheat On Other Anti-Cheats And Moon If You Want To Chat On Vulcan. And If You Don't Want To Pay LiquidBounce Is Always There."
    elif antiCheat == "Watchdog":
        pop = "Adapt"
        fop = "LiquidBounce"
        about = "Watchdog Is The Anti-Cheat That Hypixel Uses Its Not That Good, If You Want To Pay You Can Buy Adapt For The Price Tag OF 20$ But Adapt Is Only Good For Hypixel, But You Can Just Use LiquidBounce Or FDP, I Recommend LiquidBounce."
    elif antiCheat == "Sentinel":
        pop = "None"
        fop = "LiquidBounce"
        about = "Sentinel Is The Anti-Cheat That CubeCraft Uses Its Not That Good I Just Recommend Use LiquidBounce It Has A Working Fly And Others, "
    elif antiCheat == "Negativity":
        pop = "None"
        fop = "LiquidBounce"
        about = "Oh Boy Negativity, By Far The Woest Anti-Cheat Ever Created By Man This Anti-Cheat Doesn't Detect Shit And You Can COMPLETELY DISABLE It Using ONLY PING SPOOF If You Have A High Ping This Anti-Cheat Will Completely Ignore You."
    elif antiCheat == "AAC":
        pop = "None"
        fop = "FDP"
        about = "AAC Is A Decent Anti-Cheat With No Support Because Its Been Discontinued Long Time Ago Almost No Server Uses it, If You Want To Cheat On It For Some Reason, Just Use FDP"
    elif antiCheat == "Karhu":
        pop = "None"
        fop = "FDP"
        about = "Karhu Is A Bad Anti-Cheat That No One Use Just Use FDP And Try Your Best To Bypass It Thats It"
    elif antiCheat == "Sparky":
        pop = "Rise"
        fop = "CrossSine"
        about = "One Of My Favorites I Have Some Private Fly Bypasses And I Can Share Some With You DM Me On Discord My ID Is \"Amoo_zanjirbuf\" Also CrossSine Is Way Better For Sparky Don't Buy Rise."
    elif antiCheat == "NCP + Verus":
        pop = "Rise"
        fop = "CrossSine \ LiquidBounce"
        about = "So BMC Huh? BMC Is Really Fun To Cheat On But You Will Get Banned After Each Match There Is Staff 24/7 Watching. You Can Use Rise, Its Good But Don't Spend Your Money CrossSine And LiquidBounce Is Just As Good(I Recommend LiquidBounce)."
    else:
        print(f"{err} How The Fuck?")

    configGUI = f"""{yellow}
    _________________________________________
    {red}[{green}0{red}]{yellow} Clear                               
    {red}[{green}1{red}]{yellow} Download Config For {pop}   
    {red}[{green}2{red}]{yellow} Download Config For {fop}          
    {red}[{green}9{red}]{yellow} Main Menu                           
    ________________________________________
    """
    cls()
    print(f"\n{plus} Anti Cheat: {red}{antiCheat}")
    print(f"\n{plus} Best Paid Client: {red}{pop}")
    print(f"\n{plus} Best Free Client: {red}{fop}")
    print(f"\n{plus} Info: {red}{about}\n")

    if command == 5:
        YouTube = input(f"{plus} Do You Want To Learn More? [y/n] \n>{cyan}").strip().lower()
        if YouTube == "y":
            webbrowser.open("https://www.youtube.com/watch?v=lv1mCT8cR04")
        else:
            pass

    if command == 8:
        gigaleack = input(f"{plus} Do You Want To Download MinemenClub-GigaLeack-2024.7z? [y/n] \n>{cyan}")
        if gigaleack == "y":
            webbrowser.open("https://www.mediafire.com/file/efoynso3j0y1422/MinemenClub-GigaLeack-2024.7z/file")
        else:
            pass

    
    print(configGUI)
    while True:
        config = int(input(f"{plus} Config-DownLoad>{cyan} "))
        if config == 0:
            cls()
            print(configGUI)
        elif config == 2 and fop == "LiquidBounce":
            print(f"{plus} Type .config load <Anti-Cheat Name / Server Name>")
        elif config == 1 and pop == "Augustus":
            print(f"{plus} Use Online Configs...")
        elif config == 1 and pop == "Nursultan":
            print(f"{err} No Config Available For NurSultan...")
        elif config == 1 and antiCheat == "Watchdog":
            print(f"{err} You Can't Buy Adapt Anymore...")
        elif config > 0 and config < 3 and antiCheat == "Verus":
            print(f"{plus} Just Use Disabler Mode Verus And You Can Vanilla Fly...")
        elif config > 0 and config < 3 and antiCheat == "Matrix":
            print(f"{err} No Config For Matrix Anti-Cheat Is Currently Available...")
        elif config > 0 and config < 3 and antiCheat == "AGC":
            print(f"{plus} Use MineMen Online Config...")
        elif config > 0 and config < 3 and antiCheat == "Negativity":
            print(f"{plus} Use Ping Spoof To Disable Negativity...")
        elif config > 0 and config < 3 and antiCheat == "AAC":
            print(f"{err} No Config Is Available For AAC Anti-Cheat...")
        elif config > 0 and config < 3 and antiCheat == "Karhu":
            print(f"{err} No Config Is Available For Karhu Anti-Cheat...")
        elif config > 0 and config < 3 and antiCheat == "Sparky":
            print(f"{plus} DM \"Amoo_zanjirbuf\" On Discord Get Some Fly Methods...")
        elif antiCheat == "NCP + Verus":
            print(f"{err} Soon...")
        elif config == 1:
            webbrowser.open(popConfig)
        elif config == 2:
            webbrowser.open(fopConfig)
        elif config == 9:
            cls()
            break
        else:
            continue

def serverList():
    cls()
    print(svList)

def IPV4():
    cls()
    minecraft_server = input(f"{plus} Enter Your Server Address :{cyan} ")
    try:
        ipv4_address = socket.gethostbyname(minecraft_server)
        print(f"{plus} The IPv4 address for {minecraft_server} is:{red} {ipv4_address}")
    except socket.gaierror as e:
        print(f"{err} Error: {red}{e}")