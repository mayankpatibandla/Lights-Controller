from rpi_ws281x import PixelStrip


class Controller:
    def __init__(self, strip: PixelStrip):
        self._current_iter = -1
        self._max_iter = strip.numPixels() - 1

        self._strip = strip
        self._strip.begin()

    def __len__(self):
        return self._strip.numPixels()

    def __iter__(self):
        return self

    def __setitem__(self, pos, color: int):
        if isinstance(pos, slice):
            for i in range(*pos.indices(len(self))):
                self._strip.setPixelColor(i, color)
        else:
            self._strip.setPixelColor(pos, color)

    def __getitem__(self, pos):
        if isinstance(pos, slice):
            return [self._strip.getPixelColor(i) for i in range(*pos.indices(len(self)))]
        return self._strip.getPixelColor(pos)

    def __next__(self):
        self._current_iter += 1
        if self._current_iter <= self._max_iter:
            return self[self._current_iter]
        raise StopIteration

    def set_brightness(self, brightness: int):
        self._strip.setBrightness(brightness)

    def update(self):
        self._strip.show()
