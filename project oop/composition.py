class Leg:
    pass

class Back:
    pass

class Chair:
    def __init__(self, num_legs):
        self.legs = [Leg() for leg in range(num_legs)]
        self.back = Back()