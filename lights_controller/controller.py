import asyncio
from typing import Iterator

from rpi_ws281x import PixelStrip


def clamp(value, minimum, maximum):
    return max(minimum, min(value, maximum))


class Controller:
    def __init__(self, strip: PixelStrip) -> None:
        self._strip = strip
        self._strip.begin()

        self.animator = self.Animator(self)

    def __len__(self) -> int:
        return self._strip.numPixels()

    def __iter__(self) -> Iterator[int]:
        yield from self[:]  # type: ignore

    def __setitem__(self, pos: int | slice, color: int | list[int]) -> None:
        if isinstance(color, int):
            color = clamp(color, 0, 0xFFFFFF)

            if isinstance(pos, slice):
                for i in range(*pos.indices(len(self))):
                    self._strip.setPixelColor(i, color)
            else:
                self._strip.setPixelColor(pos, color)
        else:
            color = [clamp(c, 0, 0xFFFFFF) for c in color]

            if isinstance(pos, slice):
                for i in range(*pos.indices(len(self))):
                    self._strip.setPixelColor(i, color[i])
            else:
                self._strip.setPixelColor(pos, color[0])

    def __getitem__(self, pos: int | slice):
        if isinstance(pos, slice):
            return [self._strip.getPixelColor(i) for i in range(*pos.indices(len(self)))]
        return self._strip.getPixelColor(pos)

    def brightness(self, brightness: int | None = None) -> int:
        if brightness is not None:
            self._strip.setBrightness(clamp(brightness, 0, 0xFF))
        return self._strip.getBrightness()

    def update(self) -> None:
        self._strip.show()

    class Animator:
        def __init__(self, controller: "Controller") -> None:
            self._controller = controller

        async def flash(self, pattern: int | list[int], duration: float) -> None:
            original_pattern = self._controller[:]

            self._controller[:] = pattern
            self._controller.update()

            await asyncio.sleep(duration)

            self._controller[:] = original_pattern
            self._controller.update()
