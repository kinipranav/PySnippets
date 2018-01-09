from datetime import datetime
import os

print (datetime.now())
with open("c:/Users/xyz/Desktop/bigFile.txt", "wb") as dump:
  dump.truncate(1024 * 1024 * 1024)
print (datetime.now())

print (os.path.getsize("c:/Users/xyz/Desktop/bigFile.txt"))
print (os.stat("c:/Users/xyz/Desktop/bigFile.txt").st_size)
