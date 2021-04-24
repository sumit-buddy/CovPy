# Tested & Coded on Termux & Pydroid (Android)
import os, time, requests
from covid import Covid
from prettytable import PrettyTable

covid = Covid()

# ===== Symbols =====
class symbol:
	WARN = " [-] "
	DONE = " [+] "
	INPUT = " [»] "
	INFO = " [!] "
	ARROW = " > "
	NUM_1 = " [1] "
	NUM_2 = " [2] "
	NUM_3 = " [3] "
	NUM_4 = " [4] "
	NUM_5 = " [5] "

# ===== Print A Cool Banner =====
def print_banner():
	banr = '''
         o-o  o-o  o   o     o--o  o   o 
        /    o   o |   |     |   |  \ /  
       O     |   | o   o     O--o    O   
        \    o   o  \ /      |       |   
         o-o  o-o    o       o       o   
                                  
            CovPy  - Python Covid Tracker
            GitHub - @sumit-buddy
	'''
	print(banr)

# ===== Main Option Menu =====
def display_options():
	print(symbol.INPUT + "AVAILABLE OPTIONS ↓")
	print(symbol.NUM_1 + "Global Statistics")
	print(symbol.NUM_2 + "Country & ID Table")
	print(symbol.NUM_3 + "Search By Name")
	print(symbol.NUM_4 + "Search By ID")
	print(symbol.NUM_5 + "Quit")

# ===== Check Internet Connection =====
def check_internet(url='http://www.google.com/', timeout=5):
    try:
        _ = requests.head(url, timeout=timeout)
        print(symbol.DONE + "Connected Successfully.")
        return True
    except requests.ConnectionError:
        print(symbol.WARN + "No Internet Connection." + "\n")
        quit()
    return False

# ===== Fancy Box Message ===== #
def box_msg(msg):
	row = len(msg)
	m = ''.join([' +'] + ['-' *row] + ['+'])
	result= m + '\n' + " |" + msg + "|" + '\n' + m
	print("\n" + result)
	
# ===== Clear Screen =====
def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

# ===== "Press Enter To Continue" Message ===== #
def continue_msg():
	input("\n" + symbol.INPUT + "Press Enter To Continue : " )
	clear_screen()

# ===== Main Menu ===== #
def display_menu():
	print_banner()
	check_internet()
	box_msg(" Global Covid-19 Live Information Tracker ")
	display_options()

# [1] Global Covid Statistics
def global_stats():
	box_msg(" Global Coronavirus Disease Statistics ")
	try:
		print(symbol.INFO + '   Active Cases :', "{:,}".format(covid.get_total_active_cases()))
		print(symbol.INFO + 'Confirmed Cases :', "{:,}".format(covid.get_total_confirmed_cases()))
		print(symbol.INFO + 'Recovered Cases :', "{:,}".format(covid.get_total_recovered()))
		print(symbol.INFO + '    Death Cases :', "{:,}".format(covid.get_total_deaths()))
	except Exception:
		print("\n" + symbol.WARN + "No Internet Connection!")
	finally:
		continue_msg()

# [2] Print Country & ID Table
def display_name_id():
	box_msg(" Countries And Assigned Id Table ")
	country_id_table = PrettyTable(['Id','Country'])
	try:
		countries = covid.list_countries()
		for country in countries:
		  country_id_table.add_row(list(country.values()))
		  country_id_table.add_row(['-'*5, '-'*32])
		print(country_id_table)
	except Exception:
		print("\n" + symbol.WARN + "No Internet Connection!")
	finally:
		continue_msg()

# [3] Status With Country Name
def status_with_name():
	box_msg(" Search Covid-19 Statistics By Country Name ")
	country_name_data_table = PrettyTable(['Parameter','Value'])
	try:
		country_name = input(symbol.INPUT + "Enter Country Name : ").strip()
		country_name_stats = covid.get_status_by_country_name(country_name)
		for k, v in country_name_stats.items():
			country_name_data_table.add_row([k,v])
			country_name_data_table.add_row(['-'*15,'-'*15])
		print("\n")
		print(country_name_data_table)
	except:
		print(symbol.WARN + "Wrong Country Name Or No Internet Connection!")
	finally:
		continue_msg()

# [4] Status With Country ID
def status_with_id():
	box_msg(" Search Covid-19 Statistics By Country ID ")
	country_id_data_table = PrettyTable(['Parameter','Value'])
	try:
		country_id = int(input(symbol.INPUT + "Enter Country Id : "))
		country_id_stats = covid.get_status_by_country_id(country_id)
		for k, v in country_id_stats.items():
			country_id_data_table.add_row([k,v])
			country_id_data_table.add_row(['-'*15, '-'*15])
		print("\n")
		print(country_id_data_table)
	except:
		print(symbol.WARN + "Wrong Country ID Or No Internet Connection!")
	finally:
		continue_msg()

# Looping All Things
while True:
    display_menu()
    choice = input("\n" + symbol.INPUT + "Enter Your Choice [1,2,3,4,5] : ")
    
    if choice == '1':
    	global_stats()
    elif choice == '2':
    	display_name_id()
    elif choice == '3':
    	status_with_name()
    elif choice == '4':
    	status_with_id()
    elif choice == '5':
    	print(symbol.WARN + "Quitting..." + "\n")
    	time.sleep(1)
    	quit()
    else:
    	   print(symbol.WARN + "Sorry! Enter A Valid Input !")
    	   break
