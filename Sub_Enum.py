import os
import requests
import sys
import time

from cfonts import render
from termcolor import colored

banner = render("Sub_Enum", colors=['blue', 'yellow'], align='center')
print(banner)

print("======================================================")


cred='Coded by:--> @AnandGurav'
print(colored(cred,'red'))
lang='GitHub:--> Anand201096'
print(colored(lang,'red'))
print("======================================================")



a2 = input(colored('[*] Enter Domain Name:--> ','red'))


file = input(colored('[*] Enter Wordlist File Name:--> ','red'))

print(" ")
print(colored('[*] Please wait a while, the script is processing......','green'))
print(" ")



path=os.getcwd() + file

sub_list = open(file).read() 
subdoms = sub_list.splitlines()





for sub in subdoms:
    sub_domains = f"http://{sub}.{a2}"

    try:
        requests.get(sub_domains)

    except requests.ConnectionError: 
        pass
    else:
        print(colored('[*] Valid Domain:--> ','green'),sub_domains)
        


time.sleep(1)

output = render('Thankyou!', colors=['yellow', 'red'], align='center')
print(output)



def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)

if __name__ == "__main__":
    answer = input("\n [-] Do you want to restart this program ?(y/n) ")
    if answer.lower().strip() in "y".split():
        restart_program()

