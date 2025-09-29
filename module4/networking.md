<!-- Slide number: 1 -->
# Networking
Basics
Hants Williams, PhD, RN

<!-- Slide number: 2 -->
# Basics

<!-- Slide number: 3 -->
Software stack (web): Frontend

![Image](Image.jpg)

<!-- Slide number: 4 -->

![Image](Image.jpg)
FRONTEND
APIs
BACKEND
Front end: The software development that happens on the user-side. When you interact with buttons, forms, input boxes, images, banners and other elements of a webpage on a browser, all of this falls under the purview of the front-end developer.

<!-- Slide number: 5 -->

![Screen Shot 2022-09-06 at 8.55.35 AM.png](ScreenShot20220906at85535AMpng.jpg)

<!-- Slide number: 6 -->

![Image](Image.jpg)

Networking

<!-- Slide number: 7 -->
How do computers talk to one another?

Networking basics…

<!-- Slide number: 8 -->

![Image](Image.jpg)

![Image](Image.jpg)

<!-- Slide number: 9 -->

![Image](Image.jpg)
Nurse workstation
Hospital EMR

![Image](Image.jpg)

![Image](Image.jpg)
ISP
COX

ISP

AT&T

![Image](Image.jpg)
ISP
Comcast

<!-- Slide number: 10 -->
Networking Protocols

International Standards Organization's Open Systems Interconnection (OSI): 7 layers

![Screen Shot 2022-02-22 at 9.24.55 AM.png](ScreenShot20220222at92455AMpng.jpg)

![Screen Shot 2022-02-22 at 9.24.22 AM.png](ScreenShot20220222at92422AMpng.jpg)
(Frontend)

TCP is used for organizing data in a way that ensures the secure transmission between the server and client.
https://www.ibm.com/docs/no/aix/7.1?topic=networks-

<!-- Slide number: 11 -->

![Image](Image.jpg)

<!-- Slide number: 12 -->

![networking-packtrav-encap-decap.gif](networkingpacktravencapdecapgif.jpg)
Layer 4 will add a TCP header which would include a Source and Destination port
Layer 3 will add an IP header which would include a Source and Destination IP address
Layer 2 would add an Ethernet header which would include a Source and Destination MAC address
Ethernet Frame

![Image](Image.jpg)

<!-- Slide number: 13 -->
# Network layer

<!-- Slide number: 14 -->

![Screen Shot 2022-02-22 at 11.26.48 AM.png](ScreenShot20220222at112648AMpng.jpg)

![Image](Image.jpg)
An Internet Protocol (IP) address is a unique identifier assigned to a device or domain that connects to the Internet.

The fourth version of IP (IPv4 for short) was introduced in 1983

<!-- Slide number: 15 -->
Private IP - set by router / dynamically

![Image](Image.jpg)
Public IP: set by ISP

<!-- Slide number: 16 -->
Local applications:
0.0.0.0
127.0.0.1

Local Router
192.168.1.1

<!-- Slide number: 17 -->

![Image](Image.jpg)
IP data = TCP/UDP segment/packet

<!-- Slide number: 18 -->
IP packet

![Image](Image.jpg)

<!-- Slide number: 19 -->
# Simplifying the communication
DNS: Domain Name Service

![Screen Shot 2022-02-22 at 9.47.00 AM.png](ScreenShot20220222at94700AMpng.jpg)

![Image](Image.jpg)

![Image](Image.jpg)

<!-- Slide number: 20 -->
# Ports

<!-- Slide number: 21 -->

![Image](Image.jpg)
A port is a numerical identifier in networking used to facilitate communication between different applications or services. It allows data to be directed to the correct application at the application layer of networking.

![Screen Shot 2022-02-22 at 9.24.55 AM.png](ScreenShot20220222at92455AMpng.jpg)

![Screen Shot 2022-02-22 at 9.31.02 AM.png](ScreenShot20220222at93102AMpng.jpg)

<!-- Slide number: 22 -->

![Screen Shot 2022-02-22 at 9.30.19 AM.png](ScreenShot20220222at93019AMpng.jpg)

![Screen Shot 2022-02-22 at 9.30.04 AM.png](ScreenShot20220222at93004AMpng.jpg)
https://secbot.com/docs/ports/common-ports

