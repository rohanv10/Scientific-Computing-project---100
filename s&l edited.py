import turtle
screen=turtle.Screen()
screen.setup(580,580)
image="snl.gif"
screen.addshape(image)
bg=turtle.Turtle()
bg.shape(image)

p1=turtle.Turtle()
p1.color('red')

player1 = 0
player2 = 0
def check_for_snakes_and_ladders(n):
	ladders = {1:38,4:14,9:31,21:42,28:84,36:44,51:67,71:91,80:100}
	snakes = {98:78,95:75,93:73,87:24,64:60,62:19,56:53,49:11,48:26,16:6}
	if ladders.has_key(n):
		print "Its a ladder,Climb up"
		n = ladders[n]
	elif snakes.has_key(n):
		print "Its a snake!!,Come down"
		n = snakes[n]
	return n
	
import random
min = 1
max = 6
def roll_dice(r):
    d = random.randint(min, max)
    d = r + d
    return d
			
while player1 < 100 or player2 < 100:
	print "Its turn of player1\n"
	player1 = roll_dice(player1)
	player1 = check_for_snakes_and_ladders(player1)
	print "Current status of Player1:",player1,"and Player2:",player2
 	if player1 > 99:
		print "Winner of the game is player1"
 	print "Its turn of player2\n"
	player2 = roll_dice(player2)
	player2 = check_for_snakes_and_ladders(player2)
	print "Current status of Player1:",player1," and Player2:",player2
 	if player2 > 99:
		print "Winner of the game is player2"