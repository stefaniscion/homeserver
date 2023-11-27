# UPDATE SYSTEM
echo "***** updating system"
sudo dnf update -y
echo "***** installing epel repos"
sudo dnf config-manager --set-enabled crb
sudo dnf install \
    https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm \
    https://dl.fedoraproject.org/pub/epel/epel-next-release-latest-9.noarch.rpm

# UTILS
sudo dnf install wget -y

## DASHBOARD TOOLS
#echo "***** installing cockpit"
#sudo dnf install cockpit -y
#sudo systemctl enable --now cockpit.socket
#sudo firewall-cmd --add-service=cockpit --permanent
#sudo firewall-cmd --reload
#sudo dnf install cockpit-storaged cockpit-networkmanager cockpit-packagekit cockpit-podman cockpit-selinux cockpit-sosreport  -y

# FILESYSTEM TOOLS
echo "***** installing mergerfs"
sudo dnf install fuse -y
wget https://github.com/trapexit/mergerfs/releases/download/2.35.1/mergerfs-2.35.1-1.fc33.aarch64.rpm
sudo rpm -i mergerfs-2.35.1-1.fc33.aarch64.rpm
sudo rm mergerfs-2.35.1-1.fc33.aarch64.rpm
echo "***** installing snapraid"
sudo dnf install snapraid

# CONTAINERS TOOLS
sudo dnf install -y yum-utils
sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo systemctl --now enable docker
sudo groupadd docker
sudo usermod -aG docker $USER


#echo "***** installing podman"
#sudo dnf install podman -y
#echo "***** installing podman-compose"
#sudo dnf install podman-compose -y

# FINALIZING
echo "***** done!"
#sudo reboot
