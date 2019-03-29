sudo apt update && sudo apt upgrade 
sudo apt install -y net-tools curl python3-pip build-essential git
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt install -y nodejs
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.profile 
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc 
source ~/.bashrc
npm i -g truffle 

