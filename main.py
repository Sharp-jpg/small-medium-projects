import pygame

pygame.init()

class Game:

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
        self.turn = 0

        #zone creation
        self.middle_zone = Zone(280, 280)
        self.mid_left_zone = Zone(30, 280)
        self.mid_right_zone = Zone(530, 280)
        self.top_left_zone = Zone(30, 30)
        self.top_mid_zone = Zone(280, 30)
        self.top_right_zone = Zone(530, 30)
        self.bottom_left_zone = Zone(30, 530)
        self.bottom_mid_zone = Zone(280, 530)
        self.bottom_right_zone = Zone(530, 530)


    def main_loop(self):
         while self.running:

            self.screen.fill(self.screen_color)

            background = Background()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            #self.debug()
            pygame.display.flip()
            self.fps_clock.tick(self.fps)



    def debug(self):
        print(pygame.mouse.get_pos())


class Background:

    def __init__(self):
        self.width = 10
        self.color = (255, 255, 255)

        self.start_vert_y = 35
        self.end_vert_y = 765
        self.start_horiz_x = 35
        self.end_horiz_x = 765

        self.left_vert = pygame.draw.line(game.screen, self.color, (275, self.start_vert_y), (275, self.end_vert_y), self.width)
        self.right_vert = pygame.draw.line(game.screen, self.color, (525, self.start_vert_y), (525, self.end_vert_y), self.width)
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
        self.center_x = self.x + (self.width / 2)
        self.center_y = self.y + (self.height / 2)
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        

class Figure():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 100
        self.center = (self.x, self.y)
        self.width = 25

        self.x_color = (0, 255, 224)
        self.o_color = (255, 45, 0)
        self.black = (0, 0, 0)

    def render_x(self):
        pygame.draw.line(game.screen, self.x_color, self.center, (self.x - 100, self.y - 100), self.width)
        pygame.draw.line(game.screen, self.x_color, self.center, (self.x + 100, self.y - 100), self.width)
        pygame.draw.line(game.screen, self.x_color, self.center, (self.x - 100, self.y + 100), self.width)
        pygame.draw.line(game.screen, self.x_color, self.center, (self.x + 100, self.y + 100), self.width)

    def render_o(self):
        pygame.draw.circle(game.screen, self.o_color, self.center, self.radius)
        pygame.draw.circle(game.screen, self.black, self.center, self.radius - 10)

    def render(self):

        if game.turn % 2 == 0:
            self.render_x()
            game.turn += 1
        else:
            self.render_o()
            game.turn += 1















if __name__ == '__main__':
    game = Game()
    game.main_loop()
