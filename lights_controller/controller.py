import asyncio

from rpi_ws281x import PixelStrip


def clamp(value, minimum, maximum):
    return max(minimum, min(value, maximum))


class Controller:
    def __init__(self, strip: PixelStrip):
        self._strip = strip
        self._strip.begin()

        self.animator = self.Animator(self)

    def __len__(self):
        return self._strip.numPixels()

    def __iter__(self):
        yield from self[:]

    def __setitem__(self, pos, color):
        if isinstance(color, int):
            color = clamp(color, 0, 0xFFFFFF)

            if isinstance(pos, slice):
                for i in range(*pos.indices(len(self))):
                    self._strip.setPixelColor(i, color)
            else:
                self._strip.setPixelColor(pos, color)
        elif isinstance(color, list):
            color = [clamp(c, 0, 0xFFFFFF) for c in color]

            for i in range(*pos.indices(len(self))):
                self._strip.setPixelColor(i, color[i])

    def __getitem__(self, pos):
        if isinstance(pos, slice):
            return [self._strip.getPixelColor(i) for i in range(*pos.indices(len(self)))]
        return self._strip.getPixelColor(pos)

    def brightness(self, brightness=None):
        if brightness is not None:
            self._strip.setBrightness(clamp(brightness, 0, 0xFF))
        return self._strip.getBrightness()

    def update(self):
        self._strip.show()

    class Animator:
        def __init__(self, controller: "Controller"):
            self._controller = controller

        async def flash(self, color, duration):
            original_pattern = self._controller[:]

            self._controller[:] = color
            self._controller.update()

            await asyncio.sleep(duration)

            self._controller[:] = original_pattern
            self._controller.update()
