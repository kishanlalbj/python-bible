import random
class Rupee:

    def __init__(self, rare=False):
        self.rare = rare
        if(self.rare):
            self.value = 10.00
        else:
            self.value = 5.00
        self.color = "silver"
        self.edges = 1
        self.diameter = 22.5 #mm
        self.thickness = 3.15 #mm
        self.heads = True
    def __del__(self):
        print("Coin spent")

    def rust(self):
        self.color = "green"
    def clean(self):
        self.color = "silver"
    def flip(self):
        options = [True,False]
        choice = random.choice(options)
        self.heads = choice

coin1 = Rupee(rare= True)
coin2 = Rupee()
coin1.rust()
coin1.flip()

print(coin1.value)
print(coin1.color)
print(coin1.heads)
del coin1

print(coin2.value)
print(coin2.color)





