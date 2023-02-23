from collections import UserDict
from datetime import datetime,  timedelta
import re



class Field:
    def __init__(self, value):
        self._value = None
        self.value = value

    
class Name(Field):

    def __repr__(self) -> str:
        return self.value
    
    def __call__(self) -> str:
        return self.value
    
    def __str__(self) -> str:
        return self.value
    
class Birthday(Field):
    @property
    def value(self, value):
        return self._value
    
    @value.setter
    def value(self, value):
        value = re.findall(r"\d{4}\.\d{2}\.\d{2}", value)
        if value:
            self._value = value
        else:
            self._value = None

    def __repr__(self) -> str:
        return self.value
    
    def __call__(self) -> str:
        return self.value
    
    def __str__(self) -> str:
        return self.value
    
class Phone(Field):
    @property
    def value(self, value):
        return self._value
    
    @value.setter
    def value(self, value):
        value = re.sub(r"[\-\(\)\+ ]", "", value)

        if len(value) == 12:
            value = "+" + value
        elif len(value) == 10:
            value = "+38" + value
        elif len(value) == 9:
            value = "+380" + value
        else:
            value = None
        self._value = value
    

    def __repr__(self) -> str:
        return self.value
    
    def __call__(self) -> str:
        return self.value
    
    def __str__(self) -> str:
        return self.value


class Record:
    def __init__(self, name: Name, phone: Phone = None, birthday : Birthday = None) -> None:
        self.name  = name
        self.phones = []
        self.birthday = birthday

        if phone:
            self.phones.append(phone)
            
    def add_phone(self, phone: Phone):
        self.phones.append(phone) 
        
    
    def remove_phone(self, phone: Phone):
        for p in self.phones:
            if p == phone.value:
                self.phones.remove(p)
    

    def change_phone(self, old_phone: Phone, new_phone: Phone):
        for phone in self.phones:
            if old_phone.value == phone.value:
                self.phones.remove(phone)
                self.phones.append(new_phone)

    def days_to_birthday(self, birthday: Birthday = None):
        current = datetime.now().date()
        user_date = datetime.strptime(birthday._value,"%Y.%m.%d")
        user_date = user_date.replace(year= current.year).date()

        if user_date < current:
            user_date = user_date.replace(year= current.year +1)
            res = user_date - current
            return f"{res.days} days before birthday"
        else:
            res = user_date - current
            return f"{res.days} days before birthday"



    def __repr__(self) -> str:
        return f"Numbers {self.phones}"
    def __call__(self) -> str:
        return f"Numbers {self.phones}"
    def __str__(self) -> str:
        return f"Numbers {self.phones}"
        
        
class AdressBook(UserDict):
    def dict_info(self, word):
        return word 
    
    def add_record(self, rec : Record):
        self.data[rec.name.value] = rec

    def iterator(self):
        for name, phone in self.data.items():
            yield f"{name} has phone {phone}"

    
        
















if __name__ == '__main__':
    
    name = Name('Bill')
    phone = Phone('0993790525')
    # birth = Birthday("2001.01.22")
    name1 = Name('Bill2')
    phone1 = Phone('09937905324')
    rec = Record(name, phone)
    rec1 = Record(name1, phone1)
    ab = AdressBook()
    ab.add_record(rec)
    ab.add_record(rec1)

    print(ab.iterator())

 
