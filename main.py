import pygame

pygame.init()

class TicTacToe:

    def __init__(self):
        self.screen_width = 800
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.running = True
        self.screen_color = (0, 0, 0)
        self.fps = 60
        self.fps_clock = pygame.time.Clock()
        self.caption = pygame.display.set_caption('Tic-Tac-Toe')
        self.game_over = False

        self.middle_zone = Zone(280, 280)
        self.mid_left_zone = Zone(30, 280)
        self.mid_right_zone = Zone(530, 280)
        self.top_left_zone = Zone(30, 30)
        self.top_mid_zone = Zone(280, 30)
        self.top_right_zone = Zone(530, 30)
        self.bottom_left_zone = Zone(30, 530)
        self.bottom_mid_zone = Zone(280, 530)
        self.bottom_right_zone = Zone(530, 530)

        self.zones = []


        
    def main_loop(self):
         while self.running:

            self.screen.fill(self.screen_color)

            lines = Lines()
            


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            debug()
            pygame.display.flip()
            self.fps_clock.tick(self.fps)


class Lines:

    def __init__(self):
        self.width = 10
        self.color = (255, 255, 255)

        self.start_vert_y = 35
        self.end_vert_y = 765
        self.left_vert = pygame.draw.line(game.screen, self.color, (275, self.start_vert_y), (275, self.end_vert_y), self.width)
        self.right_vert = pygame.draw.line(game.screen, self.color, (525, self.start_vert_y), (525, self.end_vert_y), self.width)

        self.start_horiz_x = 35
        self.end_horiz_x = 765
        self.top_horiz = pygame.draw.line(game.screen, self.color, (self.start_horiz_x, 275), (self.end_horiz_x, 275), self.width)
        self.bottom_horiz = pygame.draw.line(game.screen, self.color, (self.start_horiz_x, 525), (self.end_horiz_x, 525), self.width)

    def winning_lines(self):
        pass


class Zone:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.populated = False
        self.width = 240
        self.height = 240
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)





def debug():

    print(pygame.mouse.get_pos())
    print(game.middle_zone.hitbox)
    # pygame.draw.line(game.screen, 'white', (0, 0), (800, 800), 1)
    # pygame.draw.line(game.screen, 'white', (800, 0), (0, 800), 1)
    # pygame.draw.line(game.screen, 'white', (0, 0), (800, 800), 1)
    # pygame.draw.line(game.screen, 'white', (400, 0), (400, 800), 1)
    # pygame.draw.line(game.screen, 'white', (0, 400), (800, 400), 1)


if __name__ == '__main__':
    game = TicTacToe()
    game.main_loop()
