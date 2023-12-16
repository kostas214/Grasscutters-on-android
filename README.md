# Grasscutters-on-android

### A comprehensive guide on how to run the grasscutters server locally on your android device 

Client installation
1. Go to [ps.yuuki.me](https://ps.yuuki.me/game/genshin-impact) and download the android 4.0 client for genshin impact
2. Install the .apk and open it
3. You need to log onto the yuuki servers at least (make an account [here](https://ps.yuuki.me/account/register?type=web)
4. Log in in genshin impact and wait for the download to complete (you can leave the app and the download will continue)




Server installation commands
```sh
nix-channel --add https://nixos.org/channels/nixos-22.05 nixpkgs
nix-channel --update
nix-env -iA nixpkgs.git
git clone https://github.com/kostas214/Grasscutters-on-android/
cd Grasscutters-on-android
. install.sh
```

