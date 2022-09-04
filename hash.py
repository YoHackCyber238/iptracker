#!/usr/bin/python



import argparse

import hashlib

from sys import stdout

from pyfiglet import Figlet

import sys

import time

import os



#pip install pyfiglet

#pip install argparse



def clean():

	if os.name == "nt":

		os.system('cls')

	else:

		os.system('clear')

clean()



fi = Figlet(font="doom")

print fi.renderText('magelang1337')

print "\t\t Coded By nginxDEX"

print "\t\t visit to Magelang1337.com" 

print "\t\t use: python hash.py --hash [Your Hash] --lists [password.txt]" 



if __name__ == "__main__":



	parser = argparse.ArgumentParser()

	parser.add_argument("--hash", help="Enter Your MD5 Hash ")

	parser.add_argument("--lists", help="Enter Your Password List")

	args = parser.parse_args()



if len(args.hash) != 32:

	print ""

	print "Enter valid MD5 Hash "

	print ""

	sys.exit()



else:

	if args.lists:

		#fx = raw_input('Please enter password List: ')

		with open(args.lists, 'r') as f:

			fox = f.read().splitlines()

			t1 = time.time()



		print ""

		sys.stdout.write("[~] Waiting crack ")

		for n in range(3):



			sys.stdout.write(".")

			sys.stdout.flush()

			time.sleep(0.5)



		count = 0

		for i in fox:

			t2 = time.time()

			count = count + 1

			back = hashlib.md5(i).hexdigest()

	

			if args.hash == back:

				print ""

				print "[+] Your Hash: %s" % args.hash

				print "[+] Total Pass: %s" % str(count)

				print "[+] Password Crack Selesai: " + str(i)

				print "[+] Durasi: %s" % str(t2 - t1)

				print ""

				sys.exit()



		if args.hash != back:

			print ""

			print "[-] MD5: " + args.hash

			print "[-] Total Passwords: %s " % count

			print "[-] Duration: %s" % str(t2-t1) 

			print "[-] Status: Password Not Avaible On Your List"		

			print ""