import os, sys
import data_handler, interactions
from ip_t import set_rule

def init():
    hosts = data_handler.retrieve_hosts()
    services = data_handler.retrieve_services()
    chains = data_handler.retrieve_chains()

    if not os.geteuid() == 0:
        sys.exit("\nOnly root can run this program\n")
    
    clear = lambda: os.system('clear')
    while(True):
        with open('logo.txt', 'r') as f:
            print(f.read())
        main_menu(hosts,services,chains)
#        clear()


def main_menu(hosts,services,chains):
    print("\nEnter your choice - \n")
    interactions.show_main_menu()
    choice = -1;
    while choice == -1:
        choice = assert_choice(input("\n> "))
        if choice == interactions.OP_PROFILES:
            load_profile_menu()
        elif choice == interactions.OP_OBJECTS:
            object_creation_menu(hosts,services,chains)
        elif choice == interactions.OP_RULES:
            rules_menu(hosts,services,chains)
        elif choice == interactions.EXIT:
            exit(0)
        else:
            print("\nEnter your choice - \n")
            interactions.show_main_menu()
        choice = -1

def object_creation_menu(hosts,services,chains):
    print("\nEnter your choice - \n")
    interactions.show_objects_menu()
    choice = -1;
    while choice == -1:
        choice = assert_choice(input("\n> "))
        if choice == interactions.SHOW_HOSTS:
            data_handler.show_hosts(hosts)
        elif choice == interactions.SHOW_SERVICES:
            data_handler.show_services(services)
        elif choice == interactions.ADD_HOST:
            pass
        elif choice == interactions.ADD_SERVICE:
            pass
        elif choice == interactions.BACK:
            return
        else:
            print("\nEnter your choice - \n")
            interactions.show_objects_menu()
        choice = -1

def rules_menu(hosts,services,chains):
    print("\nEnter your choice - \n")
    interactions.show_rules_menu()
    choice = -1;
    while choice == -1:
        choice = assert_choice(input("\n> "))
        if choice == interactions.RULE_ADD:
            add_rule_menu(hosts,services,chains)
        elif choice == interactions.RULE_LIST:
            pass
        elif choice == interactions.RULE_BACK:
            return
        else:
            print("\nEnter your choice - \n")
            interactions.show_rules_menu()
        choice = -1

def add_rule_menu(hosts, services, chains):
    rule = []
    # Chain
    print("\nChoose chain - \n")
    interactions.show_chains_menu()
    choice = -1;
    while choice == -1:
        choice = assert_choice(input("\n> "))
        if(choice <= 0 or choice > 2):
            choice = -1
    rule.append(choice-1)

    # Source IP
    choice = -1
    print("\nChoose source - \n")
    while choice == -1:
        data_handler.show_hosts(hosts)        
        choice = assert_choice(input("\n> "))
        if(choice <= 0 or choice > len(hosts)):
            choice = -1
        rule.append(choice-1) 
    
    # Destination IP
    choice = -1
    print("Choose target - \n")
    while choice == -1:
        choice = assert_choice(input("\n> "))
        if(choice <= 0 or choice > len(hosts)):
            choice = -1
        rule.append(choice-1)
    
    # Service
    choice = -1
    num_srv = 0
    print("\nChoose Service - \n")
    while choice == -1:
        data_handler.show_services(services)
        choice = assert_choice(input("\n> "))
        if(choice <= 0 or choice > len(services)):
            choice = -1
        rule.append(choice-1)
        res = input("Add another service? [y/n] >  ")
        if(res == "y"): 
            choice = -1 
            num_srv +=1 

    # Rule setup
    for ns in range(num_srv):
        for i in range(len(services[rule[3]].getProtocol())):
            set_rule(chains[rule[0]], hosts[rule[1]].getAddr(), hosts[rule[2]].getAddr(), services[rule[3+ns]].getPort(), services[rule[3+ns]].getProtocol()[i], "ACCEPT")


def load_profile_menu():
    print("\nEnter your choice - \n")
    interactions.show_profiles_menu()
    choice = -1;
    all_profiles = []
    while choice == -1:
        choice = assert_choice(input("\n> "))
        if choice == interactions.LIST_PROFILES:
            all_profiles = data_handler.retrieve_profiles()
            data_handler.show_profiles(all_profiles)
        elif choice == interactions.LOAD_PROFILE:
            pass
        elif choice == interactions.PROFILE_BACK:
            return
        else:
            print("\nEnter your choice - \n")
            interactions.show_profiles_menu()
        choice = -1


def assert_choice(choice):
    try:
        choice = int(choice)
    except:
        return -1;
    return choice

init()
