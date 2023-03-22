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