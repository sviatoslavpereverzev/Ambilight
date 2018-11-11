from PIL import ImageGrab
from pyfirmata import Arduino

SERIAL_PORT = '/dev/cu.usbmodem1411'
board = Arduino(SERIAL_PORT)
PIN_RED = board.get_pin('d:5:p')
PIN_GREEN = board.get_pin('d:6:p')
PIN_BLUE = board.get_pin('d:3:p')


def monitor_color():
    for _ in range(10):
        img = ImageGrab.grab()
        img = img.resize((100, 100))
        width, height = img.size
        r_total = 0
        g_total = 0
        b_total = 0
        count = 0
        for x in range(0, width):
            for y in range(0, height):
                r, g, b, a = img.getpixel((x, y))
                r_total += r
                g_total += g
                b_total += b
                count += 1

        return {'red': r_total / count / 255, 'green': g_total / count / 255, 'blue': b_total / count / 300}


def write_color(color):
    PIN_RED.write(color['red'])
    PIN_GREEN.write(color['green'])
    PIN_BLUE.write(color['blue'])
    return True


if __name__ == '__main__':
    for _ in range(10):
        color = monitor_color()
        write_color(color)
