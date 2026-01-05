import os
import platform

print("--- INFO SYSTEM ASHIKIN ---")
print("User: " + os.environ.get('USER', 'Tidak Ditemui'))
print("OS: " + platform.system())
print("Release: " + platform.release())
print("Directory: " + os.getcwd())

