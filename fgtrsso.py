from pyrad.client import Client
from pyrad.dictionary import Dictionary
from io import StringIO
import socket
import sys
import pyrad.packet
import ipaddress

def SendPacket(srv, req):
    try:
        srv.SendPacket(req)
    except pyrad.client.Timeout:
        print("RADIUS server does not reply")
        sys.exit(1)
    except socket.error as error:
        print("Network error: " + error[1])
        sys.exit(1)
        
# For more Acct-Status-Type action, check Radius Dictionary
        
dict = StringIO("ATTRIBUTE User-Name 1 string\n" +
                "ATTRIBUTE Framed-IP-Address 8 ipaddr\n" +
                "ATTRIBUTE Class 25 string\n" +
                "ATTRIBUTE Calling-Station-Id 31 string\n" +
                "ATTRIBUTE Acct-Status-Type 40 integer\n" +
                "ATTRIBUTE Acct-Session-Id 44 string\n" +
                "VALUE Acct-Status-Type Start 1\n" +
                "VALUE Acct-Status-Type Stop 2")        

srv = Client(server="192.168.3.1", secret=b"123456",
             dict=Dictionary(dict))            

req = srv.CreateAcctPacket(User_Name="teste2")

req["Calling-Station-Id"] = "00-0c-29-44-BE-B8"
req["Acct-Session-Id"] = "0211a4ef"
req["Framed-IP-Address"] = "10.0.0.100"
req["Class"] = "group1"
req["Acct-Status-Type"] = "Start"

for ip in ipaddress.IPv4Network('192.168.0.0/14'):
    req["Framed-IP-Address"] = "%s" % ip
    print("Sending accounting start packet")
    SendPacket(srv, req)