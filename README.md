# My Homeserver

## Installation
I'm using Rocky Linux (9) as base OS. Then the commandands and the packages are for this OS. Feel free to use any other OS bya adapting the commands. 
### Install the Base OS
First install your base os on the server.
I'm using Rocky Linux.
#### Why Rocky Linux?
I love how YUM and DNF manages the packages Sadly i think that CentOS is not anymore a good choice for a server. So i decided to use Rocky Linux.
You can find more info about Rocky Linux [here](https://rockylinux.org/).
### SSH into the server
After the installation, you need to ssh into the server so you can do the installation process remotely.
### Installing Git
First of all we need to install git to clone this repository.
```bash 
sudo dnf install git
```
then clone that repository in your prefered working directory.
```bash 
git clone https://github.com/stefaniscion/homeserver
```
Done that, we can go on with the installation.
### Do setup
To setup all base system, just run the following command:
```bash
sh setup.sh
```
Do now a reboot of the server to be sure that all packages are installed correctly.