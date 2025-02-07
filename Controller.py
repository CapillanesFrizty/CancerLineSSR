from colorama import Fore, Style, init

# Initialize colorama for Windows compatibility
init(autoreset=True)

def show_menu():
    print(Fore.RED + r"""
       _____                                        _        _                     _____   _        _____ 
      / ____|                                      | |      (_)                   / ____| | |      |_   _|
     | |        __ _   _ __     ___    ___   _ __  | |       _   _ __     ___    | |      | |        | |  
     | |       / _` | | '_ \   / __|  / _ \ | '__| | |      | | | '_ \   / _ \   | |      | |        | |  
     | |____  | (_| | | | | | | (__  |  __/ | |    | |____  | | | | | | |  __/   | |____  | |____   _| |_ 
      \_____|  \__,_| |_| |_|  \___|  \___| |_|    |______| |_| |_| |_|  \___|    \_____| |______| |_____|
    """ + Style.RESET_ALL)

    print(Fore.CYAN + """
    ===========================================
                    MAIN MENU               
    ===========================================
    """ + Fore.GREEN + """
    [1] Option 1 - Data Definition Language
    [2] Option 2 - Data Access Object Commands
    [5] Option 3 - Exit
    """ + Fore.CYAN + """
    ===========================================
    """ + Fore.YELLOW)

show_menu()