import re
from collections import UserDict
from datetime import datetime

from colorit import *


class Error(Exception):  #власне виключення
     pass
    #  def __str__(self) -> str:
    #       return "\n \nSomething went wrong\n Try again!\n"



class Field:
    
    def __init__(self, value) -> None:
        self._value = value

    def __str__(self) -> str:
        return self._value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = value


class Name(Field):   #клас длч створення поля name

    def __str__(self) -> str:
        self._value : str
        return self._value.title()
    

class Phone(Field):   #клас для створення поля phone
    
    @staticmethod   #метод який не звязаний з класом
    def verify(number):  #перевирка номеру телефона
        number = re.sub(r"[\-\(\)\+\ a-zA-Zа-яА-я]", "", number)
        try:
            if len(number) == 12:
                number = "+" + number
            elif len(number) == 10:
                number = "+38" + number
            elif len(number) == 9:
                number = "+380" + number
            else:
                number = False
                raise Error
        except Error:
            print(color("\nSomething went wrong\n Try again!\n", Colors.green))
        
        if number:
            return number
        else:
            return ""


    def __init__(self, value) -> None:
        self._value = Phone.verify(value)

    @Field.value.setter
    def value(self, value):
        self._value =Phone.verify(value)


class Birthday:

    @staticmethod   #метод який не звязаний з класом
    def verify_date(birth_date: str):
        try:
            birthdate = re.findall(r"\d{4}\.\d{2}\.\d{2}", birth_date)
            if bool(birthdate) == False:
                raise Error
        except Error:
            print(color("\nYou enter wrong date.\nUse this format - YYYY.MM.DD \nTry again!\n", Colors.purple))

        if birthdate:
            return birthdate[0]
        else:
            return ""

    def __init__(self, birthday) -> None:
        self.__birthday = self.verify_date(birthday)

    @property
    def birthday(self):
        return self.__birthday
    
    @birthday.setter
    def birthday(self,birthday):
        self.__birthday = self.verify_date(birthday)

    def __repr__(self) -> str:
        return self.__birthday
    
    def __str__(self) -> str:
        return self.__birthday



class Record:   #клас для запису инфи
    def __init__ (self, name : Name, phone: Phone = None, birthday: Birthday = None):
        self.name = name
        self.phone = phone
        self.birthday = birthday
        self.phones = []
        if phone:
            self.phones.append(phone)

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def remove_phone(self, phone):
        phone = Phone(phone)
        for ph in self.phones:
            if ph == phone:
                self.phones.remove(ph)

    def change_phone(self, oldphone, newphone):
        oldphone = Phone(oldphone)
        newphone = Phone(newphone)

        for ph in self.phones:
            if ph == oldphone:
                self.phones.remove(oldphone)
                self.phones.append(newphone)

    def days_to_birthday(self):

        try:
                
            if str(self.birthday) == None:
                return None
            
            current = datetime.now().date()
            current : datetime
            user_date = datetime.strptime(str(self.birthday), "%Y.%m.%d")
            user_date: datetime
            user_date = user_date.replace(year=current.year).date()

            if user_date < current:
                user_date = user_date.replace(year= current.year +1)
                res = user_date - current

                return color(f"{res.days} days before next birthday", Colors.purple)
            else:
                res = user_date - current
                return color(f"{res.days} days before next birthday", Colors.purple)
        except ValueError:
            print(color("You set wrong date. Try again set new date in format YYYY.MM.DD", Colors.red))
            return ""

        

    

class AdressBook(UserDict): #адресна книга

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def generator(self):
        for name, info in self.data:
            yield color(f"{name} has phone {info}",Colors.green)

    
    def iterator(self, value):
        value = value
        gen = self.generator()
        while value > 0:
            print(next(gen))
            value -= 1
            









name = Name("Dima")
phone = Phone("0993796625")
birth = Birthday("2001.08.11")
rec = Record(name, phone, birth)

print(rec.days_to_birthday())
