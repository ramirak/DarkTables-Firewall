import json
from unicodedata import name
import objects

def retrieve_hosts():
    # Opening hosts JSON file
    with open('hosts.json') as hosts_file:
        data = json.load(hosts_file)
        all_hosts = [objects.Host("any","any")]
        
        for h1 in data["default"]:
            all_hosts.append(objects.Host(h1["name"], h1["ipaddr"]))
       
        for h2 in data["user_defined"]:
            all_hosts.append(objects.Host(h2["name"], h2["ipaddr"]))
        
        return all_hosts
        
def retrieve_services():
    # Opening services JSON file
    with open('services.json') as services_file:
        data = json.load(services_file)
        all_services = [objects.Service("any","any","[any]")]
        
        for s1 in data["default"]:
            all_services.append(objects.Service(s1["name"], s1["port"], s1["proto"]))
       
        for s2 in data["user_defined"]:
            all_services.append(objects.Service(s2["name"], s2["port"], s2["proto"]))

        return all_services 


def retrieve_profiles():
    # Opening profiles JSON file
    with open('profiles.json') as profiles_file:
        data = json.load(profiles_file)
        return data 


def retrieve_block_list():
    ip_list = []
    with open("addresses.list") as file:
        for line in file:
            ip_list.append(line.rstrip())
    return ip_list


def show_profiles(data):
    i = 1
    for p in data:
        print("- " + str(i) + " " + p)
        i+=1

def show_hosts(hosts):
    i = 1
    for h in hosts:
        print("%-30s %-30s" % ("(" + str(i) + ") " + h.getName(), h.getAddr()))
        i+=1


def show_services(services):
    i = 1
    for s in services:
        print("%-30s %-30s %-30s" % ("(" + str(i) + ") " + s.getName(), s.getProtocol(), s.getPort()))
        i+=1


def retrieve_chains():
    # more user defined chains may be implemented in the future
    chains = ["INPUT", "OUTPUT"]
    return chains   


    


