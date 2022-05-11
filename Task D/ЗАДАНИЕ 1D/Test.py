import pickle
import datetime
from Trainer import Trainer
from Gym import Gym
from Client import Client

f = open("logging.txt","w+")
logg = []
templogg = ""

client1 = Client("Elena","Drozdova","24","54625", f, logg)
client2 = Client("Sergey","Vorozhtsov","15","53385", f, logg)
client3 = Client("Olga","Malkova","46","59025", f, logg)
client4 = Client("Timofey","Vorozhtsov","34","59005", f, logg)
client5 = Client("Luda","Fokina","19","54095", f, logg)
client6 = Client("Natalia","Kremleva","38","57845", f, logg)
client7 = Client("Makar","Toropov","26","51105", f, logg)
client8 = Client("Zhanna","Listunova","31","50074", f, logg)
client9 = Client("Grigory","Skuratov","50","50001", f, logg)
client10 = Client("Anatoly","Krivov","23","63758", f, logg)
client11 = Client("Mikhail","Olkhovskiy","17","86753", f, logg)
client12 = Client("Vyacheslav","Yatsenko ","22","90074", f, logg)
client13 = Client("Maria","Korshunova","34","12834", f, logg)
client14 = Client("George","Schultz","28","08462", f, logg)
client15 = Client("Semen","Antinov ","21","27487", f, logg)
#trainer1 = Trainer("Nikolay","Kolesnik","45","66843","Trainer")
#trainer2 = Trainer("Olga","Fedorova","34","29673","Fitness instructor")
#trainer3 = Trainer("Yuli","Kovalenko","42","42380","Fitness instructor")
#trainer4 = Trainer("Elena","Kovalenko","36","42380","Fitness instructor")
#trainer5 = Trainer("Artem","Baskakov","41","47132","Director")
#trainer6 = Trainer("Timofey","Samoylov","34","93441","Trainer")
#trainer7 = Trainer("Daniel","Yakunichev","27","93441","Trainer")



clients = [client1,client2,client3,client4,client5,client6,client7,client8,client9,client10,client11,client12,client13,client14,client15]
#trainers = [trainer1,trainer2,trainer3,trainer4,trainer5,trainer6,trainer7]

for i in range(0, len(clients)):
    print(clients[i])



#################Добавление/Удаление клиектов##################

#NewCustomer = Gym.customer('+', clients)
#clients.append(NewCustomer)
#print(clients[15])

##print(len(clients))
##DeleteCustomer = Gym.customer('-', clients)
##clients.remove(DeleteCustomer)
##print(len(clients))


#################Проверка словаря упражнений клиентов / Получение определенного параметра#####################

#print(client1)
#print(client1.exercise)

#looking = str(input('Введите название параметр: '))
#for key, value in (client1.exercise).items():
#    if key == looking:
#        print("Параметр  ", key, "  имеет значение  ", value)
        

################Проверка словаря рабочего дня тренера / Получение расписания определенного дня###############

#print(trainer1)
#print(trainer1.workhours)

#looking = str(input('Расписание какого рабочего дня? : '))
#for key, value in (trainer1.workhours).items():
#    if key == looking:
#        print("Расписание на  ", key, "  ====  ", value)



###############Проверка  Gym   ######################
#
#BossOfThisGym = Gym("Улица Пушкина Дом Калатушкина",clients,trainers)
#index = int(input("Введите индекс тренера: "))#
####Изменение тренера####
#ChangeNow = Gym.changetrainer(trainers, index)
#trainers[index] = ChangeNow
#print(trainers[index])
####Удаление Тренера#####
#DeleteFuckingTrainer = Gym.deletetrainer(trainers, index)
#print(DeleteFuckingTrainer)
####Сколько тренеров####
#HowMany = Gym.trainers(trainers))
####Информация о тренере#####
#ThisTrainer = Gym.getrainer(trainers)

###############Запись информации в txt файл ##############

#print(client1.exercise)


#f = open("info.txt","w+")
#f.write("Clients: \n\n")
#for i in range(0, len(clients)):
#    f.write(str(clients[i]))
#    f.write("\n")
#    f.write(str(clients[i].exercise))
#    f.write("\n\n")

    
#f.write("\n\n Trainers: \n\n")
#for i in range(0, len(trainers)):
#    f.write(str(trainers[i]))
#    f.write("\n")
#    
#    f.write("\n\n")
#
#f.close()





###############################@    D      @######################

############## Логирование ##################

##(Метод в Clients)#
f.close
############ Изменение ключа логирования ############
#al = open("logging.txt","w+")
#logg[1] = Client.key_change()
#for i in range(0, len(logg)):
#    al.write(str(logg[i]))
#    al.write("\n")
#al.close()

########### Сериализация #################
al = open("binary.txt","wb")
for i in range(0,len(logg)):
    pickle.dump(str(logg[i]), al)
    pickle.dump("\n", al)
al.close()

########### Десериализация ##############

with open("binary.txt", "rb") as file:
        try:
            while True:
                print(pickle.load(file))
        except EOFError:
            pass











