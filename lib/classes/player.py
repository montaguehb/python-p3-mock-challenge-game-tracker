class Player:

    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []
        Player.all.append(self)
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
            if(2 <= len(username) <= 16):
                self._username = username
            else:
                raise AttributeError
            
    def results(self, new_result=None):
        from classes.result import Result
        if(new_result):
            self._results.append(new_result)
        return [result for result in Result.all if result.player == self]
    
    def games_played(self, new_game=None):
        from classes.game import Game
        if(new_game):
            self._games_played.append(new_game)
        return [game for game in Game.all if self in game._players]
    
    def played_game(self, game):
        return game in self._games_played
    
    def num_times_played(self, game):
        return len([played for played in self._games_played if game == played])
    
    @classmethod
    def highest_scored(cls, game):
        pass
        
