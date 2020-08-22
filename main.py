from bot import AskBot
import ctypes
from time import sleep
from iohandler import ConfigReader ,DataReader
import os
import telnetlib


if __name__ == '__main__':
   
    ctypes.windll.kernel32.SetConsoleTitleW("ASK.fm - Likes Bot  v 1.0 - By - Mahmoud Farid (EL3oksh) ")
    config = ConfigReader()
    i = 0
    while True:
        bot = AskBot()
        bot.createAccout()
        bot.fillProfile()
        sleep(2)
        bot.giveLikes(config.TARGET_USER_NAME)
        sleep(2)
        #bot.askDiscoveredPeople()
        #sleep(3)
        bot.shoutOut()
        sleep(2)
        bot.shoutOut()
        sleep(2)
        bot.shoutOut()
        sleep(2)
        bot.shoutOut()
        sleep(2)
        #sleep(50)
        bot.closeDriver()
        # i+=1
        # if i == 8:
        #     routerReboot()
        #     i=0
        #     sleep(120)
    