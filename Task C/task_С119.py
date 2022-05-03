"""
Каждый класс реализовать в отдельном модуле, импортируя их в производные модули.
Создать класс Person с полями имя, фамилия, возраст. Добавить конструктор класса.
Создать производный от Person класс Client. Новые поля: номер билета, параметры тренировок
    (словарь вида параметр: значение). Определить конструктор, с вызовом родительского конструктора.
    Определить функции добавления параметра в журнал тренировок, получения значения по параметру,
    форматированной печати всех параметров. Переопределить метод преобразования в строку для печати
    основной информации (ФИ, возраст, номер билета).
Создать производный от Person класс Trainer. Новые поля: номер удостоверения, должность, расписание
    работы (словарь вида день : время). Определить конструктор, с вызовом родительского конструктора. Определить
    функции изменения, добавления и удаления в расписание. Переопределить метод преобразования
    в строку для печати основной информации (ФИ, возраст, номер удостоверения, должность).
Создать класс Gym. Поля: адрес, список клиентов (список экземпляров класса Client), список тренеров
    (список экземпляров класса Trainer). Определить конструктор. Переопределить метод преобразования в строку для печати
    всей информации о спортзале (с использованием переопределения в классах Client и Trainer). Переопределить
    методы получения количества тренеров функцией len, получения тренеров по индексу, изменения
    по индексу, удаления по индексу. Переопределить операции + и - для добавления или удаления клиента.
    Добавить функцию создания txt-файла и записи всей информации в него (в том числе расписаний тренеров и
    журналов тренировок клиентов).
Предусмотреть хотя бы в 3 местах обработку возможных исключений.
В каждом модуле провести подробное тестирование всех создаваемых объектов и функций.
"""


class Person:
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age   
class Client(Person):
    def __init__(self, name, surname, age, num_ticket):
        Person.__init__(self, name, surname, age)
        self.num_ticket = num_ticket
        self.tren = {}
    
    def __str__(self):
        s = "Surname: {} Name: {}\nage: {}, num_ticket: {}".format(self.surname, self.name, self.age, self.num_ticket)
        return s
 
            
class Trainer(Person):
    def __init__(self, name,surname, age,num_udost, doljnost):
        Person. __init__(self, name, surname, age)
        self.num_udost = num_udost
        self.doljnost = doljnost
        self.raspisanie = {}
    def __str__(self):
        st = "Surname: {} Name: {}\nage: {},num_udost: {}, doljnost: {}".format(self.surname,self.name,self.age,self.num_udost,self.doljnost) 
        return st
 
class Gym:
    def __init__(self,address,lst_clients,lst_trainers):
        self.address = address
        self.lst_clients = lst_clients
        self.lst_trainers = lst_trainers
        
client1 = Client("Elena","Drozdova","24","54625")
client2 = Client("Sergey","Vorozhtsov","15","53385")
client3 = Client("Olga","Malkova","46","59025")
client4 = Client("Timofey","Vorozhtsov","34","59005")
client5 = Client("Luda","Fokina","19","54095")
client6 = Client("Natalia","Kremleva","38","57845")
client7 = Client("Makar","Toropov","26","51105")
client8 = Client("Zhanna","Listunova","31","50074")
client9 = Client("Grigory","Skuratov","50","50001")
client10 = Client("Anatoly","Krivov","23","63758")
client11 = Client("Mikhail","Olkhovskiy","17","86753")
client12 = Client("Vyacheslav","Yatsenko ","22","90074")
client13 = Client("Maria","Korshunova","34","12834")
client14 = Client("George","Schultz","28","08462")
client15 = Client("Semen","Antinov ","21","27487")
trainer1 = Trainer("Nikolay","Kolesnik","45","66843","Trainer")
trainer2 = Trainer("Olga","Fedorova","34","29673","Fitness instructor")
trainer3 = Trainer("Yuli","Kovalenko","4236","42380","Fitness instructor")
trainer4 = Trainer("Elena","Kovalenko","36","42380","Fitness instructor")
trainer5 = Trainer("Artem","Baskakov","41","47132","Director")
trainer6 = Trainer("Timofey","Samoylov","34","93441","Trainer")
trainer7 = Trainer("Daniel","Yakunichev","27","93441","Trainer")
 
clients = [client1,client2,client3,client4,client5,client6,client7,client8,client9,client10,client11,client12,client13,client14,client15]
trainers = [trainer1,trainer2,trainer3,trainer4,trainer5,trainer6,trainer7]
