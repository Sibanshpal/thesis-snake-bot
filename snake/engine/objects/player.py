from pygame import image

from snake.assets import get_absolute_file_path, SNAKE_HEAD
from snake.utils.logger import Logger
from snake import FIELD_SIZE


class Player:
    def __init__(self, config):
        self.__game_state = config["gamestate"]
        self.__game_state.register_player(self)
        self.__board_size = config["board_size"]
        self.__move_sleep = config["move_sleep"]
        self.__position = (3*FIELD_SIZE, 3*FIELD_SIZE)
        self.__direction = (1,0)
        self.__ellapsed_from_move = 0
        self.__TILE = image.load(get_absolute_file_path(SNAKE_HEAD))
        Logger.log_trace(self, "Player initialized")

    def get_position(self):
        return self.__position

    def process(self, delta):
        self.__ellapsed_from_move = self.__ellapsed_from_move + delta
        if self.__ellapsed_from_move > self.__move_sleep:
            self.__ellapsed_from_move = 0
            self.move(
                self.__direction[0],
                self.__direction[1]
            )

    def render(self, display):
        display.blit(
            self.__TILE, 
            self.__position
        )

    def move(self, x, y):
        new_position = (
            self.__position[0] + x * FIELD_SIZE, 
            self.__position[1] + y * FIELD_SIZE
        )
        self.can_move_to(new_position)
        if not self.__game_state.is_game_finished():
            self.__position = new_position
            self.__game_state.add_move()
            self.eat(self.__position)

    def can_move_to(self, new_position):
        if self.__game_state.is_field_taken(new_position):
            self.__game_state.finish_game()
        
    def eat(self, position):
        if self.__game_state.is_there_a_fruit(position):
            self.__game_state.remove_fruit()
            self.__game_state.add_point()

    def up(self):
        self.__direction = ( 0,-1)

    def down(self):
        self.__direction = ( 0, 1)

    def left(self):
        self.__direction = (-1, 0)

    def right(self):
        self.__direction = ( 1, 0)
