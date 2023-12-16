nix-env -iA nixpkgs.nano nixpkgs.mongodb nixpkgs.jdk17 nixpkgs.mitmproxy nixpkgs.wget nixpkgs.curl
wget https://github.com/Grasscutters/Grasscutter/releases/download/v1.7.4/grasscutter-1.7.4.jar
git clone https://gitlab.com/YuukiPS/GC-Resources
java -jar grasscutter-1.7.4.jar
cd GC-Resources/Resources
mv BinOutput/ ExcelBinOutput/ Scripts ScriptSceneData/ Server TextMap/ ~/Grasscutters-on-android/resources
cd ~/Grasscutters-on-android
