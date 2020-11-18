print("give me a sentence")
sentence = input()
words = sentence.split(" ")

for i in range(len(words)):
	
	for j in range(len(words[i])):
		print(words[i][j:j+1])
	
	if i != len(words) - 1:
		print("-")
