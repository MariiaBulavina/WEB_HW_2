import re

from prompt_toolkit import prompt

from prmt import get_completer
from phone import PhoneError
from record import Record
from addressbook import AddressBook
from birthday import BirthdayError
from note import Note
from notebook import NoteBook
from user_intaraction import ContactTable, NoteTable, HelpTable

book = AddressBook()
notes = NoteBook()

def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return 'Not enough params'
        except KeyError:
            return 'You have no contacts with this name'
        except ValueError:
            return 'You entered incorrect data'
        except BirthdayError:
            return 'You can\'t add a date in this format'
        except PhoneError:
            return 'Phone number must be 10 digits long'
    return inner


def hello(*args):
    return 'How can I help you?'


@input_error
def add_contact(*args):

    name = args[0]

    if name in book:
            return f'A contact with the name {name} already exists'
    else:
        book[name] = Record(name)
        try:
            phone = args[1]
            book[name].add_phone(phone)
            return f'A contact with the name {name} and number: {phone} has been added'
        except IndexError:
            return f'A contact with the name {name} has been added'


@input_error
def add_phone(*args):

    name = args[0]

    if name in book:
        phone = args[1]
        book[name].add_phone(phone)
        return f'Number {phone} has been added for contact {name}'
    else:
        return 'You have no contacts with this name'



@input_error
def change_phone(*args):
    name = args[0]
    old_phone = args[1]
    new_phone = args[2]
    record = book.get(name)

    if record:
        message = record.edit_phone(old_phone, new_phone)
        return message
    else:
        raise KeyError


@input_error
def phone(*args):
    name = args[0]
    record = book.get(name)

    if record:
        return record.phones
    else:
        return 'You have no contacts with this name'


@input_error
def delete_contact(*args):
    name = args[0]
    book.delete(name)
    return f'Сontact with the name {name} has been deleted'



@input_error
def remove_phone(*args):
    name = args[0]
    phone = args[1]
    record = book.get(name)

    if record:
        message = record.remove_phone(phone)
        return message
    else:
        return 'You have no contacts with this name'
    

@input_error
def add_birthday(*args):

    name = args[0]

    if name in book:
        birthday = args[1]
        book[name].add_birthday(birthday)
        return f'A birthday {birthday} has been added to the entry for the name {name}' 
    else:
        return 'Enter a contact name to add a birthday'

@input_error
def days_to_birthday(*args):
    name = args[0]
    record = book.get(name)

    try:
        days_until_birthday = record.days_to_birthday() 
        return f'{days_until_birthday} days until {name}\'s birthday'
    except AttributeError:
        return f'There is no birthday entry in the contact with the name {name}'

@input_error
def find_contact(*args):

    data = args[0]
    search_matches = []

    for _, contact in book.data.items():
        changed_contact = str(contact).replace('Contact name:', '').replace('phones:', '').replace('birthday:', '').replace('address:', '').replace('emails:', '').replace('None', '')
        result = re.findall(data, str(changed_contact))
        if result:
            search_matches.append(contact)
    contact_table = ContactTable()
    return contact_table.create_table(search_matches)

@input_error
def find_note(*args):

    data = args[0]
    search_matches = []

    for _, note in notes.data.items():
        changed_note = str(note).replace('tegs:', '')
        result = re.findall(data, changed_note)

        if result:
            search_matches.append(note)
    note_table = NoteTable()
    return note_table.create_table(search_matches)


@input_error
def delete_note(*args):
    title = args[0]
    message = notes.delete_note(title)
    return message



@input_error
def add_email(*args):

    name = args[0]

    if name in book:
        email = args[1]
        book[name].add_email(email)
        return f'Email {email} has been added for contact {name}'
    else:
        return 'You have no contacts with this name'
    

@input_error
def change_email(*args):
    name = args[0]
    old_email = args[1]
    new_email = args[2]
    record = book.get(name)

    if record:
        message = record.edit_email(old_email, new_email)
        return message
    else:
        raise KeyError
    

@input_error
def remove_email(*args):

    name = args[0]
    email = args[1]
    record = book.get(name)

    if record:
        message = record.remove_email(email)
        return message
    else:
        return 'You have no contacts with this name'


@input_error
def add_address(*args):

    name = args[0]

    if name in book:
        address_str = ' '.join(list(args[1:]))
        address = address_str.split(', ')

        book[name].add_address(address)
        return f'Address {address} has been added for contact {name}'
    else:
        return 'You have no contacts with this name'
    
