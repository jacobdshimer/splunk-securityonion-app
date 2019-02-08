import os
import fileinput

path = 'default/data/ui/views'
files = os.listdir(path)

def main():
	print("Is this the initial setup? [Y]/N")
	answer = input("> ") or "Y"
	if answer == "Y":
		print("What is the IP address of your security onion master?")
		ipaddr = input("> ")
		for file in files:
			for line in fileinput.input(path+'/'+file, inplace=True):
				line = line.rstrip('\r\n')
				print(line.replace('[INSERT SEC ONION IP ADDRESS]',ipaddr))
	else:
		print("What do you need to change?")
		first = input("> ")
		print("What do you want to change it to?")
		second = input("> ")
		for file in files:
			for line in fileinput.input(path+'/'+file, inplace=True):
				line = line.rstrip('\r\n')
				print(line.replace(first,second))

if __name__ == "__main__":
	main()