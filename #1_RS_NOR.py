def getResetString():
    return input("Ну-ка чё там по Reset'у? Вводи: ")


def getSetString():
    return input("Во дают. А чё там по Set'у? Вводи: ")


def printQNQ(setString, resetString):
    arrayQ = []
    arrayNQ = []

    if setString[0] == "0" and resetString[0] == "0":
        print("Браток, я чёт не понял, я как тебе должен хранение первое определить?\n"
              "У бабушки Ванги пойду узнаю, ты пока перезапусти с нормальынми данными...")
        return

    for i in range(len(resetString)):
        if resetString[i] == "1" and setString[i] == "0":
            arrayQ.append(0)
            arrayNQ.append(1)
        elif resetString[i] == "0" and setString[i] == "1":
            arrayQ.append(1)
            arrayNQ.append(0)
        elif resetString[i] == "1" and setString[i] == "1":
            arrayQ.append(0)
            arrayNQ.append(0)
        else:
            if resetString[i - 1] == "1" and setString[i - 1] == "1":
                arrayQ.append("X")
                arrayNQ.append("X")
            else:
                arrayQ.append(arrayQ[i - 1])
                arrayNQ.append(arrayNQ[i - 1])

    print("Ну посмотри, чё получилось, ё-моё...")
    print("Q: ", end = '')
    for j in arrayQ:
        print(j, end = '')
    print()
    print("#Q: ", end = '')
    for j in arrayNQ:
        print(j, end = '')


def main():
    print("Ща порешаем, ё-моё...")

    resetString = getResetString()
    setString = getSetString()

    if len(resetString) != len(setString):
        print("Чёт количество точек не совпадает. Я так работать не буду, иди подумай над своим поведением...")
        return

    printQNQ(setString, resetString)


main()