<!-- Slide number: 23 -->

![Screenshot 2024-09-23 at 5.25.05 PM.png](Screenshot20240923at52505PMpng.jpg)

![Screenshot 2024-09-23 at 5.24.38 PM.png](Screenshot20240923at52438PMpng.jpg)
https://secbot.com/docs/ports/common-ports

<!-- Slide number: 24 -->
# Transport Layers

<!-- Slide number: 25 -->
Transmission control protocol (TCP) and Use Datagram Protocol (UDP)
Both TCP and UDP help in converting the data into smaller units referred to as units.

Data units include details such as: — the IP addresses of the respective sender and the receiver, the data that is to be transferred, multiple configurations, and the trailer (data which refers to the end of the packet).

One of the most common difference between the TCP and UDP protocols is the way that data is being transferred: handshake vs no handshake

![Screenshot 2023-02-21 at 8.12.35 AM.png](Screenshot20230221at81235AMpng.jpg)

![Screenshot 2023-02-21 at 8.12.35 AM.png](Screenshot20230221at81235AMpng.jpg)

<!-- Slide number: 26 -->

![Image](Image.jpg)

![Image](Image.jpg)

![Image](Image.jpg)

<!-- Slide number: 27 -->
3 Way Handshake
SYN, SYN-ACK, and ACK for SYNchronize, SYNchronize-ACKnowledgement, and ACKnowledge

It is a three-step process that requires both the client and server to exchange synchronization and acknowledgment packets before the real data communication process starts

![Image](Image.jpg)
| Message | Description |
| --- | --- |
| Syn | Used to initiate and establish a connection. It also helps you to synchronize sequence numbers between devices. |
| ACK | Helps to confirm to the other side that it has received the SYN. |
| SYN-ACK | SYN message from local device and ACK of the earlier packet. |
| FIN | Used to terminate a connection. |

<!-- Slide number: 28 -->

![Image](Image.jpg)
Sequence number – A device initiating a TCP connection must choose a random initial sequence number, which is then incremented according to the number of transmitted bytes.

Acknowledgment number – The receiving device maintains an acknowledgment number starting with zero. It increments this number according to the number of bytes received.

TCP data offset – This specifies the size of the TCP header, expressed in 32-bit words. One word represents four bytes.

Reserved data – The reserved field is always set to zero.

Control flags – TCP uses nine control flags to manage data flow in specific situations, such as the initiating of a reset.

Window size TCP checksum – The sender generates a checksum and transmits it in every packet header. The receiving device can use the checksum to check for errors in the received header and payload.

Urgent pointer – If URG control flag is set, this value indicates an offset from the sequence number, indicating the last urgent data byte.

Metadata

<!-- Slide number: 29 -->

![Image](Image.jpg)
The first four bytes of the UDP header store the port numbers for the source and destination.

The next two bytes of the UDP header store the length (in bytes) of the segment (including the header).

The final two bytes of the UDP header is the checksum, a field that's used by the sender and receiver to check for data corruption.

<!-- Slide number: 30 -->

![Image](Image.jpg)

![Screen Shot 2022-02-22 at 9.31.02 AM.png](ScreenShot20220222at93102AMpng.jpg)

<!-- Slide number: 31 -->

![Screen Shot 2022-02-22 at 9.30.19 AM.png](ScreenShot20220222at93019AMpng.jpg)

![Screen Shot 2022-02-22 at 9.30.04 AM.png](ScreenShot20220222at93004AMpng.jpg)
https://secbot.com/docs/ports/common-ports

<!-- Slide number: 32 -->
# DNS Specifics

<!-- Slide number: 33 -->
# Internet Names and Addresses

Addresses, e.g. 129.10.117.100
Computer usable labels for machines
Conform to structure of the network
Names, e.g. www.stonybrook.edu
Human usable labels for machines
Conform to organizational structure
How do you map from one to the other?
Domain Name System (DNS)

<!-- Slide number: 34 -->

![Screenshot 2024-09-23 at 5.18.15 PM.png](Screenshot20240923at51815PMpng.jpg)
# History

