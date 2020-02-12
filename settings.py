class Settings():
    def __init__(self, traffic):
        self.max_speed = 120
        self.min_speed = 80
        self.lane_length = 100000 # meters
        self.switch_time = 3.6  # seconds
        self.collide_time = 10  # seconds
        self.time = 1000000
        self.lanes = 5
        self.traffic = traffic  # option: 'heavy'/'light'
        self.time_unit = 0.1    # sec
        # appear
        self.random_0 = 0
        self.random_1 = 0
        self.random_2 = 0
        self.add_p = []