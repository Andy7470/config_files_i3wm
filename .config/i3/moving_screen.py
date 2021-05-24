
class MovingScreen:

    screen = []
    size = 6

    def __init__(self,text,decorative='-'):
        self.text = text
        self.size = len(text)
        self.decorative = decorative
    
    def make_screen(self):
        for i in range(self.size):
            self.screen.append(self.decorative)

    def get_size(self):
        return self.size
    
    def to_array(self,text):
        array = []
        for t in self.text:
            array.append(t)
        return array

    def to_text(self):
        text = ""
        for i in range(len(self.screen)):
            text += self.screen[i]
        return text

    def run_screen(self,counter):
        text_array = self.to_array(self.text)
        self.screen.pop(0)
        if counter < len(text_array):
            self.screen.append(text_array[counter])
        else:
            self.screen.append(self.decorative)
        text = self.to_text()
        return text 
