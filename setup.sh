# UTILS
sudo dnf install wget -y

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
sudo dnf install fuse -y
wget https://github.com/trapexit/mergerfs/releases/download/2.35.1/mergerfs-2.35.1-1.fc33.aarch64.rpm
sudo rpm -i mergerfs-2.35.1-1.fc33.aarch64.rpm
sudo rm mergerfs-2.35.1-1.fc33.aarch64.rpm
# snapraid
echo "* installing snapraid"
wget https://rpmfind.net/linux/epel/testing/7/aarch64/Packages/s/snapraid-11.2-1.el7.aarch64.rpm
sudo rpm -i snapraid-11.2-1.el7.aarch64.rpm
sudo rm snapraid-11.2-1.el7.aarch64.rpm


# CONTAINERS TOOLS
# podman
echo "* installing cockpit"
sudo dnf install podman -y
# docker-compose
echo "* installing podman-compose"
sudo dnf install podman-compose -y
echo "* done!"
#sudo reboot
