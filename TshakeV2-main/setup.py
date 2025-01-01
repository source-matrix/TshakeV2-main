import requests,os

try:
  from config import *
  os.system('pm2 start bot.py --name {} --interpreter python3.7 --interpreter-args -u'.format(BOT_ID))
except Exception as e:
  API_ID = 21321670
  API_HASH = '7ffe42a7ac4872b6efd6ba014d44944e'

  out ="""
from pyrogram import enums
API_ID = 21321670
API_HASH = '7ffe42a7ac4872b6efd6ba014d44944e'
"""
  def Bot(TOKEN,method,data):
    url = "https://api.telegram.org/bot{}/{}".format(TOKEN,method)
    post = requests.post(url,data=data)
    return post.json()
  ID = "7211799879"
  go = True
  while go:
    token = input("7211799879:AAFW5zk11OkaIr132ES6Xg9UPMJpu1ZmIQ4:")
    get = Bot(token,"getme",{})
    if get["ok"]:
      out = out+"\n"+"TOKEN = '{}'\nBOT_ID = TOKEN.split(':')[0]".format(token)
      go = False
      ID = token.split(':')[0]

    else:
      print("TOKEN is invalid, Try again")

  sudo = input("input you're ID:")
  out = out+"\n"+"SUDO = {}".format(sudo)

  f = open("config.py","w+") 
  f.write(out)
  f.close()

  os.system('pm2 start bot.py -f --name {} --interpreter python3.7 --interpreter-args -u'.format(ID))
