import random
import json
from datetime import datetime

class Note:
	def __init__ (self, id, header, body, date):
		self.id = id
		self.header = header
		self.body = body
		self.date = date
		
def save_notes(notes):
	with open('notes.txt', 'w', encoding='utf-8') as file:
		json.dump([note.__dict__ for note in notes], file, indent=4, separators=(',', ': '))

def read_notes():
	try:
		with open('notes.txt', 'r') as file:
			data = json.load(file)
			notes = [Note(**note) for note in data]
	except (json.decoder.JSONDecodeError, FileNotFoundError):
		notes = []
	return notes

def idAdd():
	idNew = random.randint(1, 100)
	idArr = []
	for note in notes:
		idArr.append(note.id)
	while True:
		if idNew in idArr:
			idNew = random.randint(1, 100)
		else:
			break
	return idNew

def add_note():
	header = input('Введите заголовок: ')
	body = input('Введите заметку: ')
	date = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
	id = idAdd()
	note = Note(id, header, body, date)
	notes.append(note)
	save_notes(notes)
	print('Заметка сохранена.')
	
def edit_note():
	id = int(input('Введите индификатор: '))
	note = next ((note for note in notes if note.id == id), None)
	if note:
		print(f'Редоктирование заметки: { note.header}')
		header = input('Введите новый заголовок или оставьте пустым,чтобы не менять: ')
		body = input('Введите новый текст заметки или оставьте пустым: ')
		date = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
		note.date = date
		if header:
			note.header = header
		if body:
			note.body = body
		save_notes(notes)
		print('Изменения сохранены.')
	else:
		print('Заметка не найдена')
			
def delete_note():
	id = int(input('Введите индефикатор заметки для удаления: '))
	note = next ((note for note in notes if note.id == id), None)
	if note:
		notes.remove(note)
		save_notes(notes)
		print('Заметка удалена')
	else:
		print('Заметка не найдена')

def view_notes():
	date_str = input("введите дату для фильтра: ")
	try:
		filter_date = datetime.strptime(date_str, '%d.%m.%Y')
		filtered_notes = [note for note in notes if datetime.strptime(note.date, '%d.%m.%Y %H:%M:%S').date() == filter_date.date()]
	except ValueError:
		filtered_notes = notes
	if filtered_notes:
		for note in filtered_notes:
			print(f'{note.id} {note.header} ({note.date}):\n {note.body}')
	else:
		print('нет заметок')
		
def main():
	global notes
	notes = read_notes()
	while True:
		print(' 1 - Показать все заметки\n 2 - Добавить заметку\n 3 - Редактировать заметку\n 4 - Удалить заметку\n 5 - Выход\n')
		choice = input('Выберите действие: ')
		if choice == '1':
			view_notes()
		elif choice == '2':
			add_note()
		elif choice == '3':
			edit_note()
		elif choice == '4':
			delete_note()
		elif choice == '5':
			break
		else:
			print('ошибка')
main()
