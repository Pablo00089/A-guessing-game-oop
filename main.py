import random

class GuessNumber:
    
    def __init__(self, data_info):
        self.data_info = data_info
        
    
    def winner_chacker(self,data_u, data_r):
        if self.data_u == self.data_info:
            print("Vítěz")
        elif self.d > self.data_info:
            print("Moc vysoké číslo.")
        elif self.data_info < self.data_info:
            print("Moc nízké info.")        
        


# *****************************************

data_random = random.randint(1,50)
data_user = int(input("Hádej číslo 1-50: "))

data_r = GuessNumber(data_random)
data_u = GuessNumber(data_user)

print(data_r.data_info)
data_u.data_info

data_r.winner_chacker()


