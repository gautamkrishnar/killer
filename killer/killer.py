import sys
import time
import subprocess
def main():
	print("""
	**********************************************************************
	             Scheduler by Gautam krishna R
	***********************************************************************
	
	""")
	if len(sys.argv) <3 or len(sys.argv)>3:
		print("Error in args... Syntax: killer <min> <app>")
		exit(0)
	wait=int(sys.argv[1])
	app=sys.argv[2]
	print("Waiting "+str(wait)+ " Minute(s) to close "+str(app)+"...")
	time.sleep(wait*60)
	subprocess.call("TASKKILL /F /IM "+str(app)+" /T")
	exit(0)
if __name__ == '__main__':
	main()