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
        # Get user input
        if (self.x < pg.mouse.get_pos()[0] < self.x + self.width) and (self.y < pg.mouse.get_pos()[1] < self.y + self.height):
            self.isMouseOver = True
            self.isDown = True if (pg.mouse.get_pressed() == (1, 0, 0)) else False
        else:
            self.isMouseOver = False

    def Update(self):
        self.__user_input()
        self.__draw()


class TextBox():
    def __init__(self, Surface, position, dimensions, bg_color, highlight, max_txt, font="SourceCodePro-Light", font_size=10, txt_color=(0, 0, 0)):
        # Attributes
        self.surface = Surface
        self.position = position
        self.dimensions = dimensions
        self.color = bg_color
        self.highlight = highlight
        self.max_txt = max_txt
        self.font = font_dir + font + ".ttf"
        self.font_size = font_size
        self.text_color = txt_color

        self.x, self.y = self.position
        self.width, self.height = self.dimensions

        self.isActive = False
        self.cursor = 0
        self.text = []

    def draw(self):

        # Check if the box is active
        if (pg.mouse.get_pressed() == (1, 0, 0)):
            if (self.x < pg.mouse.get_pos()[0] < self.x + self.width) and (self.y < pg.mouse.get_pos()[1] < self.y + self.height):
                self.isActive = True
            else:
                self.isActive = False

        if self.isActive:
            color = self.highlight
        else:
            color = self.color
        # Generate text box bg*
        box_img = pg.Surface(self.dimensions)
        box_rect = box_img.get_rect()
        box_rect.topleft = self.position
        box_img.fill(color)

        # Generate text
        font = pg.font.Font(self.font, self.font_size)
        txt = "".join(self.text)
        txt = font.render(txt, True, self.text_color)
        txt_size = txt.get_size()

        padding = 5

        # Center the text while leaving a padding
        if txt_size[0] > self.dimensions[0]:
            x, y = self.width - (txt_size[0] + padding), (self.height//2) - (txt_size[1]//2)
        else:
            x, y = padding, (self.height // 2) - (txt_size[1]//2)

        pos = (x, y)

        # Render the textbox
        box_img.blit(txt, pos)
        self.surface.blit(box_img, self.position)

    def user_input(self, event):

        # Get user input
        keys = [13, 273, 274, 275, 276, 8, 127]
        if self.isActive:
            if event.key not in keys and len(self.text) < self.max_txt:
                self.text.insert(self.cursor, event.unicode)
                self.cursor += 1
            elif event.key == 8 and len(self.text) > 0 and self.cursor > 0:
                del self.text[self.cursor - 1]
                self.cursor -= 1
            elif event.key == 276 and self.cursor != 0:
                self.cursor -= 1
            elif event.key == 275 and self.cursor < len(self.text):
                self.cursor += 1
            elif event.key == 127 and self.cursor < len(self.text):
                del self.text[self.cursor]
            print(event.unicode)
