# Fasten-Your-Seatbelts
A School project for Cyber Sec at HvA

#upgrade All
sudo apt update && sudo apt upgrade

#remove python 2 and set it to python 3
sudo rm /user/bin/python
sudo ln -s /usr/bin/python3 /usr/bin/python

#Installing all needed packages 
sudo apt install apache2 python3-pip mariadb-server hostapd dnsmasq -y

#Creating the database
sudo mysql -u root -p 
#And now press enter en fill out the following
  CREATE DATABASE corendon;
  CREATE USER ‘admin’@’localhost’ IDENTIFIED BY ‘W@CHTW00RD123’;
  GRANT ALL PRIVILEGES ON corendon.* to ‘naam’@’localhost’;
  FLUSH PRIVILEGES;

#Setting up apache2
sudo a2dismod mpm_event && sudo a2enmod mpm_prefork cgi
sudo mv 000-default.conf /etc/apache2/sites-enabled/

#On to the AP
sudo systemctl enable hostapd && sudo systemctl unmask hostapd && sudo systemctl stop hostapd && sudo systemctl stop dnsudo smasq
sudo mv dnsmasq.conf /etc/
sudo mv hostapd.conf /etc/hostapd/
sudo mv dhcpcd.conf /etc/
