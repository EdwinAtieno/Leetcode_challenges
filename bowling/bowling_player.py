class Player:
    def __init__(self, name):
        self.name = name
        self.frames = []

    def add_score(self, score):
        if not self.frames or len(self.frames[-1].scores) == 2:
            self.frames.append(Frame())
        self.frames[-1].add_score(score)

    def calculate_total_score(self):
        return sum(frame.calculate_score() for frame in self.frames)
