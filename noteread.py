def delete(terminal_index):
	with open('notes.txt','r') as file:
		notes = file.read().split("\n")
		for note in notes:
			if note == '':
				notes.remove(note)
		try:
			notes.pop(int(terminal_index) - 1)
		except:
			print("Invalid index!")
			return
	with open('notes.txt', 'w') as file:
		for note in notes:
			if (note != ''):
				file.write(note + "\n")
		print('Deleted number {}!'.format(terminal_index))

def print_notes():
	with open('notes.txt','r') as file:
		notes = file.read().split("\n")
		print("Your notes:\n-------------")
		for note in notes:
			if(note != ''):
				print(note)
		print('-------------')

def clear():
	with open('notes.txt','w') as file:
		print('Cleared all notes!')


# Main portion
print_notes()
input_str = input('Choose an action: ')
while input_str != 'exit':
	if ('delete' in input_str):
		del_index = input_str.replace('delete', '')
		del_index = del_index.replace(' ', '')
		delete(del_index)
	if ('print' in input_str):
		print_notes()
	if ('clear') in input_str:
		clear()
	input_str = input('Choose an action: ')
