import pygame

#Output to EyeBraille
#from convertOutput import *

pygame.init()
##screen = pygame.display.set_mode((640, 480))
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font('freesansbold.ttf', 20)


class InputBox:

    def __init__(self, screen, x, y, w, h, text=''):
        self.screen = screen
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.txt_start = 0
        self.txt_display_length = 16

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)

                    # Write text to file
                    f = open ("Text_File.txt", "w+")
                    f.write(self.text)
                    f.close()

                    #convert()

                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

                # Adjust for text out of bounds
                if len(self.text) >= self.txt_display_length:
                    self.txt_start = len(self.text) - self.txt_display_length

                # Re-render the text.
                self.txt_surface = FONT.render(self.text[self.txt_start:len(self.text)], True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, 100) #self.txt_surface.get_width()+10
        self.rect.w = width

    def draw(self):
        # Blit the text.
        self.screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(self.screen, self.color, self.rect, 2)
