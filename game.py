
class Move:
	def __init__(self, cooperate=True):
		self.cooperate = cooperate
# Initiate
	def __str__ (self):
		if self.cooperate == True:
			return "."
		elif self.cooperate == False:
			return "x"
# True False cases
	def __repr__(self):
		str1 = "Move("+str(self.cooperate)+")"
		return str1
# return the string corresponding to cooperate status
	def __eq__ (self, other):
		if repr(self) == repr(other):
			return True
		else:
			return False
# if the same return True if not return False
	def change (self):
		if self.cooperate == True:
			self.cooperate = False
		else:
			self.cooperate = True
# change status
	def copy (self):
		x = Move(self.cooperate)
		return x
class PlayerException(Exception):
	def __init__(self, msg):
		self.msg = msg
# initiate
	def __str__ (self):
		return self.msg
# return msg
	def __repr__(self):
		return "PlayerException('"+self.msg+"')"
# return the string corresponding the msg		
class Player:
	def __init__(self, style, points=0, history=None):
		self.style = style
		self.points = points
		self.history = history
# initiate these three
		if self.history == None:
			self.history = []
# when no history of moves then its empty
		x = ["previous","friend","cheater","grudger","detective"]
		if self.style not in x:
			raise PlayerException("no style '"+self.style+"'.")
# if style isn't one of the five raise the exception
	def __str__ (self):
		z = []
		if len(self.history) > 0:
			for i in range(len(self.history)):
				z.append(self.history[i].__str__())		
		y = "".join(z)
		return ""+self.style+"("+str(self.points)+")"+y+""
# get the required string
	def __repr__(self):
		z = []
		if len(self.history) > 0:
			for i in range(len(self.history)):
				z.append(self.history[i].__repr__())		
		y = ", ".join(z)
		return "Player('"+self.style+"', "+str(self.points)+", ["+y+"])"
# same concept get the required string
	def reset_history(self):
		self.history = []
# get history empty
	def reset(self):
	    self.history = []
	    self.points = 0
# get history empty get points to 0
	def update_points(self, amount):
		self.points += amount
# add the amount to points
	def ever_betrayed(self):
		z = []
		if self.history == []:
			return False
		if len(self.history) > 0:
			for i in range(len(self.history)):
				if self.history[i].__str__() == 'x':
					return True
				else:
					continue
			return False
# check history if there's x then the player has been betrayed
	def record_opponent_move(self, move):
		self.history.append(move)
# add move in the history
	def copy_with_style(self):
		player = Player(self.style)
		return player
# get a player with same style
	def choose_move(self):
		if self.style == "previous":
			if len(self.history) < 1:
				return Move(True)
			x = self.history[-1].cooperate
			return Move(x)
# check the last move and do the same, if no moves start with cooperate
		if self.style == "friend":
			return Move(True)
# always cooperate
		if self.style == "cheater":
			return Move(False)
# always non-cooperate
		if self.style == "grudger":
			for i in self.history:
				if i.cooperate == False:
					return Move(False)
				else:
					continue
			return Move(True)
# always cooperate until gets betrayed then turn to cheater
		if self.style == "detective":
			if len(self.history) == 0:
				return Move(True)
			if len(self.history) == 1:
				return Move(False)
			if len(self.history) == 2:
				return Move(True)
			if len(self.history) == 3:
				return Move(True)
# first four moves are given
			if len(self.history) >= 4:
					for i in range(len(self.history)):
						if self.history[i].__str__() == 'x':
							x = self.history[-1].cooperate
							return Move(x)
						else:
							continue
					return Move(False)
# after the first 4 if gets betrayed acts like previous, if not becomes cheater
def turn_payouts (move_a, move_b):
	if move_a == Move(True) and move_b == Move(True):
		return (2,2)
	elif move_a == Move(False) and move_b == Move(False):
		return (0,0)
	elif move_a == Move(False) and move_b == Move(True):
		return (3,-1)
	elif move_a == Move(True) and move_b == Move(False):
		return (-1,3)
# return the tuple based on moves		
def build_players(initials):
    x = ["p","f","c","g","d"]
    y = []
    for i in initials:
        if i == "p":
            y.append(Player("previous"))
        if i == "f":
            y.append(Player("friend"))
        if i == "c":
            y.append(Player("cheater"))
        if i == "g":
            y.append(Player("grudger"))
        if i == "d":
            y.append(Player("detective"))
        if i not in x:
            raise PlayerException ("no style with initial '"+i+"'.")
    return y
# return the Player of the correspond initial, if not one of the 5 then raise
def composition(players):
    dictionary = {}
    for i in players:
        if i.style not in dictionary.keys():
            dictionary[i.style] = 1
        else:
            dictionary[i.style]+=1
    return dictionary
# put the players to key and value is the number of that player
def run_turn(player_a, player_b):
    if id(player_a) == id(player_b):
        raise PlayerException("players must be distinct.")
# when they identical
    else:
        player_a.update_points(-1)
        player_b.update_points(-1)
# start with paying 1 point for each
        move_a = player_a.choose_move()
        move_b = player_b.choose_move()
# get their moves
        player_a.record_opponent_move(move_b)
        player_b.record_opponent_move(move_a)
# get opponents
        a,b=turn_payouts(move_a,move_b)
# see pay outs and set a,b to the payout amount for player a and b
        player_a.update_points(a)
        player_b.update_points(b)
# add amount to points
def run_game(player_a, player_b, num_turns=5):
    if id(player_a) != id(player_b):
        player_a.reset_history()
        player_b.reset_history()
        for i in range(num_turns):
            run_turn(player_a, player_b)
# when they are not identical reset history
# and run turns so the points will update
