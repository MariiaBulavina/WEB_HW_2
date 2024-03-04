from collections import UserDict

from save_load import SaverLoader
from user_interaction import AddressbookTable


class AddressBook(UserDict, SaverLoader, AddressbookTable):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
            self.data.pop(name)
   
    def upcoming_birthdays(self, period):

        result = []

        for user in self.data.values():
            if user and user.birthday:
                if 0 <= user.days_to_birthday() <= period:
                    result.append(f'Name: {user.name.value}, days to birthday: {user.days_to_birthday()}')

        return result
