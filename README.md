# My Homeserver
This is my personal homeserver setup. I wanted some features and settings that i didn't find in other homeserver setups. So i decided to create my own. I'm sharing this with you so you can use it as a base for your own homeserver.

## Docker-compose Stack Structure

| Service               | Dns Url         | External Port | Internal Port |
|-----------------------|-----------------|---------------|---------------|
| swag                  | www.*           | 80,443        | 80,443        |
| duckdns               | ---             | ---           | ---           |
| nextcloud             | nextcloud.*     | 9001          | 443           |
| jellyfin              | jellyfin.*      | 9002          | 8096          |
| homeassistant         | homeassistant.* | 9003          | 8123          |
| postgres              | ---             | 5432          | 5432          |
| esphome               | ---             | 6052          | 6052          |
| wireguard             | wireguard.*     | 51820         | 51820         |

## Features
I setup my homeserver with some specification in mind.

I wanted to install the apps in containers so i can manage them easly and i can have a better control and a modularization of the system. So i decided to use **Docker** to do so.

**Linuxserver.io** is a great source of containers, so i decided to use them as base for my containers. Here you can find their [Website](https://www.linuxserver.io/).

I wanted to have a modularization of the storage so i can add more storage easly. So i decided to use **MergerFS** to do so.

To manage the backup of the data i decided to use **SnapRAID**.

## Host configuration
I'm using Arch Linux as base OS. Then the commands and the packages are for this OS. Feel free to use any other OS by adapting the commands.

### Install the base OS
First install your base os on the server.
I'm using Arch Linux.
In my particular case i'm using an OrangePi 5B, so i'm using the specific image from the [following project from 7Ji](https://github.com/7Ji/orangepi5-archlinuxarm/)

Please follow the installation guide of your OS to get a working system before proceding.

#### Why i choosed Arch Linux?
I love how ```pacman``` manages the packages and the minimalist philosophy of Arch.
Initially i started the project with Rocky Linux, but i had some problems when i switched from a Raspberry PI 3B+ to an OrangePi 5B, so i decided to switch to Arch Linux.

You can find more info about Arch Linux on the [Arch Linux Website](https://archlinux.org/).

### SSH into the server
After the installation, you need to ssh into the server so you can do the installation process remotely.

### Installing Git
First of all we need to install git to clone this repository.
```bash 
sudo pacman -Sy git
```
then clone that repository in your prefered working directory.
```bash 
git clone https://github.com/stefaniscion/homeserver
cd homeserver
```
Done that, we can go on with the installation.

### Start setup script
To setup all base system, just run the following command:
```bash
sh setup.sh
```
Do now a reboot of the server to be sure that all packages are installed correctly.
```bash
sudo reboot
```

### Mounting the storages and set up MergerFS
Now we need to mount the storage and set up MergerFS.
First of all we need to create the mount points for the storage.
Edit the file /etc/fstab and add the following lines for each physical drive:
```
UUID={diskuuid} /mnt/data/data1 ext4 defaults,nofail 0 0
UUID={diskuuid} /mnt/data/data2 ext4 defaults,nofail 0 0
UUID={diskuuid} /mnt/parity/parity1 ext4 defaults,nofail 0 0
```
Where {diskuuid} is the UUID of the disk. You can find it with the command:
```bash
sudo blkid
```
You ned now to create the mount points directories:
```bash
sudo mkdir /mnt/data
sudo mkdir /mnt/data/data1
sudo mkdir /mnt/data/data2
sudo mkdir /mnt/parity
sudo mkdir /mnt/parity/parity1
```
Also check for permission, i sudgest to give the permission to the user that will run the containers, i will use the user with uid 1000 and gid 1000.
```bash
sudo chown -R 1000:1000 /mnt/data/*
sudo chown -R 1000:1000 /mnt/parity/*
```
You can test the configuration the command:
```bash
sudo systemctl daemon-reload
sudo mount -a
```
Now we need to create the mount point for the MergerFS pool. Edit the file /etc/fstab and add the following line:
```
/mnt/data/* /mnt/merger fuse.mergerfs cache.files=partial,dropcacheonclose=true,category.create=mfs,func.getattr=newest,uid=1000,gid=1000 0 0
```
Again you need to create the mount point directory:
```bash
sudo mkdir /mnt/merger
```
Then you can test the configuration with the command:
```bash
sudo systemctl daemon-reload
sudo mount -a
```

### Setup SnapRaid
Now we need to setup SnapRaid.
First of all we need to create the configuration file, that will be located in /etc/snapraid.conf.
I made an example file for the case below.
```
parity /mnt/parity/parity1/snapraid.parity
data data1 /mnt/data/data1/
data data2 /mnt/data/data2/
content /mnt/data/data1/snapraid.content
content /mnt/data/data2/snapraid.content
```

## Docker configuration

### Create .env file
Now we need to create the .env file in the project directory, with the secret used by the Docker-compose, with the following data:
```
HOMESERVER_URL=
DUCKDNS_TOKEN=
NEXTCLOUD_DB_ROOT_PASSWORD=
STORAGE_PATH=
CONFIG_PATH=
```
This data will be used by the Docker-compose to setup the containers.

### Start the stacks
Now we can start the stacks with the command:
```bash
sh start.sh
```
the script will launch the docker-compose commands to start the stacks.

### SWAG
Now you need to create the needed confs for the other services, so go to the ```config/nginx/proxy-confs``` folder and create the needed confs. 

You can find some examples like in the ```config/nginx/proxy-confs/nextcloud.subdomain.conf.sample``` file.

Any of the following services need a subdomain, so you need to create a subdomain for each service you want to use.

You also need to change the port to connect to the service. Refer to the docker-compose files to see the port used by the service.

### Duckdns
Duckdns shouldn't need any specific configuration.

### Nextcloud
First you need to connect your Nextcloud instance to the database. To do so, you need to go to the address https://localhost:9001 and create a SQLite database.

Then you need to create the admin user and password.

#### Nextcloud sync with filesystem
I made the following tuning to the Nextcloud instance:
in ```config/www/nextcloud/config/config.php``` i added the following line to enable the filesystem file edit check.:
```
   'filesystem_check_changes' => 1,
```

#### Nextcloud file upload limits
I added the following lines to the ```config/php/php-local.ini``` file, to increase the upload size limit:
```
php_value upload_max_filesize 16G
php_value post_max_size 16G
php_value max_input_time 3600
php_value max_execution_time 3600
```
and for the same reason, for the chunk assembly timeout, i added the following line to the ```config/nginx/site-confs/default.conf``` file:
```
fastcgi_read_timeout 3600s;
```

Refear to the [this page](https://docs.nextcloud.com/server/latest/admin_manual/configuration_files/big_file_upload_configuration.html) for more info.

### Jellyfin
First you need to connect your Jellyfin instance to the database. To do so, you need to go to the address https://localhost:9002 and follow up the first setup by configuring your admin user and password and creating a media library.

### Homeassistant
Homeassistant needs to be configured to be used with a reverse proxy.
To do so, you need to add the following lines to the ```config/homeassistant/configuration.yaml``` file:
```yml
http:
  use_x_forwarded_for: true
```

## Add a service
If you want to add a service you have follow some steps.

### add the service yml in services folder
First you need to create the service yml file in the services folder that contains the docker-compose yml code specific to that service.
By defauly you have to specify the following parameters:
```
networks:
  - homeserver
```

### Add the service to the docker-compose.yml file
Then you need to add the service to the docker-compose.yml file in the root of the project, linking the service yml file.

### Add secrets to the .env file
You also need to add the secrets needed by the service to the .env file.

## Usage
You can now connect to all the services with the subdomain you created.

## TODO
- Add snapraid cron configuration
