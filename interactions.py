NONE, SHOW_HOSTS, SHOW_SERVICES, ADD_HOST , ADD_SERVICE, BACK, *_  = range(10)
OP_NONE,OP_MODES, OP_PROFILES, OP_OBJECTS, OP_RULES, EXIT, *_ = range(10)
RULE_NONE, RULE_ADD, RULE_LIST, RULE_BACK, *_ = range(10)
CHAIN_NONE, CHAIN_IN, CHAIN_OUT, *_ = range(5)
PROFILES_NONE, LIST_PROFILES, LOAD_PROFILE, PROFILE_BACK, *_ = range(5)
MODE_NONE, MODE_DROP, MODE_ACCEPT, MODE_BACK, *_ = range(5) 

def show_main_menu():
    print("(" + str(OP_MODES) +")  Modes")
    print("(" + str(OP_PROFILES) +")  Profiles")
    print("(" + str(OP_OBJECTS) +")  Objects")
    print("(" + str(OP_RULES) +")  rules")
    print("(" + str(EXIT) +")  Exit")


def show_objects_menu():
    print("(" + str(SHOW_HOSTS) +")  Show all hosts")
    print("(" + str(SHOW_SERVICES) +")  Show all services")
    print("(" + str(ADD_HOST) +")  Add new host")
    print("(" + str(ADD_SERVICE) +")  Add new service")
    print("(" + str(BACK) +")  Back")


def show_rules_menu():
    print("(" + str(RULE_ADD) +")  Add new rule")
    print("(" + str(RULE_LIST) +")  Block from list")
    print("(" + str(RULE_BACK) +")  Back")


def show_chains_menu():
    print("(" + str(CHAIN_IN) +")  INPUT")
    print("(" + str(CHAIN_OUT) +")  OUTPUT")
 

def show_profiles_menu():
    print("(" + str(LIST_PROFILES) +")  List profiles")
    print("(" + str(LOAD_PROFILE) +")  Load profile")
    print("(" + str(PROFILE_BACK) +")  Back")
 

def show_modes_menu():
    print("(" + str(MODE_DROP) +")  Blacklist")
    print("(" + str(MODE_ACCEPT) +")  Whitelist")
    print("(" + str(MODE_BACK) +")  Back")