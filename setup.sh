read -p "Do you want to install the Stefaniscion's Homeserver? " -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
    echo "***** updating system"
    sudo pacman -Syu --noconfirm

    echo "***** installing utility packages"
    sudo pacman -Sy wget htop --noconfirm
    sudo pacman -S --needed base-devel --noconfirm

    echo "***** installing yay"
    git clone https://aur.archlinux.org/yay.git
    cd yay
    makepkg -si  --noconfirm
    cd ..
    rm -rf yay

    echo "***** installing mergerfs"
    yay -Sy mergerfs fuse2 --noconfirm

    echo "***** installing snapraid"
    yay -Sy snapraid --noconfirm

    echo "***** installing docker"
    sudo pacman -Sy docker docker-compose --noconfirm
    sudo usermod -aG docker $USER
    sudo systemctl enable docker.service
    
    echo "***** Rebooting"
    sudo reboot
fi


