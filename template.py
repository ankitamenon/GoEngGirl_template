import pygame

BLACK = (0, 0, 0)
#PURPLE = insert RGB value here 
#WHITE = insert RGB value here 
#RED =  insert RGB value here 

class Game:
    screen = None
    aliens = []
    rockets = []
    lost = False

    def __init__(self, width, height):
        pygame.init()
        """ insert initializing code here """
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        done = False

        #hero is placed in the screen center
        hero = Hero(self, width / 2, height - 20) #example of object creation
        generator = Generator(self) 
        rocket = None

        while not done:
            if len(self.aliens) == 0:
                """ display victory text here """

            pressed = pygame.key.get_pressed()
            """ insert code here to move left or right """ 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.lost:
                    """ create a rocket object and add it to the list of rockects """

            pygame.display.flip()
            self.clock.tick(60)
            self.screen.fill(BLACK)

            for alien in self.aliens:
                """ call draw """
                """ call check collisions """
                if (alien.y > height):
                    self.lost = True
                    """ display losing text here """

            for rocket in self.rockets:
                """ call draw function """

            if not self.lost: 
                """ call draw function """

    def displayText(self, text):
        pygame.font.init()
        font = pygame.font.SysFont('Arial', 50)
        textsurface = font.render(text, False, (44, 0, 62))
        self.screen.blit(textsurface, (110, 160))


class Alien:
    def __init__(self, game, x, y):
        """ insert initializing code here """
        self.size = 30

    def draw(self):
        """ insert draw code here """

    #check the collision of the rocket and the alien
    def checkCollision(self, game):
        for rocket in game.rockets:
            if (rocket.x < self.x + self.size and
                    rocket.x > self.x - self.size and
                    rocket.y < self.y + self.size and
                    rocket.y > self.y - self.size):
                game.rockets.remove(rocket)
                game.aliens.remove(self)


class Hero:
    def __init__(self, game, x, y):
        """ insert initializing code here """
        

    def draw(self):
        """ insert draw code here """


class Generator:
    def __init__(self, game):
        margin = 30  
        width = 50  
        for x in range(margin, game.width - margin, width):
            for y in range(margin, int(game.height / 2), width):
                game.aliens.append(Alien(game, x, y))


class Rocket:
    def __init__(self, game, x, y):
        """ insert initializing code here """

    def draw(self):
         """ insert draw code here """

if __name__ == '__main__':
    game = Game(600, 400)