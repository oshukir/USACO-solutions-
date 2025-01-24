inpath = r"measurement.in"
outpath = r"measurement.out"

def my_key(item):
    return int(item[0])

with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:
    n = int(infile.readline().strip())

    data = [line.split() for line in infile.readlines()]
    data.sort(key=my_key)

    dictionary = {
        "Mildred": 7,
        "Elsie": 7,
        "Bessie": 7
    }

    display = list(dictionary.keys())  # Инициализируем как список
    res = 0

    for i in data:
        day, cow, eff = i
        eff = int(eff)  # Корректное преобразование
        dictionary[cow] += eff

        # Определяем новое состояние дисплея
        maximum = max(dictionary.values())
        new_display = [name for name, value in dictionary.items() if value == maximum]

        if display != new_display:
            res += 1
        display = new_display

    print(res, file=outfile)
