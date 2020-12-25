import arrow
import socket
import requests
import webbrowser
from covid import Covid
from cfonts import render
from prettytable import PrettyTable
from tqdm import tqdm 
from time import sleep

covid = Covid()

#color codes
BLACK = '\x1b[1;30;40m'
RED = '\x1b[0;31;40m'
GREEN = '\x1b[1;32;40m'
YELLOW = '\x1b[1;33;40m'
BLUE = '\x1b[1;34;40m'
PURPLE = '\x1b[1;35;40m'
CYAN = '\x1b[1;36;40m'
WHITE = '\x1b[1;37;40m'
END = '\x1b[0m'

#banner
def banner():
	banner = render("covid", colors=['yellow','cyan'], align='center')
	print(banner)

banner2= render("THANK-YOU",font='chrome',colors=['green','green','green'],align='center')

#display time author
def time_author():
	tem = arrow.get().format('DD-MM-YYYY')
	print(YELLOW+' [*] '+END+YELLOW+tem+END,'-'*30,YELLOW+'$ Sumit $'+END)

#print banner & time/author
banner()
time_author()

#symbol used in program
arrow_left = CYAN + '>>>' + END
arrow_right = CYAN + '<<<' + END
arrow = CYAN + ' ##>' + END
small_arrow= PURPLE + ' »' + END
tick = GREEN + '✓✓ ' + END
box = GREEN +' [*] '+END
warn_box = YELLOW+' [*] '+END

#stylish numbers
one = YELLOW+' ['+END+'1'+YELLOW+']'+END
two = YELLOW+' ['+END+'2'+YELLOW+']'+END
three = YELLOW+' ['+END+'3'+YELLOW+']'+END
four = YELLOW+' ['+END+'4'+YELLOW+']'+END
five = YELLOW+' ['+END+'5'+YELLOW+']'+END
six = YELLOW+' ['+END+'6'+YELLOW+']'+END
seven = YELLOW+' ['+END+'7'+YELLOW+']'+END

#display choices
first = WHITE + ' Global Covid-19 Status ' + END
second = WHITE +' Country & ID Table ' + END
third = WHITE + ' Status By Country Name '+END
fourth = WHITE + ' Status By Country ID '+END
fifth = WHITE + ' Visit Our Website ' +END
sixth = WHITE + ' QUIT ' + END

#input field colour
w_input = WHITE + ' Enter Your Choice [1,2,3,4,5 or 6] : ' + END

#msg box variables 
welcome_msg = GREEN + 'Global Covid-19 Live Information System'+ END
info_1 = GREEN + '\tGlobal Covid-19 Status'+END
info_2 = GREEN + '\tCountries & Respective IDs ' +END
info_3 = GREEN + '\tStatus By Country Name' +END
info_4 = GREEN + '\tCovid Search By Country ID' +END

#welcome msg_box
l = ''.join([' +'] + ['-' *49] + ['+'])
wlc_msg = l +'\n'+' '+'|'+' '+arrow_left+' '+welcome_msg+' '+arrow_right+' '+ '|' +'\n' +l

#add student msg_box
m = ''.join([' +'] + ['-' *40] + ['+'])
result_1 = m + '\n' +info_1 + '\n' + m

#view student msg_box
n = ''.join([' +'] + ['-' *40] + ['+'])
result_2 = n + '\n' + info_2 + '\n' + n

#search student msg_box
p = ''.join([' +'] + ['-' *40] + ['+'])
result_3 = p + '\n' + info_3 + '\n' + p

#update student msg_box
q = ''.join([' +'] + ['-' *48] + ['+'])
result_4 = q + '\n' + info_4 + '\n' + q

def internet(url='http://www.google.com/', timeout=5):
    try:
        _ = requests.head(url, timeout=timeout)
        print('\n')
        print(warn_box+"Connected...You Are Ready To Rock :)")
        print('\n')
        return True
    except requests.ConnectionError:
        print('\n')
        print(warn_box+WHITE+"¯\_(ツ)_/¯"+END)
        print('\n')
        print(warn_box+WHITE+"No Internet Connection."+END)
        print(warn_box+WHITE+"Turn On Your Internet To Continue."+END)
        print('\n')
        quit()
    return False

internet()

