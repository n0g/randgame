import random, cmd, sys

players = []
no_two = False # True == no two consecutive turns for one player
#turn
# todo
# add no_two functionality

class randgame(cmd.Cmd):
	intro = "this is randgame"
	prompt = "randgame # "
	file = None
	players = ["asdf", "foo"]
	turn = 0
	no_two = False
	active = False
	def do_f(self, arg):
		print arg

	def do_start(self, arg):
		'starts the game'
		if self.active == False:
			print "Game Started! glhf"
			self.active = True
			self.shuffle()
			self.do_next(1)
		else:
			print "Game already started! use \"next\" instead"
	
	def do_next(self, arg):
		'shows next player'
		if self.active == False :
			print "No active game, use \"start\" first"
			return
		print "#"*50
		print
		print "{0} Player is {1}".format(("First" if arg==1 else "Next"), self.players[self.turn])
		print 
		print "#"*50
		self.turn += 1
		if self.turn == len(self.players):
			self.turn = 0
			self.shuffle()

	def do_end(self, arg):
		'ends current game (but does not exit)'
		self.turn = 0
		self.active = False
		
	def shuffle(self):
		if no_two == False :
			random.shuffle(self.players)
		else:
			new_players = [random.choice(players)]
			while(new_players == last_player):
				new_players = [random.choice(players)]
			players.remove(new_players[0])
			random.shuffle(players)
			new_players += players
			players = new_players
				
	def do_addplayer(self, arg):
		'add a player to the game'
		self.players.append(arg)
		
	def do_list(self, arg):
		'list players'
		print ", ".join(map(str, self.players))
		
	
	def do_e(self, arg):
		'exit the program'
		return True
	
if __name__ == '__main__':
    randgame().cmdloop()

#def init():





#def main():
#	init()

	# wait for space


	#begin
	# call next
	# output result of next
	# wait for input
	# 	space: 	next
	#	enter: 	game won
	#	esc:	restart or exit
	# goto begin 

