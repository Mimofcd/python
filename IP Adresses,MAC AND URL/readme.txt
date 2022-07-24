IPv4 Addresses
An IP address is a unique identifier of a device on an IP network.

An IP address (IPv4) consists of 4 Bytes: 4 numbers between 0 and 255 separated by dots.
A dynamic IP Address can change every time your restart your device/reconnect to the network. Some devices can be configured on an IP network to have a static IP address: it will remain she same even if you restart your device.

As an IPv4 address consists of 4 Bytes (=32 bits), there are 232 possible IP addresses which is just under 4.3 billions IP addresses. Though this seems like a large number, we are reaching a stage where we are running out of unique IP addresses. Remember, every device (router, computer, smartphone, smartwatch, smart TV, smart speaker, etc.) connected to the Internet will have its own IP address and there are nearly 8 billions human beings on planet Earth. This is the reason why the Internet is progressively upgrading to the next generation of IP addresses: IPv6

Pv6 Addresses
To overcome the issue of the Internet running out of unique IPv4 addresses, a new format was introduced. IPv6 addresses consist of 16 Bytes (=128 bits). They are expressed in hexadecimal using 8 blocks of 2 Bytes (4 hexadecimal digits) separated by colons.
With 128 bits per IP address, we can generate 2128 unique IP addresses. That’s 340,282,366,920,938,463,463,374,607,431,768,211,456 IP addresses, more than enough to give each grain of sand on planet Earth a unique IP address!!!

MAC Addresses
A MAC address consists of 6 Bytes of Data, expressed in hexadecimal, separated using colons.
A MAC Address is static and unique for a device. It cannot change. It is hardcoded into the device by the manufacturer when the device is built. (A bit like the chassis number of a car!)

Networking equipment such as routers and switches use IP addresses and/or MAC addresses to direct traffic between computers/devices on the network.

URL: Uniform Resource Locator
A live website is hosted/stored on a webserver and consists of different files such as HTML pages, png graphics, jpg pictures, gif animations and other multimedia files (mp3 audio clips, mp4 movie clips, pdf documents etc.). These files are stored on the web server within a root folder and other subfolders. A URL is used to request a specific file (resource) stored on a web server.

A URL is used to request/locate a specific resource stored on a web server. It consists of:

The protocol used to access the web page: either HTTP or HTTPs,
The Domain Name to identify the web server,
Optional: Folder/Sub-folder structure: If the resource/file you are trying to access is not on the root folder of the website but in a sub-folder,
Optional: File name: the file name and extension of the file you are requesting. If the filename is not provided, the server will return the index.html file if it exists.
Domain Name Server
In order to connect to a website, your web-browser needs to know the IP address of the webserver where the website is hosted. However, IP address are tricky to remember (for human beings). This is why domain names were invented! Domains names such as 101computing.net or amazon.com are easy to remember. When the user types a domain name in the address bar of the browser, the browser automatically contacts a DNS server on the Internet. The DNS server will then lookup for the matching IP address for this domain name and return it to the web-browser. The web-browser will then be able to contact the webserver to request a specific page
Python Task #1
Write a python program to generate and output:

A random IPv4 address,
A random IPv6 address,
A random MAC address.
Python Task #2
Write a python program that asks the user to enter a URL. The program will then extract and output the following components of the URL:

Protocol,
Domain Name,
Folder Structure,
File name.