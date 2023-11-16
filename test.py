import random

fish_property = {
    "shark1":{"imageLenth" : 12,"swimmingLength":8,"baseSpeed":3,"speedRange":1.1,"captureProbability":0.05,"coinLevel":2,"multiple":10},
    "fish1":{"imageLenth" : 8,"swimmingLength":4,"baseSpeed":1,"speedRange":2,"captureProbability":0.7,"coinLevel":1,"multiple":1},
    "fish2":{"imageLenth" : 8,"swimmingLength":4,"baseSpeed":1,"speedRange":2,"captureProbability":0.6,"coinLevel":1,"multiple":2},
    "fish3":{"imageLenth" : 8,"swimmingLength":4,"baseSpeed": 1.5, "speedRange": 2, "captureProbability": 0.5, "coinLevel": 1,"multiple":3},
    "fish4":{"imageLenth" : 8,"swimmingLength":4,"baseSpeed": 2, "speedRange": 1, "captureProbability": 0.4, "coinLevel": 1,"multiple":4},
    "fish5":{"imageLenth" : 8,"swimmingLength":4,"baseSpeed": 1.2, "speedRange": 2.1, "captureProbability": 0.35, "coinLevel": 1,"multiple":5},
    "fish6":{"imageLenth" : 12,"swimmingLength":8,"baseSpeed": 1.4, "speedRange": 1, "captureProbability": 0.3, "coinLevel": 2,"multiple":1},
    "fish7":{"imageLenth" : 10,"swimmingLength":6,"baseSpeed": 1, "speedRange": 4, "captureProbability": 0.25, "coinLevel": 2,"multiple":2},
    "fish8":{"imageLenth" : 12,"swimmingLength":8,"baseSpeed": 2.2, "speedRange": 1, "captureProbability": 0.2, "coinLevel": 2,"multiple":3},
    "fish9":{"imageLenth" : 12,"swimmingLength":8,"baseSpeed": 1.2, "speedRange": 3, "captureProbability": 0.15, "coinLevel": 2,"multiple":4},
    "fish10":{"imageLenth" : 10,"swimmingLength":6,"baseSpeed": 1, "speedRange": 2, "captureProbability": 0.1, "coinLevel": 2,"multiple":5}
}

kknd = 'sdsdsd'

kknd2 = 'sdsdsdsd'

class A:
    pass

def dosometing():
    print(kknd)

is_left = True if random.randint(0,2) == 0 else False

cannons = [ i for i in range(1,8) ]
print(cannons)

print(random.random())