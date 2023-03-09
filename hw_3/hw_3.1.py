import json
import io

def printJson(object):
    return json.dumps(object, ensure_ascii=False)

def string2object(st):
    if st == None:
        return None
    return json.loads(st)

beasts = list()

beasts.append({
    "Имя": "Лосяш",
    "Цвет": "Шафрановый",
    "Серии": ["Герой Плутона", "Бабочка", "Долгая рыбалка"]
})

beasts.append({
    "Имя": "Копатыч",
    "Цвет": "Коричневый",
    "Серии": ["Долгая рыбалка", "Кулинария", "Танцор Диско"]
})
#encoding='utf-8' Без utf-8 не отображалось в файле

with open("hw_3/beasts.json","w", encoding='utf-8') as file:
    file.write(printJson(beasts))

try:
    with open("hw_3/beasts.json") as file:
        content=file.read()
except FileNotFoundError:
    print("File not Found")
except IOError:
    print("Cannot read / write file maybe disk is corrupted")
except Exception as e:
    print("Something wrong!", repr(e))
finally:
    print("Is Empty")
        

def equalDictKey(dict,value):
    dict["Имя"]="Хрюня"
    if dict["Имя"]==value:
        print("True")
    else:
        print("False")
