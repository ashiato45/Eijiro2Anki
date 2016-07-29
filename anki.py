import re
import codecs
import sys
import csv

eijiro = "EIJI-119.TXT"
wordsfile = sys.argv[1]
outfile = wordsfile + ".csv"
words = {}

with codecs.open(wordsfile, "r", "utf8") as fwords:
    for word in fwords.readlines():
        s = [x.strip() for x in word.split("/")]
        if len(s) == 1:
            s.append("")
        if word in words.keys():
            words[s[0].lower()] = [s[0].lower(), words[s[0].lower()] + s[1] + "★"]
        else:
            words[s[0].lower()] = [s[0].lower(), s[1] + "★"]

with codecs.open(eijiro, "r") as feijiro:

    for eijiline in feijiro.readlines():
        eijisplit = eijiline.split(" : ")
        word = eijisplit[0].split(" {")[0][1:].strip()
        meaning = eijisplit[1].strip()
        meaning = re.sub("(｛.*｝)", "", meaning)

        for w in words.keys():
            if w.lower() == word.lower():
                words[w.lower()] = [word, words[w.lower()][1] + meaning + "■"]
                break

with codecs.open(outfile, "w", "utf8") as fout:
    csvout = csv.writer(fout, lineterminator="\n")
    for k,v in words.items():
        csvout.writerow([k,v[1]])
