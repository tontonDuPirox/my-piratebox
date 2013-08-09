My-piratebox
============


Installation
============

1) Installer la piratebox

    Suivre le tutoriel de David Darts : 
    http://daviddarts.com/piratebox-diy-openwrt/?title=PirateBox_DIY_OpenWrt

2) Télécharger l'archive et la décompresser

    wget https://github.com/corent1/my-piratebox/archive/master.zip && unzip master.zip

3) Se connecter au réseau wifi de la piratebox

4) Copier les fichiers vers la piratebox

    scp -r ./my-piratebox-master/opt/piratebox/* root@192.168.1.1:/opt/piratebox/

5) Se connecter en ssh à la piratebox

    ssh root@192.168.1.1

6) Redémarrer le service piratebox

    /etc/init.d/piratebox stop
    /etc/init.d/piratebox start
    

