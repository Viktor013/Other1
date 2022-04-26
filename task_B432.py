"""
Создать txt-файл, вставить туда любую англоязычную статью из Википедии.
Реализовать одну функцию, которая выполняет следующие операции:
- прочитать файл построчно;
- непустые строки добавить в список;
- удалить из каждой строки все цифры, знаки препинания, скобки, кавычки и т.д. (остаются латинские буквы и пробелы);
- объединить все строки из списка в одну, используя метод join и пробел, как разделитель;
- создать словарь вида {“слово”: количество, “слово”: количество, … } для подсчета количества разных слов,
  где ключом будет уникальное слово, а значением - количество;
- вывести в порядке убывания 10 наиболее популярных слов, используя форматирование
  (вывод примерно следующего вида: “ 1 place --- sun --- 15 times \n....”);
- заменить все эти слова в строке на слово “PYTHON”;
- создать новый txt-файл;
- записать строку в файл, разбивая на строки, при этом на каждой строке записывать не более 100 символов
  при этом не делить слова.
"""

def wiki():
    with open("text.txt") as f:
        text = ''.join(filter(lambda s: s.isalpha() or s.isspace(), ' '.join([line.strip() for line in f])))
    common = []
    di = {}
    count = 0

    
    
    for word in set(text.split()):
        di[word] = di.get(word, 0) + 1
        count += 1
    print(count)
    d_list = sorted(list(di.items()), key=lambda x: x[1], reverse=True)
    for i in range(count):
        print("{} place --- {d[0]} --- {d[1]} times".format(i + 1, d=d_list[i]))
        common.append(d_list[i][0])
 
    f_text = []
    s = ''
 
    for word in text.split():
        if word in common:
            word = 'PYTHON'
        if len(s + word) < 100:
            s += word + " "
        else:
            f_text.append(s)
            s = word + " "
        
    with open('out.txt', 'w') as f:
        for line in f_text:
            f.write(line + '\n')
 
 
if __name__ == '__main__':
    wiki()


# Вызов функции