Before DNS, all mappings were in hosts.txt
/etc/hosts on Linux
C:\Windows\System32\drivers\etc\hosts on Windows
Centralized, manual system
Changes were submitted to Network Information Center (NIC) via email - managed via Stanford Research Institute (SRI)   (https://www.sri.com/hoi/domain-names-the-network-information-center/)
Machines periodically FTP new copies of hosts.txt
Administrators could pick names at their discretion
Any name was allowed
alans_server_at_sbu_pwns_joo_lol_kthxbye

<!-- Slide number: 35 -->
# Towards DNS

Eventually, the hosts.txt system fell apart
Not scalable, SRI couldn’t handle the load
Hard to enforce uniqueness of names
e.g MIT
Massachusetts Institute of Technology?
Melbourne Institute of Technology?
Manhattan Institute of Technology?
Many machines had inaccurate copies of hosts.txt
Thus, DNS was born

<!-- Slide number: 36 -->
# DNS at a High-Level

Domain Name System = DNS
Distributed database
No centralization
Simple client/server architecture
port 53
Hierarchical namespace
.com  google.com  mail.google.com

<!-- Slide number: 37 -->
# Naming Hierarchy

Root

net
edu
com
gov
mil
org
uk
fr
etc.
Top Level Domains (TLDs) are at the top
Every node in the DNS tree can be identified by Fully Qualified Domain Name (FQDN)
mail, stonybrook, edu
Each label can be up to 63 characters long.
The total number of characters of a DNS name is limited to 255
Can contains characters, numerals, and dash character (“-”)
Are not case-sensitive
Each Domain Name is a subtree
.edu  stonybrook.edu   mail.stonybrook.edu
Name collisions are avoided
stonybrook.com vs. stonybrook.edu

NYU
SBU

mail
it
library

<!-- Slide number: 38 -->
# Top Level Domains
Three types of top-level domains:
Generic Top Level Domains (gTLD): 3-character code indicates the function of the organization
Used primarily within the US
Examples: gov, mil, edu, org, com, net –
Country Code Top Level Domain (ccTLD): 2- character country or region code
Examples: us, va, jp, de
Infrastructure top level domains: A special domain (in-addr.arpa) used for IP address-to-name mapping
https://www.iana.org/domains/arpa

More than 1000+ top level domains
https://data.iana.org/TLD/tlds-alpha-by-domain.txt
https://www.iana.org/domains/root/files

<!-- Slide number: 39 -->
# Hierarchical Administration

Internet Corporation for Assigned Names and Numbers
Root

ICANN

Verisign/GoDaddy/AWS/etc….

net
edu
com
gov
mil
org
uk
fr
etc.
Tree is divided into zones
Each zone has an administrator (e.g., IT team)
Responsible for the part of the hierarchy
Example:
SBU IT controls *.stonybrook.edu
Columbia IT controls *.columbia.edu

NYU
SBU

<!-- Slide number: 40 -->
# Server Hierarchy

Root servers know about all TLDs
The buck stops at the root servers

Functions of each DNS root server:
Store all the records for hosts/domains in its zone
May be replicated for robustness
Know the addresses of the root servers
Resolve queries for unknown names

<!-- Slide number: 41 -->
# Root Name Servers
Responsible for the Root Zone File
Administered by ICANN (Internet Corporation for Assigned Names and Numbers)
13 root servers, labeled AM
Used to be under the oversight of US government
By Oct 1, 2016, free of it
Are globally replicated

![Picture 2](Picture2.jpg)

<!-- Slide number: 42 -->
# Address of Root Servers

![Content Placeholder 7](ContentPlaceholder7.jpg)

<!-- Slide number: 43 -->
https://www.internic.net/domain/root.zone

![Screen Shot 2022-11-07 at 5.41.34 PM.png](ScreenShot20221107at54134PMpng.jpg)
https://www.iana.org/domains/root/db
https://www.iana.org/domains/root/db/edu.html

![Screen Shot 2022-11-07 at 5.42.09 PM.png](ScreenShot20221107at54209PMpng.jpg)

<!-- Slide number: 44 -->
# Local Name Servers

Where is google.com?

![Picture 2](Picture2.jpg)

Optimum

![Picture 3](Picture3.jpg)

![Picture 2](Picture2.jpg)

![Picture 2](Picture2.jpg)
Each ISP/company has a local, default name server
Optimum: 167.206.112.138
Hosts begin DNS queries by contacting the local name server (e.g., Optimum)
The ISP/company will cache query results to optimize speed

<!-- Slide number: 45 -->
# Basic Domain Name Resolution

Every host knows a local DNS server
Sends all queries to the local DNS server
If the local DNS can answer the query, then you’re done
Otherwise, go down the hierarchy and search for the authoritative name server
Every DNS server knows the root servers
Use cache to skip steps if possible
e.g. skip the root and go directly to .edu if the root file is cached

<!-- Slide number: 46 -->

www.stonybrook.edu = 129.49.22.66

Where is www.stonybrook.edu?
www.stonybrook.edu

![Picture 2](Picture2.jpg)

StonyBrook

![Picture 3](Picture3.jpg)

![Picture 3](Picture3.jpg)

![Picture 3](Picture3.jpg)

Local DNS (Optimum)
Root
edu
sbu

Authority for ‘edu’ (TLD)

Authority for ‘stonybrook.edu’
Stores the nameIP mapping for a given host
https://www.educause.edu/
https://whois.domaintools.com/stonybrook.edu

<!-- Slide number: 47 -->
# DNS Resource Records

DNS queries have two fields: name and type
Resource record is the response to a query
Four fields: (name, value, type, TTL)
Name: what people will see
Value: typically where it is directed
Type: A, AAAA, NS, MX, etc…
TTL: time to live; length of cache result until query (DNS - e.g., Optimum) requests new response [shorter is better when testing…]

<!-- Slide number: 48 -->
# DNS Types

Type = A (IPv4) / AAAA (IPv6)
Name = domain name (FQDN)
Value = IP address
Type = NS
Name = partial domain
Value = name of DNS server for this domain
“Go send your query to this other server”

Name: www.hants.com
Type: A
Query

Name: www.hants.com
Value: 129.10.116.81
Resp.

Name: hants.com
Type: NS
Query

Name: hants.com
Value: 129.10.116.51
Resp.

<!-- Slide number: 49 -->
# DNS Types, Continued

Type = CNAME
Name = hostname
Value = canonical hostname
Useful for aliasing
Type = MX
Name = domain in email address
Value = canonical name of mail server

![Image](Image.jpg)

Name: pssp.hants.com
Type: CNAME
Query

Name: pssp2.hants.com  Value: pssp2.hants.com
Resp.

<!-- Slide number: 50 -->
# Aliasing and Load Balancing

One machine can have many aliases
david.choffnes.com
www.reddit.com

![Picture 2](Picture2.jpg)
alan.mislo.ve
www.foursquare.com

www.huffingtonpost.com

*.blogspot.com
One domain can map to multiple machines

![Picture 2](Picture2.jpg)

![Picture 2](Picture2.jpg)

www.google.com

![Picture 2](Picture2.jpg)

![Picture 2](Picture2.jpg)

<!-- Slide number: 51 -->
# Much More to DNS

Caching: when, where, how much, etc.
Other uses for DNS (i.e. DNS hacks)
Content Delivery Networks (CDNs)
Different types of DNS load balancing
Dynamic DNS (e.g. for mobile hosts)
DNS and botnets
Politics and growth of the DNS system
Governance
New TLDs (.xxx, .biz), eliminating TLDs altogether
Copyright, arbitration, squatting, typo-squatting

<!-- Slide number: 52 -->
# Applied Networking with a basic web app (website)

<!-- Slide number: 53 -->
# Development Frontend Basics
Web

![Screen Shot 2022-02-22 at 8.39.53 AM.png](ScreenShot20220222at83953AMpng.jpg)
TCP :80 :443
stonybrook.edu
TCP :53
ping???

<!-- Slide number: 54 -->

![Screen Shot 2022-09-06 at 8.55.35 AM.png](ScreenShot20220906at85535AMpng.jpg)

<!-- Slide number: 55 -->
HTTP: Hypertext Transfer Protocol

![Image](Image.jpg)
HTTP stands for hypertext transfer protocol and is used to transfer data across the Web.
The client makes a request and the server responds.

<!-- Slide number: 56 -->

![Image](Image.jpg)
http is the transfer protocol that transfer the resource (web page,image,video etc) from the server to the client.

<!-- Slide number: 57 -->
# Primary Components of HTTP:

HTTP version
URL
Method
Request headers
Body

<!-- Slide number: 58 -->
# HTTP versions

![Image](Image.jpg)
In 1989, Tim Berners-Lee invented HTTP. HTTP/1.1 was its 1st standardized version that was available for use in the year 1997 for the end-users. HTTP/1 was known to have poor response time. With websites becoming more resource-intensive, the protocol was losing its efficiency. It progressively became essential to minimize latency and boost page load speeds.

Google looked into these problems. And as expected, SPDY - an experimental project to end troubles with HTTP/1.x – was put into trial in the year 2010.

<!-- Slide number: 59 -->

![Image](Image.jpg)

![Image](Image.jpg)
This NeXT Computer was used by Berners-Lee at CERN and became the world's first web server
https://en.wikipedia.org/wiki/CERN_httpd

<!-- Slide number: 60 -->
Many (HTTP/1.1) versus One (HTTP/2) Connections to Server

![Image](Image.jpg)

<!-- Slide number: 61 -->
HTTP/HTTPS and URL

![Screen Shot 2022-09-06 at 9.09.11 AM.png](ScreenShot20220906at90911AMpng.jpg)

![Screen Shot 2022-09-06 at 9.09.11 AM.png](ScreenShot20220906at90911AMpng.jpg)

![Screen Shot 2022-09-06 at 9.10.30 AM.png](ScreenShot20220906at91030AMpng.jpg)

![Screen Shot 2022-09-06 at 9.10.30 AM.png](ScreenShot20220906at91030AMpng.jpg)

![Image](Image.jpg)

![Image](Image.jpg)

![Image](Image.jpg)

<!-- Slide number: 62 -->
Methods (CRUD)

![Image](Image.jpg)

![Image](Image.jpg)

<!-- Slide number: 63 -->

![Image](Image.jpg)
# Request headers
HTTP headers let the client and the server pass additional information with an HTTP request or response.

An HTTP header consists of its case-insensitive name followed by a colon (:), then by its value.

Accept-Language: en-US,en;q=0.5

Accept: text/html;

<!-- Slide number: 64 -->

![Image](Image.jpg)
# Body
Text
Javascript
JSON
HTML
XML
Form-Data
x-www-form-urlencoded

![Image](Image.jpg)

<!-- Slide number: 65 -->
Response

![Screen Shot 2022-02-22 at 12.05.21 PM.png](ScreenShot20220222at120521PMpng.jpg)

<!-- Slide number: 66 -->
# Response
Response Status codes are split into 5 groups each group has a meaning and a three digit code.
1xx – Informational
2xx – Successful
3xx -Multiple Choice
4xx– Client Error
5xx -Server Error
https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

<!-- Slide number: 67 -->
# Example in python…get
import requests

url = "http://www.google.com"

myHeaders = {"content-type": "text"}

response = requests.get(url, headers=myHeaders)

print("Status Code", response.status_code)
print("JSON Response ", response.json())

<!-- Slide number: 68 -->
# Example in python…post
import requests

url = "https://httpbin.org/post"

data = {
    "id": 1001,
    "name": "hants",
    "passion": "coding",
}

response = requests.post(url, json=data)

print("Status Code", response.status_code)
print("JSON Response ", response.json())

<!-- Slide number: 69 -->
# Pretty preview
jsonlint.com

![Screen Shot 2022-09-06 at 3.35.48 PM.png](ScreenShot20220906at33548PMpng.jpg)

![Screen Shot 2022-09-06 at 3.35.48 PM.png](ScreenShot20220906at33548PMpng.jpg)

![Screen Shot 2022-09-06 at 3.36.09 PM.png](ScreenShot20220906at33609PMpng.jpg)

![Screen Shot 2022-09-06 at 3.36.09 PM.png](ScreenShot20220906at33609PMpng.jpg)

<!-- Slide number: 70 -->
# .TECH free domain
https://get.tech/search?campaignsearch=hantswilliams&campaign-name=Github&source=github

![Picture 5](Picture5.jpg)