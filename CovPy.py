# tested on android (termux, python)
import os
import time
import requests
from covid import Covid
from termcolor import colored
from prettytable import PrettyTable

covid = Covid()

# these colors might cause errors on windows
class fontcolor:
    def green(string):
        return colored(string, "green", attrs=["bold"])

    def white(string):
        return colored(string, "white", attrs=["bold"])

    def grey(string):
        return colored(string, "grey", attrs=["bold"])

    def yellow(string):
        return colored(string, "yellow", attrs=["bold"])

    def cyan(string):
        return colored(string, "cyan", attrs=["bold"])

    def red(string):
        return colored(string, "red", attrs=["bold"])

    def blue(string):
        return colored(string, "blue", attrs=["bold"])


class symbol:
    WARN = fontcolor.red(" [-] ")
    DONE = fontcolor.green(" [+] ")
    INPUT = fontcolor.cyan(" [»] ")
    INFO = fontcolor.yellow(" [!] ")
    ARROW = fontcolor.cyan(" > ")
    NUM_1 = fontcolor.yellow(" [1] ")
    NUM_2 = fontcolor.yellow(" [2] ")
    NUM_3 = fontcolor.yellow(" [3] ")
    NUM_4 = fontcolor.yellow(" [4] ")
    NUM_5 = fontcolor.yellow(" [5] ")


def print_banner():
    banr = """
         o-o  o-o  o   o     o--o  o   o 
        /    o   o |   |     |   |  \ /  
       O     |   | o   o     O--o    O   
        \    o   o  \ /      |       |   
         o-o  o-o    o       o       o   
                                  
            CovPy  - Python Covid Tracker
            GitHub - @sumit-buddy
	"""
    print(fontcolor.cyan(banr))


# Main Option Menu
def display_options():
    print(symbol.INPUT + fontcolor.cyan("AVAILABLE OPTIONS ↓"))
    print(symbol.NUM_1 + fontcolor.white("Global Statistics"))
    print(symbol.NUM_2 + fontcolor.white("Country & ID Table"))
    print(symbol.NUM_3 + fontcolor.white("Search By Name"))
    print(symbol.NUM_4 + fontcolor.white("Search By ID"))
    print(symbol.NUM_5 + fontcolor.white("Quit"))


# Check Internet Connection
def check_internet(url="http://www.google.com/", timeout=5):
    try:
        _ = requests.head(url, timeout=timeout)
        print(symbol.DONE + fontcolor.green("Connected Successfully."))
        return True
    except requests.ConnectionError:
        print(symbol.WARN + fontcolor.red("No Internet Connection.") + "\n")
        quit()
    return False


# Fancy Box Message
def box_msg(msg):
    row = len(msg)
    m = "".join([" +"] + ["-" * row] + ["+"])
    h = fontcolor.cyan(m)
    result = (
        h
        + "\n"
        + fontcolor.cyan(" |")
        + fontcolor.white(msg)
        + fontcolor.cyan("|")
        + "\n"
        + h
    )
    print("\n" + result)


# Clear Screen
def clear_screen():
    if os.name == "posix":
        _ = os.system("clear")
    else:
        _ = os.system("cls")


# "Press Enter To Continue" Message
def continue_msg():
    input("\n" + symbol.INPUT + fontcolor.cyan("Press Enter To Continue : "))
    clear_screen()


# Main Menu
def display_menu():
    print_banner()
    check_internet()
    box_msg(" Global Covid-19 Live Information Tracker ")
    display_options()


# [1] Global Covid Statistics
def global_stats():
    box_msg(" Global Coronavirus Disease Statistics ")
    try:
        print(
            symbol.INFO + fontcolor.white("   Active Cases :"),
            "{:,}".format(covid.get_total_active_cases()),
        )
        print(
            symbol.INFO + fontcolor.white("Confirmed Cases :"),
            "{:,}".format(covid.get_total_confirmed_cases()),
        )
        print(
            symbol.INFO + fontcolor.white("Recovered Cases :"),
            "{:,}".format(covid.get_total_recovered()),
        )
        print(
            symbol.INFO + fontcolor.white("    Death Cases :"),
            "{:,}".format(covid.get_total_deaths()),
        )
    except Exception as e:
        print(e)
        print("\n" + symbol.WARN + fontcolor.red("No Internet Connection!"))
    finally:
        continue_msg()


# [2] Print Country & ID Table
def display_name_id():
    box_msg(" Countries And Assigned Id Table ")
    country_id_table = PrettyTable([fontcolor.cyan("Id"), fontcolor.cyan("Country")])
    try:
        countries = covid.list_countries()
        for country in countries:
            country_id_table.add_row(list(country.values()))
            country_id_table.add_row(
                [fontcolor.grey("-") * 5, fontcolor.grey("-") * 32]
            )
        print(country_id_table)
    except Exception:
        print("\n" + symbol.WARN + fontcolor.red("No Internet Connection!"))
    finally:
        continue_msg()


# [3] Status With Country Name
def status_with_name():
    box_msg(" Search Covid-19 Statistics By Country Name ")
    country_name_data_table = PrettyTable(
        [fontcolor.cyan("Parameter"), fontcolor.cyan("Value")]
    )
    try:
        country_name = input(
            symbol.INPUT + fontcolor.cyan("Enter Country Name : ")
        ).strip()
        country_name_stats = covid.get_status_by_country_name(country_name)
        for k, v in country_name_stats.items():
            country_name_data_table.add_row([fontcolor.white(k), fontcolor.white(v)])
            country_name_data_table.add_row(
                [fontcolor.grey("-") * 15, fontcolor.grey("-") * 15]
            )
        print("\n")
        print(country_name_data_table)
    except:
        print(
            symbol.WARN + fontcolor.red("Wrong Country Name Or No Internet Connection!")
        )
    finally:
        continue_msg()


# [4] Status With Country ID
def status_with_id():
    box_msg(" Search Covid-19 Statistics By Country ID ")
    country_id_data_table = PrettyTable(
        [fontcolor.cyan("Parameter"), fontcolor.cyan("Value")]
    )
    try:
        country_id = int(input(symbol.INPUT + fontcolor.cyan("Enter Country Id : ")))
        country_id_stats = covid.get_status_by_country_id(country_id)
        for k, v in country_id_stats.items():
            country_id_data_table.add_row(
                [fontcolor.white(k).capitalize(), fontcolor.white(v)]
            )
            country_id_data_table.add_row(
                [fontcolor.grey("-") * 15, fontcolor.grey("-") * 15]
            )
        print("\n")
        print(country_id_data_table)
    except:
        print(
            symbol.WARN + fontcolor.red("Wrong Country ID Or No Internet Connection!")
        )
    finally:
        continue_msg()


# Looping All Things
while True:
    display_menu()
    choice = input(
        "\n" + symbol.INPUT + fontcolor.cyan("Enter Your Choice [1,2,3,4,5] : ")
    )

    if choice == "1":
        global_stats()
    elif choice == "2":
        display_name_id()
    elif choice == "3":
        status_with_name()
    elif choice == "4":
        status_with_id()
    elif choice == "5":
        print(symbol.WARN + fontcolor.red("Quitting...") + "\n")
        time.sleep(1)
        quit()
    else:
        print(symbol.WARN + fontcolor.red("Sorry! Enter A Valid Input !"))
        break
