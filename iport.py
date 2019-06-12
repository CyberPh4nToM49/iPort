# -*- coding: utf-8 -*-
#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime
from config import PLUS

subprocess.call('clear', shell=True)

def banner():
    print("""
    _ _____           _   
   (_)  __ \         | |  
    _| |__) |__  _ __| |_ 
   | |  ___/ _ \| '__| __|
   | | |  | (_) | |  | |_ 
   |_|_|   \___/|_|   \__|
                                                    

https://github.com/
------------------------------------------------------------
    """)

remoteServer    = raw_input("IP à Scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer)
banner()
print "-" * 60
print "Sois patient negro, ça scan!", remoteServerIP
print "-" * 60

t1 = datetime.now()


try:
    for port in range(1,1025):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "{}Port {}: 	 Open".format(PLUS,port)
        sock.close()

except KeyboardInterrupt:
    print "arrêter Ctrl+C"
    sys.exit()

except socket.gaierror:
    print 'IP non Scannable. quit'
    sys.exit()

except socket.error:
    print "Impossible de ce connecter au serveur"
    sys.exit()

t2 = datetime.now()

total =  t2 - t1

print '{}Scan compléter en: '.format(PLUS,), total