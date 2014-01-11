import random, cmd, sys

class randgame(cmd.Cmd):
	intro = "this is randgame"
	prompt = "randgame # "
	players = ["asdf", "foo"]
	turn = 0
	rounds = 0
	active = False
	settings = {"no_two" : 0, "voice" : 0}

	def do_set(self, arg):
		'set settings. see \"list settings\" for available options'
		if arg == "" or len(arg.split()) != 2:
			print "*** syntax: set <key> <value>, where value may be 0 or 1"
			return
		setting, value = arg.split()
		if setting not in self.settings.keys():
			print '*** unrecognized setting. available settings: {0}'.format(", ".join(self.settings.keys()))
			return
		if value not in ['0', '1']:
			print "*** value must be 0 or 1" 
			return
		self.settings[setting] = int(value)
	
	def do_start(self, arg):
		'starts the game'
		if self.active == False:
			print "Game Started! glhf"
			self.active = True
			self.shuffle()
			self.do_next(1)
		else:
			print "*** Game already started! use \"next\" instead"
	
	def do_next(self, arg):
		'shows next player'
		if self.active == False :
			print "*** No active game, use \"start\" first"
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
			self.rounds += 1

	def do_end(self, arg):
		'ends current game (but does not exit)'
		if self.active != True:
			print "*** no active game!"
			return
		self.turn = 0
		self.active = False
		print "game ended after {0} rounds!".format(self.rounds)
		self.rounds = 0
		
		
	def shuffle(self):
		if self.settings["no_two"] == 0 :
			random.shuffle(self.players)
		else:
			last_player = self.players.pop()
			random.shuffle(self.players)
			self.players.insert( random.randint(1,len(self.players)), last_player)

	
	def do_addplayer(self, arg):
		'add a player to the game'
		if self.active == True:
			print "*** can't add player during active game"
			return
			
		if arg != "":
			if arg not in self.players:
				self.players.append(arg)
			else:
				print "*** player already added, please specify a different name"
		else:
			print "*** please specify a name"
			
	def do_remove(self, arg):
		'remove a player from the game'
		if self.active == True:
			print "*** can't remove player during game"
			return
		try:
			self.players.remove(arg)
			print "removed player {0} from game".format(arg)
		except ValueError:
			print "*** player not in game (check spelling?)"

	
	def do_list(self, arg):
		'list settings or list players'
		if arg == "settings":
			print "settings: "
			for key in self.settings:
				print "\t{0}\t{1}".format(key, self.settings[key])
		elif arg == "players":
			print ", ".join(map(str, self.players))
		else:
			print "*** \"list settings\" or \"list players\""
		
	def do_q(self, arg):
		'exit the program'
		return True
		
	def do_exit(self, arg):
		'exit the program'
		return True

	def do_EOF(self,arg):
		'exit the program'
		return True

if __name__ == '__main__':
    randgame().cmdloop()
