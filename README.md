## FortiGate user RSSO authentication
A simple tool to create authenticated radius single sign-on users on FortiOS.

### Requirements and Installation
Linux with Python 3 and freeradius-utils

### Usage
Replace the IP_ADDRESS and RAD_SECRET with your FortiGate IP and Radius secret configuration

### FortiGate configuration

```
config system interface    
    edit "mgmt1"
        set vdom "root"
        set ip 10.1.1.1 255.255.255.0
        set allowaccess ping https ssh snmp radius-acct
        set type physical
        set snmp-index 37
    next
end

config user radius
    edit "RSSO Agent"
        set rsso enable
        set rsso-radius-response enable
        set rsso-validate-request-secret enable
        set rsso-secret YOUR_RAD_SECRET
        set rsso-endpoint-attribute User-Name
    next
end

config user group
    edit "rsso-group1"
        set group-type rsso
        set sso-attribute-value "group1"
    next
end
```

