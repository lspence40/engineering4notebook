# man shaped pinata
# euphemism for hangman

def printList(list): #prints a list as though it were s string
	for i in list:
		print(i, end = '')
	print()


def pinata(progress): #prints the pinata

	progress = int(progress) #convert string to int

	ans = '' #empty string
	
	if progress >= 0:
		ans += '---?\n'
	if progress >= 1:
		ans += '   o\n'
	if progress >= 2:
		ans += '  /'
	if progress >= 3:
		ans += '|' #add stuff to the empty string
	if progress >= 4:
		ans += '\\\n'
	if progress >= 5:
		ans += '   |\n'
	if progress >= 6:
		ans += '  /'
	if progress >= 7:
		ans += ' \\'

	return ans #all done


print('player 1, give me a word')
target = input() #get word

guesses = 0 #initialization
temp = ''
length = len(target)

print('\n' * 50) #clear screen

status = []
for i in range(length):
	status.append('-') #make an empty word

printList(status) #show the number of letters

while True: #repeat until don't

	print('player 2, guess a letter')
	temp = input() #get letter
	
	while not len(temp) == 1:
		print('that\'s multiple letters')
		temp = input()
	
	correct = False
	for i in range(length):
		if temp == target[i]: #is player 2 right?
			correct = True
			status[i] = temp
	
	if not correct:
		guesses += 1 #limited tries
	
	print(pinata(guesses)) #show progress
	printList(status)
	
	if guesses == length:
		print('player 1 wins') #game over
		break

	if not '-' in status:
		print('player 2 wins') #game over
		break
