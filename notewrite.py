with open('notes.txt','r') as file:
	notes = file.read().split('\n')

with open('notes.txt','w') as file:
	new_note = input('New entry: ')
	if (new_note != ''):
		file.writelines([note + '\n' for note in notes])
		file.writelines(list(new_note))
		print('Saved!')
	else:
		print('No content!')