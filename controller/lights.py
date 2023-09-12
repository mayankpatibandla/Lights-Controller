from lights_controller import *
import time

# LED config
LED_COUNT = 288
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_INVERT = False
LED_BRIGHTNESS = 255
LED_CHANNEL = 0

strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
lights = Controller(strip)

def foo():
    print("LIGHTS!!")

if __name__ == "__main__":
    lights.clear()
    lights.update()

    time.sleep(3)
    
    lights[::] = 0xFFFFFF
    lights.strip.show()
    
    print("done")
