inpath = r"censor.in"
outpath = r"censor.out"

with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:
    s, moo = infile.readlines()

    s=s.replace("\n", "")
    moo=moo.replace("\n", "")
    
    censored = ""

    for char in s:
        censored += char

        if censored[-len(moo) :] == moo:
            censored = censored[: -len(moo)]

    print(censored, file=outfile)