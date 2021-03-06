

class Manager:


    def __init__(self, controlled_abstractions):
        self.__controlled_abstractions = controlled_abstractions

    def draw(self, window):
        for abstraction in self.__controlled_abstractions:
            abstraction.draw(window)
        self.__move()

    def __move(self):
        for abstraction in self.__controlled_abstractions:
            abstraction.move()
