##import pygame as pg
##
##
##def main():
##    screen = pg.display.set_mode((640, 480))
##    font = pg.font.Font(None, 32)
##    clock = pg.time.Clock()
##    input_box = pg.Rect(100, 100, 140, 32)
##    color_inactive = pg.Color('lightskyblue3')
##    color_active = pg.Color('dodgerblue2')
##    color = color_inactive
##    active = False
##    text = ''
##    done = False
##
##    while not done:
##        for event in pg.event.get():
##            if event.type == pg.QUIT:
##                done = True
##            if event.type == pg.MOUSEBUTTONDOWN:
##                # If the user clicked on the input_box rect.
##                if input_box.collidepoint(event.pos):
##                    # Toggle the active variable.
##                    active = not active
##                else:
##                    active = False
##                # Change the current color of the input box.
##                color = color_active if active else color_inactive
##            if event.type == pg.KEYDOWN:
##                if active:
##                    if event.key == pg.K_RETURN:
##                        print(text)
##                        text = ''
##                    elif event.key == pg.K_BACKSPACE:
##                        text = text[:-1]
##                    else:
##                        text += event.unicode
##
##        screen.fill((30, 30, 30))
##        # Render the current text.
##        txt_surface = font.render(text, True, color)
##        # Resize the box if the text is too long.
##        width = max(200, txt_surface.get_width()+10)
##        input_box.w = width
##        # Blit the text.
##        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
##        # Blit the input_box rect.
##        pg.draw.rect(screen, color, input_box, 2)
##
##        pg.display.flip()
##        clock.tick(30)
##
##
##if __name__ == '__main__':
##    pg.init()
##    main()
##    pg.quit()




##import pygame as pg
##
##
##pg.init()
##screen = pg.display.set_mode((640, 480))
##COLOR_INACTIVE = pg.Color('lightskyblue3')
##COLOR_ACTIVE = pg.Color('dodgerblue2')
##FONT = pg.font.Font(None, 32)
##
##
##class InputBox:
##
##    def __init__(self, x, y, w, h, text=''):
##        self.rect = pg.Rect(x, y, w, h)
##        self.color = COLOR_INACTIVE
##        self.text = text
##        self.txt_surface = FONT.render(text, True, self.color)
##        self.active = False
##
##    def handle_event(self, event):
##        if event.type == pg.MOUSEBUTTONDOWN:
##            # If the user clicked on the input_box rect.
##            if self.rect.collidepoint(event.pos):
##                # Toggle the active variable.
##                self.active = not self.active
##            else:
##                self.active = False
##            # Change the current color of the input box.
##            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
##        if event.type == pg.KEYDOWN:
##            if self.active:
##                if event.key == pg.K_RETURN:
##                    print(self.text)
##                    self.text = ''
##                elif event.key == pg.K_BACKSPACE:
##                    self.text = self.text[:-1]
##                else:
##                    self.text += event.unicode
##                # Re-render the text.
##                self.txt_surface = FONT.render(self.text, True, self.color)
##
##    def update(self):
##        # Resize the box if the text is too long.
##        width = max(200, self.txt_surface.get_width()+10)
##        self.rect.w = width
##
##    def draw(self, screen):
##        # Blit the text.
##        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
##        # Blit the rect.
##        pg.draw.rect(screen, self.color, self.rect, 2)
##
##
##
##def main():
##    clock = pg.time.Clock()
##    input_box1 = InputBox(100, 100, 140, 32)
##    input_box2 = InputBox(100, 300, 140, 32)
##    input_boxes = [input_box1, input_box2]
##    done = False
##
##    while not done:
##        for event in pg.event.get():
##            if event.type == pg.QUIT:
##                done = True
##            for box in input_boxes:
##                box.handle_event(event)
##
##        for box in input_boxes:
##            box.update()
##
##        screen.fill((30, 30, 30))
##        for box in input_boxes:
##            box.draw(screen)
##
##        pg.display.flip()
##        clock.tick(30)
##
##
##if __name__ == '__main__':
##    main()
##    pg.quit()





import pygame
pygame.init()
validChars = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
shiftChars = '~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'

class TextBox(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.text = ""
    self.font = pygame.font.Font(None, 50)
    self.image = self.font.render("Enter your name", False, [0, 0, 0])
    self.rect = self.image.get_rect()

  def add_chr(self, char):
    global shiftDown
    if char in validChars and not shiftDown:
        self.text += char
    elif char in validChars and shiftDown:
        self.text += shiftChars[validChars.index(char)]
    self.update()

  def update(self):
    old_rect_pos = self.rect.center
    self.image = self.font.render(self.text, False, [0, 0, 0])
    self.rect = self.image.get_rect()
    self.rect.center = old_rect_pos


screen = pygame.display.set_mode([640, 480])
textBox = TextBox()
shiftDown = False
textBox.rect.center = [320, 240]

running = True
while running:
  screen.fill([255, 255, 255])
  screen.blit(textBox.image, textBox.rect)
  pygame.display.flip()
  for e in pygame.event.get():
    if e.type == pygame.QUIT:
        running = False
    if e.type == pygame.KEYUP:
        if e.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
            shiftDown = False
    if e.type == pygame.KEYDOWN:
        textBox.add_chr(pygame.key.name(e.key))
        if e.key == pygame.K_SPACE:
            textBox.text += " "
            textBox.update()
        if e.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
            shiftDown = True
        if e.key == pygame.K_BACKSPACE:
            textBox.text = textBox.text[:-1]
            textBox.update()
        if e.key == pygame.K_RETURN:
            if len(textBox.text) > 0:
                print (textBox.text)
                running = False
pygame.quit()
