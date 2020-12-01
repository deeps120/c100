class Car(object):
    def __init__(self,model,color,company,speedLimit):
        self.color=color
        self.company=company
        self.speedLimit=speedLimit
        self.model=model
    
    def Start(self):
        print('car started!')
    
    def Stop(self):
        print('car stopped')
    
    def Accelerating(self):
        print('car accelerating')
    
    def Gear(self,gearType):
        print('gear change')

audi = Car('a6','red','audi','100')
