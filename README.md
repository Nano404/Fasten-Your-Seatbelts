# Fasten-Your-Seatbelts
A School project for Cyber Sec at HvA

# upgrade All
```bash 
sudo apt update && sudo apt upgrade
```

# remove python 2 and set it to python 3
```bash 
sudo rm /user/bin/python
```
```bash 
sudo ln -s /usr/bin/python3 /usr/bin/python
```

# Installing all needed packages 
```bash 
sudo apt install apache2 python3-pip mariadb-server hostapd dnsmasq -y
```

# Creating the database
```bash 
sudo mysql -u root -p 
```
pressing enter when prompted for a password(any password will do)
  ```bash 
  CREATE DATABASE corendon;
  CREATE USER ‘admin’@’localhost’ IDENTIFIED BY ‘W@CHTW00RD123’;
  GRANT ALL PRIVILEGES ON corendon.* to ‘naam’@’localhost’;
  FLUSH PRIVILEGES;
```
# Setting up apache2
```bash 
sudo a2dismod mpm_event && sudo a2enmod mpm_prefork cgi
```
```bash 
sudo mv 000-default.conf /etc/apache2/sites-available/
```
```bash 
sudo a2ensite 000-default.conf
```
```bash
sudo systemctl reload apache2
```
# Setting up the AP
```bash 
sudo systemctl enable hostapd && sudo systemctl unmask hostapd && sudo systemctl stop hostapd && sudo systemctl stop dnsmasq
```
```bash 
sudo mv dnsmasq.conf /etc/
sudo mv hostapd.conf /etc/hostapd/
sudo mv dhcpcd.conf /etc/
```
