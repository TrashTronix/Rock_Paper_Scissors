from random import choice
import time
r='rock'
p='paper'
s='scissors'
select='Select your weapon.'
i='''#######################
# Rock Paper Scissors #
#######################'''
again='Play again? (Yes) (No)'
invalid='Invalid command use (help) for a list of commands'
time.sleep(0.5)
print i
time.sleep(0.5)
print select
def menu(a):
	global invalid,r,p,s,select
	if a=='help':
		help_text('help')
		time.sleep(0.5)
		print select
		menu(human_input())
	elif a=='how':
		help_text('how')
		time.sleep(0.5)
		print select
		menu(human_input())
	elif a=='who':
		help_text('who')
		time.sleep(0.5)
		print select
		menu(human_input())
	elif a=='why':
		help_text('why')
		time.sleep(0.5)
		print select
		menu(human_input())
	elif a=='quit':
		return
	elif a=='':
		menu(human_input())
	elif a==r:
		print''
		time.sleep(0.5)
		print'-You picked rock-'
		game=logic('rock',computer_input())
		result(game)
		replay(human_input())
	elif a==p:
		print''
		time.sleep(0.5)
		print'-You picked paper-'
		game=logic('paper',computer_input())
		result(game)
		replay(human_input())
	elif a==s:
		print''
		time.sleep(0.5)
		print'-You picked scissors-'
		game=logic('scissors',computer_input())
		result(game)
		replay(human_input())
	else:
		time.sleep(0.5)
		print invalid
		time.sleep(0.5)
		menu(human_input())
def help_text(a):
	global select
	rock='-rock		   	-Selects rock as your weapon'
	paper='-paper		        -Selects papper as your weapon'
	scissors='-scissors		-Selects scissors as your weapon'
	how='-how			-How to play'
	who='-who			-Who made this'
	why='-why			-Why I made this'
	quit='-quit			-Exits the game'
	how2='Select a weapon by typing either (rock), (paper),or (scissors) on the command line.'
	who2='To be completed.'
	why2="""	This game was created as a project for my
Digital Art and Design class also known as DAAD.
When I finished the project I decided to make
it as impressive as possible. So now with this game
I am constantly working on it making changes all the
time to it. Even though its on a command line it is
still neat to make things like this, as it gives you
the feeling that you are playing an old text based game
on Dos or Unix, where it was all command line, well
most of the time, to be more specific, a time where
the modern GUI did not exist, and you had no use for a
mouse. The goal of the project was to make a rock,paper,
scissors game in Python, but like I said at the beginning
it became more than a class project for me, it became a
big project in which I wanted to create an old school text
based game. And this one thing has led to inspiration to
create more things like this. Its a different type of
experience to create something like this that looks
hard to make but in reality is simple and fun to
create rather than make something that is modern,
and looks simple, but is extremely complex when it
comes to coding."""
	if a=='help':
		print''
		print'''######################
# Available commands #
######################'''
		time.sleep(0.5)
		print how
		time.sleep(0.5)
		print rock
		time.sleep(0.5)
		print paper
		time.sleep(0.5)
		print scissors
		time.sleep(0.5)
		print who
		time.sleep(0.5)
		print why
		time.sleep(0.5)
		print quit
		print''
	elif a=='how':
		print''
		time.sleep(0.5)
		print how2
		print''
	elif a=='who':
		print''
		time.sleep(0.5)
		print who2
		print''
	elif a=='why':
		print''
		time.sleep(0.5)
		print why2
		print''
def human_input():
	_input_=raw_input('>').lower()
	return _input_
def computer_input():
	global r,p,s
	comp=choice('rps')
	if comp=='r':
		print''
		time.sleep(0.5)
		print'-The computer picked rock-'
		return r
	elif comp=='p':
		print''
		time.sleep(0.5)
		print'-The computer picked paper-'
		return p
	elif comp=='s':
		print''
		time.sleep(0.5)
		print'-The computer picked scissors-'
		return s
def logic(human,computer):
	if human=='rock'and computer=='rock':
		return'tie'
	elif human=='rock'and computer=='paper':
		return'loose'
	elif human=='rock'and computer=='scissors':
		return'win'
	elif human=='paper'and computer=='paper':
		return'tie'
	elif human=='paper'and computer=='scissors':
		return'loose'
	elif human=='paper'and computer=='rock':
		return'win'
	elif human=='scissors'and computer=='scissors':
		return'tie'
	elif human=='scissors'and computer=='rock':
		return'loose'
	elif human=='scissors'and computer=='paper':
		return'win'
def result(l):
	win='''###########
# You win #
###########'''
	loose='''#####################
# The computer wins #
#####################'''
	tie='''#############
# Its a tie #
#############'''
	again='Play again? (Yes) (No)'
	if l=='win':
		print''
		time.sleep(0.5)
		print win
		print''
		time.sleep(0.5)
		print again
	elif l=='loose':
		print''
		time.sleep(0.5)
		print loose
		print''
		time.sleep(0.5)
		print again
	elif l=='tie':
		print''
		time.sleep(0.5)
		print tie
		print''
		time.sleep(0.5)
		print again
def replay(a):
	global select,again,invalid
	if a=='yes':
		print''
		time.sleep(0.5)
		print'#'*20
		time.sleep(0.5)
		print select
		menu(human_input())
	elif a=='no':
		return
	elif a=='':
		time.sleep(0.5)
		print again
		replay(human_input())
	else:
		time.sleep(0.5)
		print invalid
		replay(human_input())
menu(human_input())