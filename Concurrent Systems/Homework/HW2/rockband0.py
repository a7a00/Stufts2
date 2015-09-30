# Read data from file and play it

import sys
from pyglet import media
from time import sleep

def playSounds(instrument, notes):
	sound = media.load(instrument, streaming=False)
	pitch = 0
	for c in notes:
		if c.isdigit():
			player = media.Player()
			player.queue(sound)
			player.pitch = (2.0**(float(c)/12))
			#player.pitch = int(c)
			print player.pitch
			player.play()
			sleep(2)

def main(argv):
	with open(argv[1]) as f:
		for line in f:
			playSounds(line.split(" ")[0], line.split(" ")[1])

if __name__ == '__main__':
	main(sys.argv)
