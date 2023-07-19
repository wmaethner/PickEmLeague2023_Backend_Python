from src.PickEmLeague.models.game import Game


def get_game_list():
    games = Game.find_all()
    return games
