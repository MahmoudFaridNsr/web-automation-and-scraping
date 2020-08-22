
import configparser
import random
import codecs
import os
class ConfigReader:
    TARGET_USER_LINK = ''
    TARGET_USER_NAME = ''
    PROFILE_WEBSITE = ''
    PROFILE_ABOUT = ''
    GIVE_LIKES =''
    GIVE_COINS = ''
    ANSWER_QUESTIONS = ''
    ASK_WALL = ''
    CHANGE_PROFILE = ''

    def __init__(self):
        self.readConfig()
        return

    def readConfig(self):
         config = configparser.ConfigParser()
         config.read('Config.txt', encoding='utf8')
         self.TARGET_USER_LINK = config['OPTIONS']['TARGET_USER_LINK']
         self.PROFILE_WEBSITE = config['OPTIONS']['PROFILE_WEBSITE']
         self.PROFILE_ABOUT = config['OPTIONS']['PROFILE_ABOUT']
         self.TARGET_USER_NAME = config['OPTIONS']['TARGET_USER_NAME']
         self.GIVE_LIKES = int(config['OPTIONS']['GIVE_LIKES'])
         self.GIVE_COINS = int(config['OPTIONS']['GIVE_COINS'])
         self.ASK_WALL = int(config['OPTIONS']['ASK_WALL'])
         self.ANSWER_QUESTIONS = int(config['OPTIONS']['ANSWER_QUESTIONS'])
         self.CHANGE_PROFILE = int(config['OPTIONS']['CHANGE_PROFILE'])

class DataReader:
    NAMES_SET = []
    CITIES_SET = []
    IMAGES_SET = []
    SHOUTS_SET = []
    PROXIES_SET= []
    TARGETS_SET= []
    def __init__(self):
        self.readCities()
        self.readNames()
        self.getImagesPaths()
        self.readShouts()
        #self.readProxies()
        return    
    
    CHARS_LIST = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    
    def getRandomShout(self):
        shout = self.SHOUTS_SET.pop(0)
        self.SHOUTS_SET.append(shout)
        shout = shout + ' @m_faried '
        return shout
    def readNames(self):
        try:
            f = codecs.open('Data/names.txt', 'r',encoding='utf8') 
            self.NAMES_SET = list(f.readlines())
            f.close()
            for n in range(0,len(self.NAMES_SET)-1):
                self.NAMES_SET[n] = self.NAMES_SET[n].rstrip("\r\n")  
            #print(self.NAMES_SET)
            random.shuffle(self.NAMES_SET)
            print('Names Set Read [Success] Count =  {}'.format(len(self.NAMES_SET)))
        except FileExistsError:
            print('Names Set Read [Fail]')
        return
    def readShouts(self):
        try:
            f = codecs.open('Data/shouts.txt', 'r',encoding='utf8') 
            self.SHOUTS_SET = list(f.readlines())
            f.close()
            for n in range(0,len(self.SHOUTS_SET)-1):
                self.SHOUTS_SET[n] = self.SHOUTS_SET[n].rstrip("\r\n")  
            #print(self.SHOUTS_SET)
            random.shuffle(self.SHOUTS_SET)
            print('SHOUTS_SET Set Read [Success] Count =  {}'.format(len(self.SHOUTS_SET)))
        except FileExistsError:
            print('SHOUTS_SET Set Read [Fail]')
        return
    def readCities(self):
        try:
            f = codecs.open('Data/cities.txt', 'r',encoding='utf8') 
            self.CITIES_SET = list(f.readlines())
            f.close()
            for n in range(0,len(self.CITIES_SET)-1):
                self.CITIES_SET[n] = self.CITIES_SET[n].rstrip("\r\n")  
            #print(self.CITIES_SET)
            random.shuffle(self.CITIES_SET)
            print('Cities Set Read [Success] Count =  {}'.format(len(self.CITIES_SET)))
        except FileExistsError:
            print('Cities Set Read [Fail]')
        return
    def getRandomCity(self):
        city  = self.CITIES_SET.pop(0)
        self.CITIES_SET.append(city)
        return city
    def getRandomName(self):
        name  = self.NAMES_SET.pop(0)
        self.NAMES_SET.append(name)
        return name
    #get the ilst of the images
    def getImagesPaths(self):
        thisdir = os.getcwd()
        # r=root, d=directories, f = files
        for r, d, f in os.walk(thisdir):
            for file in f:
                if file.endswith(".png") or file.endswith('.jpeg'):
                    path =os.path.join(r, file)
                    path = path.replace("\\","/")
                    self.IMAGES_SET.append(path) 
        #print(self.IMAGES_SET)
        print("Total Loaded Images = {}".format(len(self.IMAGES_SET)))
    #return random image from the images
    def getRandomImage(self):
        return self.IMAGES_SET[random.randint(0,len(self.IMAGES_SET)-1)]
    #getting a random mail
    def getRandomMail(self):
        mail = self.getRandomName()
        for i in range(12):
            mail = mail + self.CHARS_LIST[random.randint(0,len(self.CHARS_LIST)-1)]
        mail = mail+ '@gmail.com'
        return mail