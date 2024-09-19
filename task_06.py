class WrongNumberOfPlayersError(Exception):
    pass

class NoSuchStrategyError(Exception):
    pass

global v
v = ['P', 'R', 'S']

def getIndex(p) -> int:
    try:
        i = v.index(p[1])
        return i
    except:
        raise NoSuchStrategyError("Вы используете что-то не то.")

def rps_game_winner(players):
    if (len(players) > 2): raise WrongNumberOfPlayersError("В игре может быть только 2 игрока.")
    p1, p2 = players[0], players[1]
    i1, i2 = getIndex(p1), getIndex(p2)
    if (i1 == i2 or i1 > i2): return p1[0] + " " + p1[1]
    else: return p2[0] + " " + p2[1]

# rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]) # => WrongNumberOfPlayersError
# rps_game_winner([['player1', 'P'], ['player2', 'A']])                   # => NoSuchStrategyError
print(rps_game_winner([['player1', 'P'], ['player2', 'S']]))                   # => 'player2 S'
rps_game_winner([['player1', 'P'], ['player2', 'P']])                   # => 'player1 P'
rps_game_winner([['player1', 'S'], ['player2', 'P']])                   # => 'player1 S'