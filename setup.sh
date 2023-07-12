# DASHBOARD TOOLS
# cockpit
echo "* installing cockpit"
sudo dnf install cockpit -y
sudo systemctl enable --now cockpit.socket
sudo firewall-cmd --add-service=cockpit --permanent
sudo firewall-cmd --reload

# FILESYSTEM TOOLS
# mergerfs
echo "* installing mergerfs"
sudo dnf install mergerfs -y
# snapraid
echo "* installing snapraid"
sudo dnf install snapraid -y
echo "* done!"

# CONTAINERS TOOLS
# podman
echo "* installing cockpit"
sudo dnf install podman -y
# docker-compose
echo "* installing docker-compose"
sudo dnf install docker-compose -y

#sudo reboot