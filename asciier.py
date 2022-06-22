import pygame
import cv2


class ArtConverter:
    def __init__(self, path="sm777.jpg", font_size=10):
        pygame.init()
        self.path = path
        self.image = self.get_image()
        self.RES = self.WIDTH, self.HEIGHT = self.image.shape[0], self.image.shape[1]
        self.surface = pygame.display.set_mode(self.RES)
        self.clock = pygame.time.Clock()

        self.ASCII_CHARS = "!@#$%^&*№;:?xmoqwerty12367890"
        self.ASCII_COEF = 255 // (len(self.ASCII_CHARS) - 1)
        self.font = pygame.font.SysFont("Courier", font_size, bold=True)
        self.CHAR_STEP = int(font_size * 0.6)
        self.RENDERED_ASCII_CHARS = [self.font.render(char, False, 'white') for char in self.ASCII_CHARS]

    def draw_converted_image(self):
        char_indexes = self.image // self.ASCII_COEF
        for x in range(0, self.WIDTH, self.CHAR_STEP):
            for y in range(0, self.HEIGHT, self.CHAR_STEP):
                char_index = char_indexes[x, y]
                if char_index:
                    self.surface.blit(self.RENDERED_ASCII_CHARS[char_index], (x, y))

    def get_image(self):
        self.cv2_image = cv2.imread(self.path)
        tr_image = cv2.transpose(self.cv2_image)
        gray_image = cv2.cvtColor(tr_image, cv2.COLOR_RGB2GRAY)
        return gray_image

    def draw_cv2_image(self):
        resz_cv2_im = cv2.resize(self.cv2_image, (self.WIDTH, self.HEIGHT), interpolation=cv2.INTER_AREA)
        cv2.imshow("img", resz_cv2_im)

    def draw(self):
        self.surface.fill("black")
        self.draw_converted_image()
        self.draw_cv2_image()

    def run(self):
        while True:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    exit()
            self.draw()
            pygame.display.set_caption(str(self.clock.get_fps()))
            pygame.display.flip()
            self.clock.tick()


if __name__ == '__main__':
    app = ArtConverter()
    app.run()
