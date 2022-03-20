import multiprocessing
import ssl
from os import environ
from defs.unsorted_will_be_replaced import run_command
from defs.unsorted_will_be_replaced import wait
import time	### sleeping time for redability of print commands ###
import subprocess
import os	### For restarting program ###
from getpass import getpass
# to start main menu

run_command("clear")
print("\nVersion_by_Naitik_Joshi\n")

print("\napllications for data scraping and data mining")

print("\n\nCHOOSE A PROGRAM!")



print("\n1) Instagram-Scraper")

print("\n2) Twitter-Analyzer")

print("\n3) Account-Finder")
value = input(" \nProgram Number : ")

if value == "1":
	run_command("clear")
	print("Initializing Scraper .........")
	time.sleep(2)
	ig_username = input("Enter your instagram Username : ")
	password = getpass("Enter your instagram Password : ")
	victim = input("Username of account which needs to be scraped : ")
	print("Running Scraper...")
	time.sleep(2)
	#command = "instagram-scraper {victim} -u {username} -p {password}"
	subprocess.run(['instagram-scraper', victim, '-u', ig_username, '-p', password])
	print("Account Scraped, Check " + victim + " Directory for scraped data")
	rerun = input("Do you want to run any other program ? [Y/n] ")
	if rerun == "Y":
		os.system("python3 Menu.py")
		print("Restarting ... ")
	else:
		print("Shutting Down Scraper...")
		time.sleep(2)

elif value == "2":
	run_command("clear")
	print("Initializing Tweet Analyzer........")
	time.sleep(2)
	tt_username = input("\nEnter the twitter account to be analyzed : ")
	print("Running Analyzer...")
	time.sleep(2)
	subprocess.run(['tweets_analyzer.py', "-n", tt_username])
	rerun = input("Do you want to run any other program ? [Y/n] ")
	if rerun == "Y":
		os.system("python3 Menu.py")
		print("Restarting ... ")
	else:
		print("Shutting Down Scraper...")
		time.sleep(2)

elif value == '3':
	run_command("clear")
	print("Initializing Username Finder.....")
	time.sleep(2)
	finder_username = input("Enter The Username to Look for : ")
	print("Running Scraper...")
	time.sleep(2)
	subprocess.run(['sherlock', finder_username])
	rerun = input("Do you want to run any other program ? [Y/n] ")
	if rerun == "Y":
		os.system("python3 Menu.py")
		print("Restarting ... ")
	else:
		print("Shutting Down Scraper...")
		time.sleep(2)

