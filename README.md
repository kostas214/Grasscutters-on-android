# Grasscutters-on-android
### A comprehensive guide on how to run the grasscutters server locally on your android device 
## **READ ALL THE INSTRUCTIONS CAREFULLY BEFORE STARTING**

Client installation (If you have played on yuuki before you can skip this part)
1. Go to [ps.yuuki.me](https://ps.yuuki.me/game/genshin-impact) and download the android 4.0 client for genshin impact
2. Install the .apk and open it
3. You need to log onto the yuuki servers at least (make an account [here](https://ps.yuuki.me/account/register?type=web)
4. Log in in genshin impact and wait for the download to complete (you can leave the app and the download will continue)

## Server Installation 
1. Download and install F-droid [here](https://f-droid.org/)
2. Open F-droid and search for "Nix-on-Droid" and install the app
3. Open Nix-on-Droid
4. When you first open the application it may ask you for notifications permission (android 13 and up) and a prompt for "Bootstrap zipball location" will appear and you need to click on yes (The bootstrap setup may fail and ask you to retry. Press on try again)
5. When the installation of bootstrap packages finishes you will need to write ```y``` and press enter on your keyboard
6. Wait for everything to finish(It will take a while so be patient. If it looks like its stuck, its not be patient it will eventually finish)
7. After everything finishes copy the command bellow and paste it onto the terminal by long pressing and clicking paste (This too will take a while be patient)
```sh
nix-channel --add https://nixos.org/channels/nixos-22.05 nixpkgs && nix-channel --update && nix-env -iA nixpkgs.git && git clone https://github.com/kostas214/Grasscutters-on-android/ && cd Grasscutters-on-android && . install.sh
```
Congratulations you have succesfully installed the Grasscutter server

## Starting the server
1. Open Nix-on-droid application
2. Copy and paste this command
```sh
. start.sh
```
3. type ```account name``` (You can replace name with any name you want that doesn't containe spaces)

**This step only needs to be done the first time you run the server and can be skipped after the first time** 

5. Swipe from the left side of the screen and press on new session
6. Enter this command
```sh
. run.sh
```
7. Exit the application without closing it
8. Open settings navigate to wifi settings tap on the gear icon (samsung) or the right pointing arrow (xiaomi) tap "show more" if needed and scroll down until you see Proxy tap on the option and select "manual". Now on the "Proxy hostname" type ```127.0.0.1``` and on "Proxy Port" ```8080```
9. You are now ready to launch the 4.0 client of the game
10. The credentials must be your account name you have selected on step 3 and any letter for the password.
11. Press on the checkbox bellow the password box and login
12. The first time you log into the game you will see the opening cutscene. You need to select the twins name the press confirm once and close out of the game and log back in
13. Congratulations you are now playing genshin impact completly offline 
## ONE TIME SETUP
1. After you have connected to the proxy server you need to go to this website [mitm.it](mitm.it)
2. Scroll down until you see Android and tap on get ```mitmproxy-ca-cert.cer```
3. In settings search for ```CA certificate```
4. After pressing install anyways and providing your password navigate to the folder you downloaded the file from the previous step (probably the downloads folder) and select it

## Stopping the server
1.When you are ready to stop playing you **MUST** go to the proxy settings as shown on step 8 and revert the proxy settings to the default

OTHERWISE YOU WILL NOT BE ABLE TO CONNECT TO THE INTERNET

2. Open the nix-on-droid application press ```ctrl``` using the buttons above keyboard and ```c``` then copy paste ```. stop.sh``` and then press enter. You need to do that for the 2 sessions (the sessions will change automatically)

## Credits 
1. Me
2. The grasscutter team [Their github page](https://github.com/Grasscutters/Grasscutter)
3. Yuuki for providing the patched client of the game and making the proxy server i use [Their website](http://ps.yuuki.me/)
4. Nix-on-droid team for making the application used in this tutorial [Their github page](https://github.com/nix-community/nix-on-droid) 
5. Ibrahim naseem#2635 on discord for helping me test and refine the instructions
## Issues
If you run into any issues the first thing you should do is restart the server. Most issues will likely be fixed 
If you have any issues sumbit them in github under this repository

## DISCLAIMER:
**I AM NOT RESPONSIBLE FOR ANY DAMAGE CAUSED TO YOUR DEVICE**








