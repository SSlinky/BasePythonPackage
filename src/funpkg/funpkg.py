class Util():
    def __init__(self):
        self.stored = None

    def store(self, value):
        self.stored = value

    def retrieve(self):
        return self.stored
