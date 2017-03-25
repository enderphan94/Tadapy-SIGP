Tadaypy - Smart Information Gathering Python (SIGP)

# Usage

usage: tada.py [-h] [-a ALL] [-u URL]

optional arguments:

  -h, --help         show this help message and exit
  
  -a ALL, --all ALL  list of domain names
  
  -u URL, --URL URL  Enter a domain name

# Examples

+ Single URL:

    ` python tada.py -u domain.com`

+ Scan with a list:

    ` python tada.py -a listdomain.txt`

# Functions
## WHO IS

It will returns information about registered domain names, including the name servers they are configured to work with

## Dig and host list

Dig will let you perform any valid DNS query, the most common of which are:

1) A (the IP address),

2) TXT (text annotations),

3) MX (mail exchanges), and

4) NS nameservers.

## TCP traceroute

Use the specified interface for outgoing packets

## DNS Enumeration

1) Get the host's addresse (A record).

2) Get the namservers (threaded).

3) Get the MX record (threaded).

4) Perform axfr queries on nameservers and get BIND VERSION (threaded).

5) Get extra names and subdomains via google scraping
   (google query = "allinurl: -www site:domain").

6) Brute force subdomains from file, can also perform recursion
      on subdomain that have NS records (all threaded).

7) Calculate C class domain network ranges and perform whois
         queries on them (threaded).

8) Perform reverse lookups on netranges
   ( C class or/and whois netranges) (threaded).

## Fierce

Fierce is a semi-lightweight scanner that helps locate non-contiguous IP space and hostnames against specified domains.

It's really meant as a pre-cursor to nmap, unicornscan, nessus, nikto, etc, since all of those require that you already know what IP space you are looking for.

This does not perform exploitation and does not scan the whole internet indiscriminately. It is meant specifically to locate likely targets both inside and outside a corporate network.

Because it uses DNS primarily you will often find mis-configured networks that leak internal address space. That's especially useful in targeted malware

## Nmap

1) Scan fewer ports than the default scan

2) Scan 100 most common ports (Fast)

3) Detect OS and Services 

4) More aggressive Service Detection

5) prohibits the dynamic scan delay from exceeding 10 ms for TCP ports