def display_menu():
	print(wlc_msg)
	print(' '*40)
	print(arrow+one+first)
	print(arrow+two+second)
	print(arrow+three+third)
	print(arrow+four+fourth)
	print(arrow+five+fifth)
	print(arrow+six+sixth)
	print('\n')

#press enter to continue msg
def continue_msg():
	       	print('\n')
	       	input(arrow + YELLOW + " Press Enter To Continue : " + END)
	       	print('\n')

#progress bar for swag
def progress_bar():
	for i in tqdm(range(0, 100), desc ="Fetching Data"):
		sleep(.02)

#global status
def global_stats():
	print(result_1)
	active = covid.get_total_active_cases()
	confirmed = covid.get_total_confirmed_cases()
	recovered = covid.get_total_recovered()
	deaths = covid.get_total_deaths()
	
	print('\n')
	print(box,'Total Active Cases :',WHITE,active,END)
	print(box,'Total Confirmed Cases :',WHITE,confirmed,END)
	print(box,'Total Recovered Cases :',WHITE,recovered,END)
	print(box,'Total Death Cases :', WHITE,deaths,END)
	
	continue_msg()

#table of county & id
def display_name_id():
	print(result_2)
	country_id_table = PrettyTable([YELLOW+'COUNTRY'+END, YELLOW+'ID'+END])
	
	progress_bar()
	
	countries = covid.list_countries()
#dividing dictionaries in 2 part	
	for country in countries:
		d1 = dict(list(country.items())[len(country)//2:])
		d2 = dict(list(country.items())[:len(country)//2])
		
		#print(d1)
		#print(d2)
		
		l = list(d1.values())
		m = list(d2.values())
		
		#print(l)
		#print(m)

#Merging dict. values in a single dict.				
		full_dict = dict(zip(l,m))
		
		#print(full_dict)

#converting dict. into a table
		for x, y in full_dict.items():
			country_id_table.add_row([CYAN+x+END, WHITE+y+END])
			country_id_table.add_row([BLACK+'-'*32+END,BLACK+'-'*5+END])
	print('\n')		
	print(country_id_table)
	
	continue_msg()

#covid status using country name
def status_with_name():
	print(result_3)
	country_name = input(arrow+YELLOW+" Enter Country Name : "+END).strip()
	
	print('\n')
	progress_bar()
	print('\n')
		
	data_table_1 = PrettyTable([YELLOW+'PARAMETERS','VALUE'+END])
	
	stats_1 = covid.get_status_by_country_name(country_name)
	
	for k, v in stats_1.items():
		data_table_1.add_row([CYAN+k.capitalize()+END,v])
		data_table_1.add_row([BLACK+'-'*15+END,BLACK+'-'*15+END])
	
	print(data_table_1)
	continue_msg()
	
#covid status using country id
def status_with_id():
	print(result_4)
	country_id = int(input(arrow+YELLOW+" Enter Country Id : "+END))
	print('\n')
	progress_bar()
	print('\n')
	
	data_table_2 = PrettyTable([YELLOW+'PARAMETERS','VALUE'+END])
	
	stats_2 = covid.get_status_by_country_id(country_id)
	
	for key, val in stats_2.items():
		data_table_2.add_row([CYAN+key.capitalize()+END, val])
		data_table_2.add_row([BLACK+'-'*15+END,BLACK+'-'*15+END])
		
	print(data_table_2)
	continue_msg()

def our_site():
	print('\n')
	print(box+WHITE+"Opening"+END,GREEN+"https://thetechnohack.cf"+END,WHITE+"in 2 seconds."+END)
	sleep(2)
	webbrowser.open('https://thetechnohack.cf')
	continue_msg()
	
while True:
    display_menu()

    choice = input(arrow+w_input)
    while not choice:
    	print(box+YELLOW+'Value can\'t be empty !'+END)
    	choice = input(arrow+w_input)
    
    if choice == '1':
    	global_stats()
    elif choice == '2':
    	display_name_id()
    elif choice == '3':
    	status_with_name()
    elif choice == '4':
    	status_with_id()
    elif choice == '5':
    	our_site()
    elif choice == '6':
    	print(box+"Quitting...")
    	print(banner2)
    	quit()
    else:
    	   print(box+CYAN+'Sorry! Enter A Valid Input !'+END)
    	   print(box+CYAN+'QUITTING...'+END)
    	   break
