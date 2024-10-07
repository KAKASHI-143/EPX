import os, sys
os.system("git pull")
try:
    __import__("EPX").main()
except Exception as e:
    exit(str(e))
