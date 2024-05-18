import os
import time

print("installing...")

os.system("python -m pip install colorama")

print("done...")

time.sleep(1)

os.system("python Auto-Config.py")

time.sleep(1)

exit()