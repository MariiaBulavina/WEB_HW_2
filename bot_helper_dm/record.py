from datetime import datetime

from address import Address
from birthday import Birthday
from email_address import Email
from name import Name
from phone import Phone


class Record:
    def __init__(self, name, phone=None):
        
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.address = None
        self.emails = []

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def days_to_birthday(self):

        birthday = self.birthday.value
        today = datetime.now().date()
        current_year_birthday = birthday.replace(year=today.year)

        if current_year_birthday < today:
            current_year_birthday = current_year_birthday.replace(year=current_year_birthday.year+1)

        days_until_birthday = current_year_birthday - today
        return days_until_birthday.days

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):

        for p in self.phones:

            if str(p.value) == phone:
                index = self.phones.index(p)
                self.phones.pop(index)
                return f'Contact number {self.name} {phone} has been deleted'
            
        return f'Contact {self.name} does not have a number {phone}'

    def edit_phone(self, old_phone, new_phone):

        for p in self.phones:

            if str(p.value) == old_phone:
                index = self.phones.index(p)
                self.phones[index] = Phone(new_phone)
                return f'Contact number {self.name.value} {old_phone} has been changed to: {new_phone}' 
            
        raise ValueError

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
            
    def add_address(self, address):
        self.address = Address(address)

    def edit_address_by_key(self, key, new_information):

        if key == 'country':
            self.address.country = new_information
        elif key == 'city':
            self.address.city = new_information    
        elif key == 'street':
            self.address.street = new_information    
        elif key == 'house':
            self.address.house = new_information    
        elif key == 'apartment':
            self.address.apartment = new_information

        return f'{self.name.value}\'s {key} has been changed to {new_information}'

    def delete_address(self):
        self.address = None
        
    def add_email(self, email):
        self.emails.append(Email(email))        

    def edit_email(self, old_email, new_email):

        for em in self.emails:
            if str(em.value) == old_email:
                index = self.emails.index(em)
                self.emails[index] = Email(new_email)
                return f'{self.name.value}\'s email {old_email} has been changed to: {new_email}' 
            
        raise ValueError    
    
    def remove_email(self, email):

        for em in self.emails:

            if str(em.value) == email:
                index = self.emails.index(em)
                self.emails.pop(index)
                return f'{self.name}\'s email {email} has been deleted'
            
        return f'Contact {self.name} does not have an email {email}'

    def __str__(self):
        return f"Contact name: {self.name.value},"\
                f"phones: {'; '.join([str(p.value) for p in self.phones])}, "\
                f"birthday: {self.birthday}, "\
                f"address: {self.address}, "\
                f"emails: {'; '.join([str(em.value) for em in self.emails])}"

    def __repr__(self) -> str:
        return f"Contact name: {self.name.value}, "\
                f"phones: {'; '.join([str(p.value) for p in self.phones])}, "\
                f"birthday: {self.birthday}, "\
                f"address: {self.address}, "\
                f"emails: {'; '.join([str(em.value) for em in self.emails])}"