@input_error
def change_address_by_key(*args):
    
    name = args[0]
    key = args[1]
    new_information = args[2]

    record = book.get(name)

    if record:
        message = record.edit_address_by_key(key, new_information)
        return message
    else:
        return 'You have no contacts with this name'


@input_error
def delete_address(*args):

    name = args[0]

    if name in book:
        book[name].delete_address()
        return f'{name}\'s address has been deleted'




@input_error
def add_note(*args):

    title = input('Enter a title for your note: ')
    text = input('Enter the text of your note: ')


    if title in notes:
        exist_question = input(f'Note with title {title} already exist. Do you want to add this text to an existing note? y/n')
        if exist_question == 'y':
            notes[title].add_text(text)
            return f'A text {text} has been added to the note with the title {title}]'

        elif exist_question == 'n':
            return 'Then you need to create a note with a different title' 
    else:
        notes[title] = Note(title, text)

        teg_question = input('Do you want to add tegs? y/n ')
        if teg_question == 'y':
            tegs = input('Enter tags in the format: #teg #teg1: ')
            notes[title].add_tegs(tegs)

        return f'Note \'{title}: {text}\' was created'

@input_error
def add_tegs(*args):

    title = args[0]

    if title in notes:
        tegs = ''
        for t in args[1:]:
            tegs += ' ' + t
        notes[title].add_tegs(tegs.strip())
        return f'Tegs {tegs} were added to the note with the title {title}'
    else:
        return 'You don\'t have any notes with this title'


@input_error
def change_note(*args):
    
    title = args[0]
    if title in notes:
        new_text = args[1]
        notes[title].change_note(new_text)
        return f'Note with title {title} has been changed'
    else:
        return 'You don\'t have any notes with this title'
    

@input_error
def remove_teg(*args):
    
    title = args[0]
    if title in notes:
        teg = args[1]
        notes[title]
        notes[title].remove_teg(teg)
        return f'The {teg} tag for the note with the title {title} has been removed'
    else:
        return 'You don\'t have any notes with this title'

@input_error
def show_all_notes(*args):
    table = notes.create_table()
    return table

@input_error
def show_all_contacts(*args):
    table = book.create_table()
    return table


@input_error
def upcoming_birthdays(*args):
    
    result = ''
    period = int(args[0])
    birthdays = book.upcoming_birthdays(period)
    for line in birthdays:
        result += line + '\n'
    return result.strip()    

    
def close(*args):
    return 'Good bye!'


def no_command(*args):
    return 'Unknown command'


def help(*args):
    helptable = HelpTable()
    return helptable.create_table()

     

COMMANDS = {
    help: ['help'],
    hello: ['hello'],
    close: ['good bye', 'close', 'exit', '.'],

    add_contact: ['add contact'],
    show_all_contacts: ['show all contacts'],
    delete_contact: ['delete contact'],
    find_contact: ['find contact'],

    add_phone: ['add phone'],
    change_phone: ['change phone'],
    phone: ['phone'],
    remove_phone: ['remove phone'],

    add_birthday: ['add birthday'],
    days_to_birthday: ['days to birthday'],
    upcoming_birthdays: ['upcoming birthdays'],

    add_email: ['add email'],
    change_email: ['change email'],
    remove_email: ['remove email'],

    add_address: ['add address'],
    change_address_by_key: ['change address'],
    delete_address: ['delete address'],

    add_note: ['add note'],
    add_tegs: ['add tegs'],
    show_all_notes: ['show all notes'],
    find_note: ['find note'],
    delete_note: ['delete note'],
    change_note: ['change note'],
    remove_teg: ['remove teg']


}


@input_error
def get_handler(user_input: str):

    for func, k_words in COMMANDS.items():
        for word in k_words:
            if user_input.lower().startswith(word):

                return func, user_input[len(word):].strip().split()
    return no_command, []



def main():

    book.load('contacts.bin')
    notes.load('notes.bin')
  
    while True:

        user_input = prompt(message=">>> ",
                           completer=get_completer(),
                           bottom_toolbar='enter \'help\' to get information about bot commands')
        
        function, data = get_handler(user_input)

        print(function(*data))

        if function.__name__ == 'close':
            book.save('contacts.bin')
            notes.save('notes.bin')
            break



if __name__ == '__main__':
    main()