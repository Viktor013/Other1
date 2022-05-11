import pickle
import datetime
from Person import Person

class Client(Person):
    def __init__(self, name, surname, age, num_ticket, f, logg):
        try:

            Person.__init__(self, name, surname, age)
            self.num_ticket = num_ticket
            self.log_time = datetime.datetime.now()
            comment = str(input("Введите комментарий для логирования: "))
            templogg = ""
            templogg += "CRE --- "
            templogg += str(self.log_time)
            templogg += " --- "
            templogg += str(comment)
            logg.append(templogg)
            f.write(str(templogg))
            f.write("\n\n")
        except ValueError:
            comment = str(input("Введите комментарий для логирования: "))
            templogg = ""
            templogg += "ERR --- "
            templogg += str(self.log_time)
            templogg += " --- "
            templogg += str(comment)
            logg.append(templogg)
            f.write(str(templogg))
            f.write("\n\n")
            
#############   ДЛЯ СЛОВАРЯ  ##############
#
#        self.exercise = {}
#        self.loop = int(input("Введите количество параметров тренировок: "))
#        for i in range(0, self.loop):
#            self.typeof = input("Введите вид параметра тренировки: ")
#            self.value = input("Введите значение параметра: ")
#            self.exercise[self.typeof] = self.value
#
#############   ДЛЯ СЛОВАРЯ  ##############


    def __str__(self):
        
        s = "Surname: {}   Name: {}\nage: {},   num_ticket: {}".format(self.surname, self.name, self.age, self.num_ticket)
        return s


    def key_change():
        log_time = datetime.datetime.now()
        templogg = ""
        comment = str(input("Введите комментарий для логирования: "))
        templogg = ""
        templogg += "INF --- "
        templogg += str(log_time)
        templogg += " --- "
        templogg += str(comment)
        return templogg
        

