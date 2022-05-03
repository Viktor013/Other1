from Person import Person

class Trainer(Person):
    def __init__(self, name,surname, age,num_udost, doljnost):
        Person. __init__(self, name, surname, age)
        self.num_udost = num_udost
        self.doljnost = doljnost
        self.workhours = {}

#############   ДЛЯ СЛОВАРЯ  ##############
        
#        for i in range(1, 6):
#            self.whatdayisit = str(i)
#            self.day = self.whatdayisit
#            self.day += "-й рабочий день"
#            self.daywork = str(input("Введите время начала и конца рабочего дня:  "))
#            self.workhours[self.day] = self.daywork

#############   ДЛЯ СЛОВАРЯ  ##############


        
    def __str__(self):
        st = "Surname: {} Name: {}\nage: {},num_udost: {}, doljnost: {}".format(self.surname,self.name,self.age,self.num_udost,self.doljnost) 
        return st
