# Grasscutters-on-android

### A comprehensive guide on how to run the grasscutters server locally on your android device 

Client installation (If you have played on yuuki before you can skip this part)
1. Go to [ps.yuuki.me](https://ps.yuuki.me/game/genshin-impact) and download the android 4.0 client for genshin impact
2. Install the .apk and open it
3. You need to log onto the yuuki servers at least (make an account [here](https://ps.yuuki.me/account/register?type=web)
4. Log in in genshin impact and wait for the download to complete (you can leave the app and the download will continue)

Server installation 
1. Download and install F-droid [here](https://f-droid.org/)
2. Open F-droid and search for "Nix-on-Droid" and install the app
3. Open Nix-on-Droid
4. When you first open the application it may ask you for notifications permission (android 13 and up) and a prompt for "Bootstrap zipball location" will appear and you need to click on yes
5. When the installation of bootstrap packages finishes you will need to write ```y``` and press enter on your keyboard
6. Wait for everything to finish(It will take a while so be patient. If it looks like its stuck, its not be patient it will eventually finish)
7. After everything finishes copy the command bellow and paste it onto the terminal by long pressing and clicking paste (This too will take a while be patient)
```sh
nix-channel --add https://nixos.org/channels/nixos-22.05 nixpkgs && nix-channel --update && nix-env -iA nixpkgs.git && git clone https://github.com/kostas214/Grasscutters-on-android/ && cd Grasscutters-on-android && . install.sh
```

