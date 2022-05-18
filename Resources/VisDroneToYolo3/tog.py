import sys
from pathlib import Path

def main():
	if len(sys.argv)!=4:
		print('Error: Arg')
		return
	out = open(sys.argv[3],'w')
	ffile = Path(sys.argv[1]).read_text()
	sfile = Path(sys.argv[2]).read_text()
	out.write(ffile+sfile)
	out.close()

if __name__ == "__main__":
	main()