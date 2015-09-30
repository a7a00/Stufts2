# Alex Gould
# 9/26/15
# COMP50CP
# transform_image.py - Uses multithreading to concurrently alter
# sections of an image.
# Since the threads never share resources, there's no real need to
# coordinate them, apart from making sure they're all done
# before continuing with the program

from threading import Thread
import sys
from PIL import Image

global MAX_THREADS

def switch_r_b((r,g,b)):
	return (b,g,r)

def negate((r,g,b)):
	return (255-r, 255-g, 255-b)

def greenonly((r,g,b)):
	return (0,255,0)

tfDict = {"switch-r-b":switch_r_b, "negate":negate, "green":greenonly}

def transformSection(pixels, tf, x, width, y, height):
	temp_x = x
	for i in range(width):
		temp_y = y
		for j in range(height):
			try:
				pixels[temp_x,temp_y] = tf(pixels[temp_x,temp_y])
			except:
				#print "Error at " + str(x) + ", " + str(temp_y)
				break
			temp_y = temp_y+1
		temp_x = temp_x+1

def threading(infile, outfile, tf, numrows, numcols):
	pic = Image.open(infile)
	width, height = pic.size
	if numcols > width:
		numcols = width
	if numrows > height:
		numrows = height
	xcoords = []
	ycoords = []
	xcount = 0
	ycount = 0
	colwidth = width/numcols
	rowheight = height/numrows
	while xcount < width:
		ycount = 0
		while ycount < height:
			xcoords.append(xcount)
			ycoords.append(ycount)
			ycount = ycount + rowheight
		xcount = xcount + colwidth
	pixels = pic.load()
	threads = []
	#print "Width: " + str(width)
	#print "Height: " + str(height)
	#print xcoords
	#print ycoords
	#print xcoords
	#print ycoords
	for i in range(len(xcoords)):
		#print "X: " + str(xcoords[i])
		#print "Y: " + str(ycoords[i])
		threads.append(Thread(target = transformSection, \
			args = (pixels, tf, xcoords[i], colwidth, \
				ycoords[i], rowheight)))
	for i in threads:
		i.start()
	for i in threads:
		i.join()
	pic.save(outfile)

def main(argv):
	MAX_THREADS = 200
	if len(argv) != 4 and len(argv) != 6:
		sys.stderr.write("Wrong number of arguments!\n");
		sys.exit(1)
	infile = argv[1]
	outfile = argv[2]
	func = argv[3]
	if len(argv) == 6:
		rows = int(argv[4])
		cols = int(argv[5])
	else:
		rows = 2
		cols = 2
	if rows*cols > MAX_THREADS:
		sys.stderr.write("Too many threads!\n")
		sys.exit(1)
	threading(infile, outfile, tfDict[func], rows, cols)

if __name__ == '__main__':
	main(sys.argv)

