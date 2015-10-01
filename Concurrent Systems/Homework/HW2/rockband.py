import sys
import threading
from pyglet import media
from time import sleep

class ThreadCounter:
	count = 0
	total = 6
	def __init__(self):
		self.count = 0
	def get():
		return count
	def increment():
		count += 1
	def decrement():
		count -= 1
	def setNum(threads):
		total = threads
	def getNum():
		return total

def playSounds(instrument, notes, mutex, turnstile, turnstile2, counter):
	sound = media.load(instrument, streaming=False)
	pitch = 0
	for c in notes:
		mutex.acquire()
		counter.increment()
		if counter.get() == counter.getNum():
			turnstile2.acquire()
			turnstile.release()
		mutex.release()
		turnstile.acquire()
		turnstile.release()
		if c.isdigit():
			player = media.Player()
			player.queue(sound)
			player.pitch = (2.0**(float(c)/12))
			#player.pitch = int(c)
			#print player.pitch
			player.play()
			sleep(2)
		mutex.acquire()
		counter.decrement()
		if counter.get() == 0:
			turnstile.acquire()
			turnstile2.release()
		mutex.release()
		turnstile2.acquire()
		turnstile2.release()

def main(argv):
	threads = []
	mutex = threading.Semaphore()
	turnstile = threading.Semaphore()
	turnstile2 = threading.Semaphore()
	counter = ThreadCounter()
	with open(argv[1]) as f:
		for line in f:
			threads.append(threading.Thread(target = playSounds, args = \
				(line.split(" ")[0], line.split(" ")[1], mutex, turnstile, \
					turnstile2, counter)))
	counter.setNum(len(threads))
	for i in threads:
		i.start()
	for i in threads:
		i.join()

if __name__ == '__main__':
	main(sys.argv)
