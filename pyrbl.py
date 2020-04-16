#!/usr/bin/env python3

import subprocess
import shlex
import socket
import IPy
import os

rbl=[line.strip() for line in open('rbllist')]
ipaddress=[line.strip() for line in open('iplist')]

def rblcheck():
    for i in ipaddress:
        for f in rbl:
            reverseip = ".".join(reversed(i.split('.')))
            checkstring = reverseip + '.' + f + '.'
            cmd = 'dig +short ' + checkstring
            proc=subprocess.Popen(shlex.split(cmd),stdout=subprocess.PIPE)
            out,err=proc.communicate()
            if out:
                try:
                    gethost = socket.gethostbyaddr(i)
                    gethost = gethost[0]
                    alert_msg=f"{i} ({gethost}) is blacklisted on {f}"
                    print(alert_msg)
                except socket.herror:
                    gethost = 'Unknown host'
                    alert_msg=f"{i} ({gethost}) is blacklisted on {f}"
                    print(alert_msg)

if __name__ == "__main__":
    rblcheck()
