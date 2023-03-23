#Global functions
class Animation_loop:
    def __init__(self):
        self.step_index = 0

    def __call__(self):
        self.step_index += 1
        if self.step_index > 9:
            self.step_index = 0
        image = self.step_index // 5
        return image
    
    
class Color_loop:
    def __init__(self):
        self.step_index = 0
        self.colors = ((255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 0, 255), (75, 0, 130), (238, 130, 238))

    def __call__(self):
        self.step_index += 1
        if self.step_index > 69:
            self.step_index = 0
        color = self.colors[self.step_index // 10]
        return color