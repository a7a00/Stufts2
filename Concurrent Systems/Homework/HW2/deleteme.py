import pyglet
import time
customSound = pyglet.media.load("./media/1st_String_E_64kb.wav", streaming = False)
# Each instrument gets its own media player
player = pyglet.media.Player()
# Play the next sound in the queue if there is one
player.play()
# queue a new sound
player.queue(customSound)
# dividing by number to get different pitches
# Or multiply
# Finally output our sound
time.sleep(4)
