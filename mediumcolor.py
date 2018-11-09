from PIL import ImageGrab
from pyfirmata import Arduino, util


board = Arduino('/dev/cu.usbmodem1411')
# board.digital[13].write(0.5)
# analog_0 = board.get_pin('a:0:i')
# pin3 = board.get_pin('a:13:p')
# pin3.write(1)
# board.analog[13].write(0.5)
red = board.get_pin('d:9:p')
green = board.get_pin('d:10:p')
blue = board.get_pin('d:11:p')
# red.write(55/255)
# green.write(55/255)
# blue.write(55/255)

def compute_average_image_color():
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
        red.write(r_total / count / 255)
        green.write(g_total / count / 255)
        blue.write(b_total / count / 300)
        return round(r_total / count), round(g_total / count), round(b_total / count)


def main():
    for i in range(10):
        average_color = compute_average_image_color()
        print(average_color)


if __name__ == '__main__':
    print('ok')