import os
a=int(input("Press 1 for Termux\nPress 2 For Linux\n->>>>  "))
if a==1:
  os.system("pkg install python3&&pip install --upgrade pip&&pip install requests&&cd&&cd TBomb-Infinity&&chmod +x TBomb-Infinite.py && python3 TBomb-Infinite.py")
else:
  os.system("apt install python3&&pip install --upgrade pip&&pip install requests&&cd&&cd TBomb-Infinity&&chmod +x TBomb-Infinite.py && python3 TBomb-Infinite.py")

