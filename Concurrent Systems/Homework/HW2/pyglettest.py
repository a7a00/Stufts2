from pyglet import media
from time import sleep

def playSounds(instrument, notes):
	sound = media.load(instrument, streaming=False)
	pitch = 0
	for c in notes:
		if c != "x":
			player = media.Player()
			player.queue(sound)
			player.pitch = (2.0**(float(c)/12))
			#player.pitch = int(c)
			print player.pitch
			player.play()
			sleep(2)

if __name__ == '__main__':
	#playSounds("./media/6th_String_E_64kb.wav", "1x232xx11")
	playSounds("./media/3rd_String_G_64kb.wav", "314159265358979")
