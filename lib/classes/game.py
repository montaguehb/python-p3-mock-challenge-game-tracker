class Game:
    all = []
    
    def __init__(self, title):
        if(len(title)):
            self._title = title
        else:
            raise AttributeError
        self._results = []
        self._players = []
        Game.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        raise AttributeError
         
    def results(self, new_result=None):
        from classes.result import Result
        if(new_result):
            self._results.append(new_result)
        return [result for result in Result.all if result.game == self]
    
    def players(self, new_player=None):
        from classes.player import Player
        if(new_player):
            self._players.append(new_player)
        return self._players
    
    def average_score(self, player):
        all_scores = [result.score for result in self._results if result.player == player]
        return sum(all_scores)/len(all_scores)
