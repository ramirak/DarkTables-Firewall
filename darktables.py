import os, sys
import data_handler, interactions
from ip_t import clear_chains, set_rule, show_chains, switch_mode

def init():
    hosts = data_handler.retrieve_hosts()
    services = data_handler.retrieve_services()
    chains = data_handler.retrieve_chains()

    if not os.geteuid() == 0:
        sys.exit("\nOnly root can run this program\n")
    
    clear = lambda: os.system('clear')
    while(True):
        if os.path.isfile('logo.txt'):
            with open('logo.txt', 'r') as f:
                print(f.read())
        main_menu(hosts,services,chains)


def main_menu(hosts,services,chains):
    print("\nEnter your choice - \n")
    interactions.show_main_menu()
    choice = -1;
    while choice == -1:
        choice = assert_choice(input("\n> "))
        if choice == interactions.OP_MODES:
            modes_menu()
        elif choice == interactions.OP_PROFILES:
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


def modes_menu():
    print("\nEnter your choice - \n")
    interactions.show_modes_menu()
    choice = -1;
    all_profiles = []
    while choice == -1:
        choice = assert_choice(input("\n> "))
        if choice == interactions.MODE_DROP:
            switch_mode("DROP")
        elif choice == interactions.MODE_ACCEPT:
            switch_mode("ACCEPT")
        elif choice == interactions.MODE_BACK:
            return
        else:
            print("\nEnter your choice - \n")
            interactions.show_modes_menu()
        choice = -1


def load_profile_menu():
    print("\nEnter your choice - \n")
    interactions.show_profiles_menu()
    choice = -1;
    all_profiles = data_handler.retrieve_profiles()
    while choice == -1:
        choice = assert_choice(input("\n> "))
        if choice == interactions.LIST_PROFILES:
            data_handler.show_profiles(all_profiles)
        elif choice == interactions.LOAD_PROFILE:
            profile = -1
            while profile == -1:
                print("\nChoose your profile -\n")
                data_handler.show_profiles(all_profiles)
                profile = assert_choice(input("\n> "))
                if(profile < 0 or profile > len(all_profiles)):
                    profile = -1
            load_profile(all_profiles,profile - 1)
        elif choice == interactions.PROFILE_BACK:
            return
        else:
            print("\nEnter your choice - \n")
            interactions.show_profiles_menu()
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
            res = input("Are you sure you would like to block all addresses in the list? [y/n] >  ")
            if(res == "y"):
                ip_list = data_handler.retrieve_block_list()
                for addr in ip_list:
                    set_rule("OUTPUT", "any", addr,"any","any","DROP")
        elif choice == interactions.RULE_SHOW:
            show_chains()
        elif choice == interactions.RULE_REMOVE_ALL:
            clear_chains()
        elif choice == interactions.RULE_BACK:
            return
        else:
            print("\nEnter your choice - \n")
            interactions.show_rules_menu()
        choice = -1


def add_rule_menu(hosts, services, chains):
    rule = []
    action = "DROP"
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
    num_srv = 1
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

    choice = -1
    while choice == -1:
        print("\nAction to perform -\n(1) Drop\n(2) Accept")
        choice = assert_choice(input("\n> "))
        if(choice != 1 and choice != 2):
            choice = -1
    
    if choice == 2:
        action = "ACCEPT"   
        
    # Rule setup
    for ns in range(num_srv):
        for i in range(len(services[rule[3]].getProtocol())):
            set_rule(chains[rule[0]], hosts[rule[1]].getAddr(), hosts[rule[2]].getAddr(), services[rule[3+ns]].getPort(), services[rule[3+ns]].getProtocol()[i - 1], action)


def load_profile(data, profile_id):
    profiles_names = []
    for p in data:
        profiles_names.append(p)
    clear_chains()
    print("Loading rules . . . ")
    for p in data[profiles_names[profile_id]]:
        for i in range(len(p["proto"])):
            print(p["dir"] + ": " + p["src"] + ", " + p["dst"] + ", " + p["dport"] + ", " + p["proto"][i] + ", " + p["action"])
            set_rule(p["dir"], p["src"], p["dst"], p["dport"], p["proto"][i], p["action"])
    
    if(p["action"] == "ACCEPT"):
        switch_mode("DROP")
    else:
        switch_mode("ACCEPT")


def assert_choice(choice):
    try:
        choice = int(choice)
    except:
        return -1;
    return choice

init()
