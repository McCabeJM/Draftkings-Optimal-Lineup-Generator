

from constants import ALL_POS_TEAM

class Roster:
    POSITION_ORDER = {
        "QB": 0,
        "RB": 1,
        "WR": 2,
        "TE": 3,
        "DST": 4
    }

    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def spent(self):
        return sum(map(lambda x: x.cost, self.players))

    def projected(self):
        return sum(map(lambda x: x.proj, self.players))/10

    def position_order(self, player):
        return self.POSITION_ORDER[player.pos]

    def sorted_players(self):
        return sorted(self.players, key=self.position_order)

    def __repr__(self):
        s = '\n'.join(str(x) for x in self.sorted_players())
        s += "\nProjected Score: %s" % self.projected()
        s += "\tCost: $%s\n" % self.spent()
        return s

class Player:
    def __init__(self, pos, name, team, cost, risk, proj=0, code='aa', marked=None):
        self.pos = pos
        self.name = name
        self.code = code
        self.team = team
        self.cost = int(cost)
        self.risk = risk
        self.proj = proj
        self.marked = marked
        self.cost_ranking = 0

    def player_report(self):
        print self.pos + ' '+ self.name + \
        ' (' + str(self.cost) + ')' + ' (' + str(self.proj/10) + ')'

    def __repr__(self):
        return "[{0: <2}] {1: <20}(${2}, {3})".format(self.pos, \
                                    self.name, \
                                    self.cost, \
                                    self.proj/10)

class Team:
    def __init__(self, give):
        self._set_team_pos(give)
        self.team_cost = self._get_team_prop('cost')
        self.team_proj = self._get_team_prop('proj')

    def team_report(self):
        for pos in ALL_POS_TEAM:
            getattr(self, pos).player_report()

        print 'Total Cost: ' + str(self.team_cost)
        print 'Total Projected: ' + str(self.team_proj)

    def contains_dups(self):
        players = []
        for pos in ALL_POS_TEAM:
            name = getattr(self, pos).name
            players.append(name)

        return len(players) != len(set(players))

    def _set_team_pos(self, give):
        for idx, val in enumerate(give):
            setattr(self, ALL_POS_TEAM[idx], val)

    def _get_team_prop(self, prop):
        val = 0
        for pos in ALL_POS_TEAM:
            val += int(getattr(getattr(self, pos), prop))

        return val
