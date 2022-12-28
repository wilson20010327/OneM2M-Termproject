from Farmland import Farmland
import random
import requests
from datetime import datetime

import os

idx = 0
Farmlands = []
node_red_ip='http://127.0.0.1:1880/'

def generate_Farmland():
    global idx
    global Farmlands
    tmp = Farmland(idx)
    fp = open(str(idx)+'.txt', 'w')
    fp.write('40')
    fp.close()
    idx = idx+1
    Farmlands.append(tmp)

    print(Farmlands)


def pest_event():
    global Farmlands
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)	
    r = requests.post(node_red_ip+'GetVirus', data = {'time':dt_string,'Sum_of_Farm':len(Farmlands)})
    virus_happened()

    

def virus_happened():
    global Farmlands
    path = './active.txt'
   
    # Check whether the specified
    # path exists or not
    isExist = os.path.exists(path)
    print(isExist)
    defence=0
    if isExist:
        defence=1 #to simulate know the virus come
        os.remove(path)
    for farmland in Farmlands:
            strength = random.randint(0, 100) # virus strength
            index=Farmlands.index(farmland) # index of farmland
            with open(str(index)+".txt") as f: #get strength in file
                contents = f.readlines()
                farmland.defend_strength=int(contents[0])
                print(farmland.defend_strength)

            check__point=(strength > farmland.defend_strength*defence and len(farmland.plants)>0) # defence or not
            r = requests.post(node_red_ip+'VirusData', data = {'index':index,'DefenceCheck':not check__point,'dfStrength':farmland.defend_strength})
            if check__point:
                farmland.layout.removeWidget(farmland.plants[0])
                del farmland.plants[0]