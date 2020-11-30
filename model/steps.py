
class Steps:
    def __init__(self):
        self.players = []
        self.has_started = False
        self.winners = []
        self.is_awake = False
        self.step_count = 100

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, players):
        self.__players = players

    @property
    def winners(self):
        return self.__winners

    @winners.setter
    def winners(self, winners):
        self.__winners = winners

    @property
    def has_started(self):
        return self.__has_started

    @has_started.setter
    def has_started(self, has_started):
        self.__has_started = has_started
     
    @property
    def is_awake(self):
        return self.__is_awake

    @is_awake.setter
    def is_awake(self, is_awake):
        self.__is_awake = is_awake

    @property
    def step_count(self):
        return self.__step_count

    @is_awake.setter
    def step_count(self, step_count):
        self.__step_count = step_count
