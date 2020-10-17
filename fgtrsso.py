import ipaddress
import os
for ip in ipaddress.IPv4Network('192.168.0.0/14'):
    os.system('echo "Acct-Status-Type =Start,Framed-Ip-Address=%s,User-Name=test2,Acct-Session-Id=0211a4ef,Class=group1,Calling-Station-Id=00-0c-29-44-BE-B8" |  radclient -x IP_ADDRESS acct RAD_SECRET' % ip)
