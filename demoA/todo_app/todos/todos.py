from datetime import date


class ToDo:
    __count=0

    def __init__(self, *args,**kwargs):
        self.__count += 1        
        for key,value in kwargs.items():
            if key == "priority":
                self.__priority == value
            else:
                self.__priority = self.__count
        self.__date = args[0]
        self._note = ""
        

    # @property
    # def count(self):
    #     return self.__count

    @property
    def date(self):
        return self.__date

    @property
    def note(self):
        return self._note

    @note.setter
    def note(self, content):
        self._note = content

    @property
    def priority(self):
        return self.__priority

    def search_note(self, date):
        if date == self.date:
            return self.note

    def __str__(self) -> str:
        return f"\n{self.date.strftime('%Y-%m-%d')} | {self.note}\n"

    def __repr__(self):
        return {"date":self.date.strftime('%Y-%m-%d'),
                "priority":self.priority,
                "note":self.note}