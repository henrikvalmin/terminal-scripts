import sqlite3

def print_notes(connection):
	c = connection.cursor()
	#c.execute("INSERT INTO notes VALUES ('hello')")
	#connection.commit()
	notes = c.execute('SELECT * from notes')
	print("Your notes:\n-------------")
	for i, row in enumerate(notes):
		if i == 0:
			print(row[0], '. ', row[1], sep='')
		else:
			print('\n', row[0], '. ', row[1], sep='')
	print('-------------')

def present_choices():
	print("Choices:")
	print("'del index' to remove note at index\n'clearall' to remove all notes',\n'exit' to exit")
	return input('')

def main():

	# handle table not existing

	connection = sqlite3.connect('noteDB.db')
	c = connection.cursor()
	print_notes(connection)

	response = ''
	while response != 'exit':
		response = present_choices()
		
		if response.strip() == 'clearall':
			c.execute("DELETE FROM notes")
			connection.commit
			print("Cleared everything!")
			response = 'exit'
		
		elif 'del' in response:
			index = response.split(' ')[1]
			c.execute("DELETE FROM notes WHERE id={}".format(index))
			connection.commit()
			print_notes(connection)

		elif response.strip() != 'exit':
			print('Invalid choice, pick again:')


if __name__ == "__main__":
	main()
