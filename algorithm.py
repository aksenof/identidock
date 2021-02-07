from PIL import Image, ImageDraw
from colormap import colormap
from random import choice
import os


class AvatarGenerator:
    def __init__(self, name):
        self.username = name
        self.width, self.height = 500, 500  # 100x100, 200x200, 300x300, 400x400 ...
        self.size = 50  # size of one piece

    def coords(self):
        x0_y1 = []  # [(x0, y1)]
        y0_x1 = []  # [(y0, x1)]
        result = []  # [(x0, y0, x1, y1)]
        for x0 in range(0, self.width, self.size):
            for y1 in range(self.size, self.height + self.size, self.size):
                x0_y1.append((x0, y1))
        for x1 in range(self.size, self.width + self.size, self.size):
            for y0 in range(0, self.height, self.size):
                y0_x1.append((y0, x1))
        for index_x0y1, x0y1 in enumerate(x0_y1):
            for index_y0x1, y0x1 in enumerate(y0_x1):
                if index_x0y1 == index_y0x1:
                    result.append((x0y1[0], y0x1[0], y0x1[1], x0y1[1]))
        return result

    def save(self):
        if not os.path.exists('static/{file}.png'.format(file=self.username)):
            im = Image.new('RGB', (self.width, self.height), (255, 255, 255))
            draw = ImageDraw.Draw(im)
            for coord in self.coords():
                random_color = choice(colormap)
                draw.rectangle(coord, fill=random_color)
            im.save('static/{file}.png'.format(file=self.username), quality=100)
