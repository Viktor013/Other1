from Person import Person

class Client(Person):
    def __init__(self, name, surname, age, num_ticket):
        Person.__init__(self, name, surname, age)
        self.num_ticket = num_ticket

#############   ДЛЯ СЛОВАРЯ  ##############
#
        self.exercise = {}
        self.loop = int(input("Введите количество параметров тренировок: "))
        for i in range(0, self.loop):
            self.typeof = input("Введите вид параметра тренировки: ")
            self.value = input("Введите значение параметра: ")
            self.exercise[self.typeof] = self.value
#
#############   ДЛЯ СЛОВАРЯ  ##############


    def __str__(self):
        
        s = "Surname: {}   Name: {}\nage: {},   num_ticket: {}".format(self.surname, self.name, self.age, self.num_ticket)
        return s

