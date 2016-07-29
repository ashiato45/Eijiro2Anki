import re
import codecs

pattern = u"■[a-b]"

with codecs.open("short.txt", "w") as fw:
    with open("EIJI-119.TXT") as fr:
        for line in fr.readlines():
            if re.match(pattern, line):
                fw.write(line)
