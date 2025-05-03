import sys

inpath = r"notlast.in"
outpath = r"notlast.out"

cow = {
    "Bessie" : 0,
    "Elsie" : 0,
    "Daisy" : 0,
    "Gertie" : 0,
    "Annabelle" : 0,
    "Maggie" : 0,
    "Henrietta" : 0
}


with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:
    n = int(infile.readline())
    data = [(word, int(num)) for word, num in [infile.readline().split() for _ in range(n)]]

    for item in data:
        cow[item[0]] += item[1]

    dict_milk = {}
    for mycow, milk in cow.items():
        if not milk in dict_milk:
            dict_milk[milk] = []
        dict_milk[milk].append(mycow)

    dcopy = list(dict_milk.items())
    dcopy.sort()

    if len(dcopy) == 1 or len(dcopy[1][1]) > 1:
        print("Tie", file=outfile)
    else:
        print(dcopy[1][1][0], file=outfile)
    