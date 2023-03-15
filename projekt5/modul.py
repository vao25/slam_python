import json

class Map:
    def __init__(self):
        self.x = []
        self.lm = []
        self.wp = []
        
    def load(self):
        with open('file.json', 'r') as fr:
            dataR = json.load(fr)
        self.x = dataR["x"]
        self.lm = dataR["lm"]
        self.wp = dataR["wp"]
        
    def save(self):
        dataW = {}
        dataW["x"] = self.x
        dataW["lm"] = self.lm
        dataW["wp"] = self.wp
        open('file.json', 'w').close()
        with open('file.json', 'w') as fw:
            json.dump(dataW, fw)
            
    def add(self, switch, x, y):
        if switch == "r":
            self.x = []
            self.x.append(x)
            self.x.append(y)            
        elif switch == "l":
            self.lm.append([x-self.x[0], self.x[1]-y])            
        elif switch == "w":
            self.wp.append([x-self.x[0], self.x[1]-y])
            
    def remove(self, switch, index):
        if switch == "l":
            del self.lm[index]            
        elif switch == "w":
            del self.wp[index]
