import random
import threading
import asyncio
import telethon
from telethon import events
from queue import Queue
import requests
from telethon.sync import functions
from user_agent import generate_user_agent
import requests
from user_agent import *
from help import *
from config import *
from threading import Thread

a = 'qwertyuiopasdfghjklzxcvbnm'
b = '1234567890'
e = 'qwertyuiopassdfghjklzxcvbnm1234567890'

banned = []
isclaim = ["off"]
isauto = ["off"]
with open("banned.txt", "r") as f:
    f = f.read().split()
    banned.append(f)

que = Queue()


def check_user(username):
    url = "https://t.me/"+str(username)
    headers = {
        "User-Agent": generate_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}

    response = requests.get(url, headers=headers)
    if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
        return "Available"
    else:
        return "Unavailable"

def gen_user(choice):
    if choice == "1":
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], c[0], c[0], c[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(e)
            f = [c[0], d[0], c[0], c[0], c[0]]
            username = ''.join(f)
        else:
            pass
    if choice == "2":
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], d[0], c[0], c[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(e)
            f = [c[0], c[0], d[0], c[0], c[0]]
            username = ''.join(f)
        else:
            pass
    if choice == "3":
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], d[0], c[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(e)
            f = [c[0], c[0], c[0], d[0], c[0]]
            username = ''.join(f)
        else:
            pass
    if choice == "4":
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], c[0], d[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(e)
            f = [c[0], c[0], c[0], c[0], d[0]]
            username = ''.join(f)
        else:
            pass
    if choice == "5":
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], d[0], c[0], c[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(e)
            f = [c[0], d[0], d[0], c[0], c[0]]
            username = ''.join(f)
        else:
            pass
    if choice == "6":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], d[0], d[0], c[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(e)
            f = [c[0], c[0], d[0], d[0], c[0]]
            username = ''.join(f)
        else:
            pass
    if choice == "7":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], d[0], d[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(e)
            f = [c[0], c[0], c[0], d[0], d[0]]
            username = ''.join(f)
        else:
            pass
    if choice == "8":
        c = d = 
                else:
                    pass
                trys += 1

                await asyncio.sleep(8)
            trys = ""
            isclaim.clear()
            isclaim.append("off")
            await sython.send_message(event.chat_id, "تم الانتهاء من التثبيت التلقائي")
        if msg[0] == "يدوي":  # تثبيت يدوي يوزر قناة
            await event.edit(f"حسناً سأحاول تثبيت `{username}` على `{ch}` !")
            msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
            username = str(msg[0])
            ch = str(msg[1])
            try:
                await sython(functions.channels.UpdateUsernameRequest(
                    channel=ch, username=username))
                await event.client.send_message(event.chat_id, f'''
●━━━━━━━━●
┏━━━━━┓
- By ↣ @X_K_5
┗━━━━━┛
┏━━━━━┓
↣ (@{username})
┗━━━━━┛
┏━━━━━┓
- By ↣ @is_TNT
┗━━━━━┛
●━━━━━━━━●
    ''')
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                await event.client.send_message(event.chat_id, f"مبند `{username}` ❌❌")
            except Exception as eee:
                await sython.send_message(event.chat_id, f'''خطأ مع {username}
    الخطأ :
    {str(eee)}''')
Threads=[] 
for t in range(100):
    x = threading.Thread(target=_)
    le = threading.Thread(target=gen_user)
    x.start()
    le.start()
    Threads.append(x)
    Threads.append(le)
for Th in Threads:
    Th.join()
