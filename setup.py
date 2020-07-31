from os import system

system("sudo apt-get install squid -y")
system("mkdir /build ")
system("mkdir /build/data ")
system("cp redirector.py /build/")
system('cp -rf squid.conf /etc/squid/')
system('cp config.json /build/data/')
system("chmod -R 777 /build")
system("systemctl restart squid")
