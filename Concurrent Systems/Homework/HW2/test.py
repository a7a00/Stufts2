import sys
def main(argv):
	if len(argv) != 3 and len(argv) != 5:
		sys.stderr.write("BAD\n")
	else:
		sys.stderr.write("GOOD\n")
	if argv[10]:
		print "there is no 10"

if __name__ == '__main__':
	print sys.argv[1:]
        main(sys.argv[1:])

