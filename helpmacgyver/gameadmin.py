
import pygame


class GameAdmin:
    """ I'm the admin of the game. """
    def __init__(self, window):
        self.window = window

    def loose_game(self):
        """ I'm saying this is a loose game and I'm closing the game. """
        self.msg_loose()
        self.state = False
        pygame.time.wait(3000)
        return self.state

    def win_game(self):
        """ I'm saying this is a win game and I'm closing the game. """
        self.msg_win()
        pygame.time.wait(3000)
        self.state = False
        return self.state

    def msg_loose(self):
        """ I display the loose text. """
        font = pygame.font.SysFont("arial", 56)
        text = font.render("  You loose !  ", True, (255, 255, 255), (0, 0, 0))
        self.window.blit(text, (200, 300))
        pygame.display.flip()

    def msg_win(self):
        """ I display the win text"""
        font = pygame.font.SysFont("arial", 56)
        text = font.render("  You win !  ", True, (0, 0, 0), (255, 255, 255))
        self.window.blit(text, (200, 300))
        pygame.display.flip()
