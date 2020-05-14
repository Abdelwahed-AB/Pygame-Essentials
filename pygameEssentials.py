import pygame as pg

font_dir = 'C:\\Users\\Abdelwahed\\AppData\\Local\\Microsoft\\Windows\\Fonts\\'


class Button():
    def __init__(self, Surface, position, dimensions, bg_color, highlight_color, text="", font='SourceCodePro-Light', font_size=10, txt_color=(0, 0, 0)):

        # Attributes
        self.surface = Surface
        self.position = position
        self.dimensions = dimensions
        self.color = bg_color
        self.highlight = highlight_color
        self.text = text
        self.font = font_dir + font + ".ttf"
        self.font_size = font_size
        self.text_color = txt_color

        self.width, self.height = self.dimensions
        self.x, self.y = self.position

        self.isDown = False
        self.isMouseOver = False

    def __draw(self):

        # Change color if mouse is over the button
        if self.isMouseOver:
            color = self.highlight
        else:
            color = self.color
        # Generate Button
        button_img = pg.Surface(self.dimensions)
        button_rect = button_img.get_rect()
        button_img.fill(color)

        # Generate Text
        font = pg.font.Font(self.font, self.font_size)
        txt = font.render(self.text, True, self.text_color)
        txt_rect = txt.get_rect()
        txt_rect.center = button_rect.center

        # Render Button to screen
        button_img.blit(txt, txt_rect)
        self.surface.blit(button_img, self.position)

    def __user_input(self):
        if (self.x < pg.mouse.get_pos()[0] < self.x + self.width) and (self.y < pg.mouse.get_pos()[1] < self.y + self.height):
            self.isMouseOver = True
            self.isDown = True if (pg.mouse.get_pressed() == (1, 0, 0)) else False
        else:
            self.isMouseOver = False

    def Update(self):
        self.__user_input()
        self.__draw()
