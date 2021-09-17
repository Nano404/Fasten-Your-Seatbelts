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

# Installing Webserver Packages
```bash 
sudo apt install apache2 python3-pip mariadb-server php -y
```

# Creating the database
```bash 
sudo mysql -u root -p 
```
pressing enter when prompted for a password(any password will do)
  ```bash 
  CREATE DATABASE corendon;
  CREATE USER 'admin'@'localhost' IDENTIFIED BY 'W@CHTW00RD123';
  GRANT ALL PRIVILEGES ON corendon.* to 'admin'@'localhost';
  FLUSH PRIVILEGES;
```
# Setting up apache2
```bash 
sudo a2dismod mpm_event && sudo a2enmod mpm_prefork cgi
```
```bash 
sudo nano /etc/apache2/sites-enabled/000-default.conf
```
en plak daar volgende in
```bash
<VirtualHost *:443>
        ServerName 10.0.0.1
        <Directory /var/www/html>
                Options +ExecCGI
                DirectoryIndex index.html
        </Directory>
        #allows for CGI to run
        AddHandler cgi-script .py
        #allows for PHP to run inside HTML
        AddHandler application/x-httpd-php .php .html
        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html
        SSLEngine on
        SSLCertificateFile /var/www/certs/wifi.crt
        SSLCertificateKeyFile /var/www/certs/wifi.key

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```
```bash 
sudo a2ensite 000-default.conf
```
```bash
sudo systemctl reload apache2
```
# Setting up the AP
```bash
sudo apt install hostapd dnsmasq -y
rfkill unblock wlan
```
```bash 
sudo systemctl unmask hostapd
sudo systemctl enable hostapd
```
Add the following at the end of the file
```bash
sudo nano /etc/dhcpcd.conf
```
```bash
interface wlan0
    static ip_address=10.0.0.1/24
    nohook wpa_supplicant
```
Open dit bestand en plak daarna het onderstaande in dit voert het internet door
```bash
sudo nano /etc/sysctl.d/routed-ap.conf
```
this will add forwarding capabilitaties to the AP
```bash
net.ipv4.ip_forward=1
```
close and open an other file
```bash
sudo nano /etc/dnsmasq.conf
```
add this to the file
```bash
interface=wlan0
dhcp-range=10.0.0.2,10.0.0.250,255.255.255.0,12h
dhcp-option=3,10.0.0.1
dhcp-option=6,10.0.0.1
server=1.1.1.3
server=1.1.1.2
log-queries
listen-address=127.0.0.1
```
```bash
sudo nano /etc/hostadp/hostapd.conf
```
```bash
interface=wlan0
ssid=My_AP
hw_mode=g
channel=6
auth_algs=1
wmm_enabled=0
```
# Iptables
```bash
sudo DEBIAN_FRONTEND=noninteractive apt install -y netfilter-persistent iptables-persistent
```
```bash
sudo iptables -A POSTROUTING -t nat -o eth0 -j MASQUERADE
sudo iptables -t mangle -N internet
sudo iptables -t mangle -A PREROUTING -i wlan0 -p tcp -m tcp --dport 80 -j internet
sudo iptables -t mangle -A PREROUTING -i wlan0 -p tcp -m tcp --dport 443 -j internet
sudo iptables -t mangle -A internet -j MARK --set-mark 99
sudo iptables -t nat -A PREROUTING -i wlan0 -p tcp -m mark --mark 99 -m tcp --dport 80 -j DNAT --to-destination 10.0.0.1
sudo iptables -t nat -A PREROUTING -i wlan0 -p tcp -m mark --mark 99 -m tcp --dport 443 -j DNAT --to-destination 10.0.0.1
```
```bash
sudo netfilter-persistent save
```
