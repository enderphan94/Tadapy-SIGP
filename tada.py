import re
from sys import argv
from os.path import exists
import optparse
import argparse
import sys
from subprocess import call
from termcolor import colored
import os
import io

parser = argparse.ArgumentParser()
parser.add_argument(
        '-a',
        '--all',
        help='list of domain names',
        required=False)
parser.add_argument(
        '-u',
        '--URL',
        help='Enter a domain name',
        required=False)

args = parser.parse_args()

list = args.all
sig  = args.URL


if sig is not None:
    print colored("\n===============WHO IS===============",'red')
    call(["whois",sig])
    print colored("\n===============DIG and HOST LIST===============",'red')
    call(["dig",sig,"any"])
    print "\n"
    call(["host","-l",sig])
    print colored("\n===============TCP Traceroute===============\n",'red')
    call(["ifconfig","-s"])
    print "\nEnter your Network interface is active"
    inter = raw_input()
    print "\n"
    call(["tcptraceroute","-i",inter,sig])
    print colored("\n===============DNS enumeration=============== \n",'red')
    os.system("perl tools/dnsenum.pl --enum -f tools/dns.txt --update a -r "+sig)
    print colored("\n===============NMAP===============\n",'red')
    os.system("nmap -PN -n -F -T4 -sV --version-intensity 5 -A "+sig)

    

if list is not None:
    if not os.path.exists("database"):
        os.system("mkdir database")
    with open(list) as l:
        for line in l:
                line = line.strip()
                file = line+".txt"
                nmap_file = line+".nmap.xml"
                os.system("echo ===============WHOIS=============== >> "+file) 
                os.system("whois "+line+" >> "+file)
                os.system("echo ===============DIG and HOST LIST=============== >> "+file)
                os.system("dig "+line+" >> "+file)
                os.system("echo ===============DNS enumeration=============== >> "+file)
                os.system("perl tools/dnsenum.pl --enum -f tools/dns.txt --update a -r "+line+" 1>> "+file)
                os.system("nmap -PN -n -F -T4 -sV --version-intensity 5 -A "+line+" -oX "+nmap_file)
                os.system("mv "+file+" database/")
                os.system("mv "+nmap_file+" database/")
    print colored("\nCheck output from database/ folder",'red')
