import json
from math import radians, degrees

class Map:
    def __init__(self):
        self.x3 = 0
        self.lm = []
        self.wp = []
        
    def load(self):
        with open('file.json', 'r') as fr:
            dataR = json.load(fr)
        self.x3 = round(degrees(dataR["x3"]))
        self.lm = dataR["lm"]
        self.wp = dataR["wp"]
        
    def save(self):
        dataW = {}
        dataW["x3"] = self.x3
        dataW["lm"] = self.lm
        dataW["wp"] = self.wp
        open('file.json', 'w').close()
        with open('file.json', 'w') as fw:
            json.dump(dataW, fw)
            
    def add(self, switch, x = 0, y = 0, phi = ""):
        if switch == "r":
            if phi != "":
                deg = float(phi)
                deg = deg - int(deg/360)*360
                if deg > 180:
                    deg = -1*(360 - deg)
                rad = radians(deg)
                self.x3 = rad
                return deg
            else:
                self.x3 = 0
                return 0
        elif switch == "l":
            self.lm.append([x, -y])            
        elif switch == "w":
            self.wp.append([x, -y])
            
    def remove(self, switch, index):
        if switch == "l":
            del self.lm[index]            
        elif switch == "w":
            del self.wp[index]
