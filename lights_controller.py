from rpi_ws281x import PixelStrip

class Controller:
    def __init__(self, strip: PixelStrip):
        self.currentIter = -1
        self.maxIter = strip.numPixels() - 1

        self.strip = strip
        strip.begin()

    def __len__(self):
        return self.strip.numPixels()

    def __iter__(self):
        return self
    
    def __setitem__(self, index: int, color: int):
        self.strip.setPixelColor(index, color)

    def __getitem__(self, index: int):
        return self.strip.getPixelColor(index)

    def __next__(self):
        self.currentIter += 1
        if self.currentIter <= self.maxIter:
            return self[self.currentIter]
        raise StopIteration
