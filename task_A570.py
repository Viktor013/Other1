# Создать список (супермаркет), состоящий из словарей (товары). Словари должны содержать как минимум 5 полей
# (например, номер, наименование, отдел продажи, ...). В список добавить хотя бы 10 словарей.
# Конструкция вида:
# market = [{"id":123456, "product":"coca-cola 0.5", "department": "drinks", ...} , {...}, {...}, ...].
# Реализовать функции:
# – вывода информации о всех товарах;
# – вывода информации о товаре по введенному с клавиатуры номеру;
# – вывода количества товаров, продающихся в определенном отделе;
# – обновлении всей информации о товаре по введенному номеру;
# – удалении товара по номеру.
# Провести тестирование функций.

import traceback

market =  [
    {'id': 701, "product": "coca-cola 0.5", "department": "drinks", "retailer": "cocesolutions", "price": 50},
    {'id': 702, "product": "fanta 2", "department": "drinks", "retailer": "cocesolutions", "price": 220},
    {'id': 200, "product": "mini ladder", "department": "instruments", "retailer": "builders league united", "price": 2165},
    {'id': 512, "product": "meat cleaver", "department": "kitchen", "retailer": "toms", "price": 1487},
    {'id': 631, "product": "dried squids", "department": "snacks", "retailer": "dryfire", "price": 117},
    {'id': 607, "product": "ham sandvich", "department": "snacks", "retailer": "snackattack", "price": 143},
    {'id': 218, "product": "flashlight", "department": "instruments", "retailer": "builders league united", "price": 248},
    {'id': 558, "product": "potato peeler", "department": "kitchen", "retailer": "tolerz", "price": 301},
    {'id': 929, "product": "mosquito spray", "department": "nature", "retailer": "builders league united", "price": 168},
    {'id': 403, "product": "cutting board", "department": "kitchen", "retailer": "toms", "price": 808}
    ]       



def allmarket():
    global market
    for i in  market:
        market = str(market)
        print(i)

def id_search():
    global market
    a = int(input('Введите ID: '))
    for i in market:
        market = str(market)
        if a == i['id']:
              print(i)

def department_search():
    global market
    a = str(input('Введите отдел товара: '))
    b = 0
    for i in market:
        market = str(market)
        if i['department'] == a:
            b += 1
    print("В отделе ", a, " продается ", b, " товара")

def updateProduct():
    global market
    a = int(input('Введите ID продукта, который хотите изменить: '))
    for i in market:
        if i['id'] == a:
            product = str(input("Введите новое название: "))
            department = str(input("Введите отдел: "))
            retailer = str(input("Введите название компании: "))
            price = str(input("Введите цену: "))
            i2 = {"id": i['id'], "product": product, "department": department, "retailer": retailer, "price": price}
            i.update(i2)
            print(i)

def deleteProduct():
    global market
    a = int(input('Введите ID продукта, который хотите удалить: '))
    for i in market:
        if i['id'] == a:
            del i['id']
            del i['product']
            del i['department']
            del i['retailer']
            del i['price']
    print(market)
    

