from Client import Client

class Gym:
    def __init__(self,address,clientlist,trainerlist):
        self.address = address
        self.clientlist = clientlist
        self.trainerlist = trainerlist

    def customer(char, clientlist):
        if char == '+':
            newclientName = str(input("Введите имя нового клиента:"))
            newclientSur = str(input("Введите фамилию нового клиента:"))
            newclientAge = str(input("Введите возраст нового клиента:"))
            newclientNumTicket = str(input("Введите номер билета нового клиента:"))
            newclient = Client(newclientName, newclientSur, newclientAge, newclientNumTicket)
            return(newclient)
        if char == '-':
            index = input("Введите номер билета клиента ")
            for i in range(0, len(clientlist)):
                if index == clientlist[i].num_ticket:
                    return(clientlist[i])
            
    def trainers(trainerlist):
        print("Всего в этом здании находятся ", len(trainerlist), " Тренеров")
        
            
    def getrainer(trainerlist):
        index = int(input("Введите индекс тренера: "))
        print("Информация а данном тренере:   ", trainerlist[index])

    def changetrainer(trainerlist, index):
        name = str(input("Измените имя тренера: "))
        surname = str(input("Измените фамилию тренера: "))
        age = int(input("Измените возвраст тренера: "))
        num_udost = int(input("Измените номер удостоверения: "))
        doljnost = str(input("Измените должность тренера: "))
        st = "Surname: {} Name: {}\nage: {},num_udost: {}, doljnost: {}".format(surname,name,age,num_udost,doljnost)
        trainerlist[index] = st
        print(trainerlist[index])
        return(trainerlist[index])
    def deletetrainer(trainerlist, index):
        del trainerlist[index]
        for i in range(0, len(trainerlist)):
            print(trainerlist[i])
