from abc import ABC, abstractmethod

from tabulate import tabulate


class Table(ABC):
    @abstractmethod
    def create_table(self):
        ...


class AddressbookTable(Table):

    def create_table(self):
        data = [
        ['name', 'phones', 'birthday', 'emails', 'address']
    ]
        for contact in self.data.values():
            line = [contact.name,  '; '.join([str(p.value) for p in contact.phones]), contact.birthday, '; '.join([str(em.value) for em in contact.emails]), contact.address]
            data.append(line)

        result = tabulate(data,headers='firstrow',tablefmt='fancy_grid')
        return result


class NotebookTable(Table):

    def create_table(self):
        data = [
        ['title', 'text', 'tags']
    ]

        for note in self.data.values():
            line = [note.title, note.text, "; ".join([str(tag) for tag in note.tags])]
            data.append(line)

        result = tabulate(data,headers='firstrow',tablefmt='fancy_grid')
        return result
    

class ContactTable(Table):

    def create_table(self, contacts):
        data = [
        ['name', 'phones', 'birthday', 'emails', 'address']
    ]
        
        for contact in contacts:
            line = [contact.name, '; '.join([str(p.value) for p in contact.phones]), contact.birthday, '; '.join([str(em.value) for em in contact.emails]), contact.address]
            data.append(line)

        result = tabulate(data,headers='firstrow',tablefmt='fancy_grid')
        return result
    

class NoteTable(Table):

    def create_table(self, notes):
        data = [
        ['title', 'text', 'tags']
    ]
        
        for note in notes:
            line = [note.title, note.text, "; ".join([str(tag) for tag in note.tags])]
            data.append(line)

        result = tabulate(data,headers='firstrow',tablefmt='fancy_grid')
        return result
    

class HelpTable(Table):

    def create_table(self):
        data = [['FUNCTIONS', 'DESCRIPTION'],
                ['hello', 'greeting'],
                ['good bye or close or exit or .' ,'finish the bot\'s work'],

                ['add contact <name> or <name> <phone>', 'to add a contact'],
                ['delete contact <name>', 'to delete a contact'],
                ['find contact <character sequence>', 'to find a contact based on matches with letters or numbers'],
                ['show all contacts', 'to see the entire phone book'],

                ['add phone <name> <phone>', 'to add a phone number'],
                ['change phone <name> <old phone> <new phone>', 'to change a phone number'],
                ['phone <name>', 'to view a contact\'s phone number'],
                ['remove phone <name> <phone>', 'to remove a phone number'],

                ['add birthday <name> <dd-mm-yyyy>', 'to add a birthday entry'],
                ['days to birthday <name>', 'to get the number of days until contact\'s next birthday'],
                ['upcoming birthdays <time range in days>', 'to see all birthdays within a time period'],

                ['add email <name> <email>', 'to add an email addresss'],
                ['change email <name> <old email> <new email>', 'to change an email addresss'],
                ['remove email <name> <email>', 'to remove an email addresss'],

                ['add address <name> <country>, <city>, <street>, <house>, <apartment>', 'to add an address'],
                ['change address name/country/city/street/house/apartment <information>', 'to change an address'],
                ['delete address <name>', 'to delete an address'],

                ['add note', 'to add a note'],
                ['find note <character sequence>', 'to find a note based on matches with letters or numbers'],
                ['delete note <title>', 'to delete a note'],
                ['change note <title> <text>', 'to change a note'],
                ['show all notes', 'to see the entire notebook'],

                ['add tags <title> <#tag>', 'to add a tag'],
                ['remove tag <title> <#tag>', 'to remove a tag']]

        result = tabulate(data,headers='firstrow',tablefmt='fancy_grid')
        return result    