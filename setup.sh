# installing cockpit
sudo dnf install cockpit -y
sudo systemctl enable --now cockpit.socket
#sudo firewall-cmd --add-service=cockpit --permanent
#sudo firewall-cmd --reload