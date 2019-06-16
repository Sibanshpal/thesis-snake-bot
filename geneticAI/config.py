from snake.utils import logger_levels
from snake import DEFAULT_CONFIG, AI_MODE, DISPLAY_OFF

ai_config = dict(DEFAULT_CONFIG)
ai_config["board_size"] = (10, 10)
ai_config["game_mode"] = AI_MODE
ai_config['move_sleep'] = 1
ai_config['log_level'] = logger_levels.NONE
ai_config['display_mode'] = DISPLAY_OFF

RUN_CONFIG = dict(
    base_game_config=ai_config,
    network_schema=[
        ('dense', 256),
    ],
    population_size=52,
    generations=20,
    generation_mutation_rate=1
)
