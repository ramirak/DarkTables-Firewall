import subprocess
import socket

def set_mode(mode):
    if mode == "DEFAULT_ACCEPT":
        pass
    elif mode == "DEFAULT_DROP":
        pass
    else:
        print("failed to resolve mode")


def set_rule(direction, s_host, d_host, d_port, protocol, action):
    ip_0 = "iptables -A " + direction + " -m state --state NEW"
    if protocol != "any":
        ip_0 += " -p " + protocol + " --match multiport --dport " + d_port
    if s_host != "any":
        ip_0 += " -s " + s_host
    if d_host != "any":
        ip_0 += " -d " + d_host
    ip_0 += " -j " + action 

    switch_dir(direction)

    ip_1 = "iptables -A " + direction + " -m state --state RELATED,ESTABLISHED"
    if protocol != "any":
        ip_1 += " -p " + protocol + " --match multiport --sport " + d_port
    if s_host != "any":
        ip_1 += " -s " + d_host
    if d_host != "any":
        ip_1 += " -d " + s_host
    ip_1 += " -j " + action 

    proc1 = subprocess.Popen(ip_0.split(), stdout=subprocess.PIPE)
    output, error = proc1.communicate()
    proc2 = subprocess.Popen(ip_1.split(), stdout=subprocess.PIPE)
    output, error = proc2.communicate()
    

def switch_dir(direction):
    if direction == "OUTPUT":
        return "INPUT"
    return "OUTPUT"


def is_valid_ip(address):
    try:
        socket.inet_aton(address)
        return 1
    except socket.error:
        return 0
