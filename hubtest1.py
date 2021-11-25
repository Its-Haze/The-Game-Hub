import pygame
from sys import exit
from eriks_runner import play_runner
from tetris import play_tetris


class Image:
    def __init__(self, image_url, pos):
        self.image_surface = pygame.image.load(image_url).convert_alpha()
        self.image_rect = self.image_surface.get_rect(midtop=pos)

    def draw(self, _screen):
        _screen.blit(self.image_surface, self.image_rect)


class Text:
    def __init__(self, text, pos, color):
        self.text = text
        self.color = color
        self.font = pygame.font.SysFont('Comic Sans MS', 40)
        self.text_surface = self.font.render(self.text, False, self.color)
        self.text_rect = self.text_surface.get_rect(midtop=pos)

    def draw(self, _screen):
        _screen.blit(self.text_surface, self.text_rect)

    def update_text(self, text):
        self.text_surface = self.font.render(text, False, self.color)

    def update_color(self, color):
        self.text_surface = self.font.render(self.text, False, color)


class Game:
    text: Text
    image: Image

    def __init__(self, text, image):
        self.text = text
        self.image = image


def start_game_hub():
    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    clock = pygame.time.Clock()
    running = True

    pygame.font.init()  # Behövs för att initiera fonts

    menu_text = Text('Game hub', (400, 50), 'White')
    runner_text = Text('Runner', (200, 150), 'White')
    tetris_text = Text('Tetris', (600, 150), 'White')

    list_of_games = []
    runner = Game(runner_text, Image('Runner_folder/graphics/medium_runner.png', (200, 200)))
    tetris = Game(tetris_text, Image('Tetris_folder/medium_tetris.png', (600, 200)))
    list_of_games.append(runner)
    list_of_games.append(tetris)

    while running:
        screen.fill('Black')
        # Change screen to the current game
        menu_text.draw(screen)
        for game in list_of_games:
            game.text.draw(screen)
            game.image.draw(screen)

        # When user click "runner", play "runner"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if tetris.image.image_rect.collidepoint(event.pos):
                    print('Klickade på tetris')
                    play_tetris()
                if runner.image.image_rect.collidepoint(event.pos):
                    print('Klickade på runner')
                    play_runner()


        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    start_game_hub()
