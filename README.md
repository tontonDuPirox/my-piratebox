My-piratebox
============

Fork de rlespinasse/my-piratebox

Distribué sans aucune garantie.

Screenshots
===========

Homepage
--------

![ScreenShot](https://raw.github.com/tontonDuPirox/my-piratebox/master/screens/screen-home.png)

Fichiers
--------

![ScreenShot](https://raw.github.com/tontonDuPirox/my-piratebox/master/screens/screen-shared.png)

Forum
-----

![ScreenShot](https://raw.github.com/tontonDuPirox/my-piratebox/master/screens/screen-forum.png)

Chat
----

![ScreenShot](https://raw.github.com/tontonDuPirox/my-piratebox/master/screens/screen-chat.png)

A propos
--------

![ScreenShot](https://raw.github.com/tontonDuPirox/my-piratebox/master/screens/screen-about.png)

Installation
============

1) Installer la piratebox

    Suivre le tutoriel de David Darts : 
    http://daviddarts.com/piratebox-diy-openwrt/?title=PirateBox_DIY_OpenWrt

2) Télécharger l'archive et la décompresser

    wget https://github.com/tontonDuPirox/my-piratebox/archive/master.zip && unzip master.zip

3) Se connecter à la piratebox

4) Copier les fichiers vers la piratebox

    scp -r ./my-piratebox-master/opt/piratebox/* root@192.168.1.1:/opt/piratebox/

5) Se connecter en ssh à la piratebox

    ssh root@192.168.1.1

6) Redémarrer le service piratebox

    /etc/init.d/piratebox stop

    /etc/init.d/piratebox start
