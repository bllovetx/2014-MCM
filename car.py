class Car():
    def __init__(self, settings, speed, x):
        self.settings = settings
        self.length = 4.6    #The length of the car along its driving direction;
        self.speed = speed
        self.y = 0  #Position on this lane;
        self.x = x  #Which lane;
        self.is_switch = 0  
        self.switch_time = settings.switch_time
        self.is_collide = 0
        self.collide_time = settings.collide_time
    def update(self):
        self.switch_time -= self.is_switch*self.settings.time_unit
        self.collide_time -= self.is_collide*self.settings.time_unit
        if not self.is_collide:
            self.y += self.speed*self.settings.time_unit
        if self.is_switch == 1 and self.switch_time <= 0:
            self.is_switch = 0
            self.switch_time = self.settings.switch_time
        if self.is_collide == 1 and self.collide_time <= 0:
            return True
        return False

def sort_key(car):
    return car.y