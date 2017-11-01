import glob
import os

def sanitize(s):
    illegals = " :/!@#$%^&*()-=+[]{}:;',./<>?'"
    illegals += '"'
    for i in illegals:
        s = s.replace(i, "_")
    s = s.replace(" ", "_")
    
    while "__" in s:
        s = s.replace("__", "_")
    s = s.lower()
    return s

files = glob.glob(os.path.expanduser("~/Desktop/test/*"))

txtfiles = [x for x in files if ".txt" in x]

for path in txtfiles:
    with open(path) as f:
        lines = f.readlines()

    # process our line data
    stripped = [x.strip() for x in lines]
    lines_with_stuff = [x for x in stripped if x != '']
    first = lines_with_stuff[0]

    # setup our output file
    chunks = path.split(os.sep)

    filename = chunks[-1]
    basedir = os.sep.join(chunks[:-1])

    trunk, ext = os.path.splitext(filename)

    first = sanitize(first)

    off = first + ".txt"
    off = basedir + os.sep + off
    print("%s ----> %s" % (path.ljust(60), off))

    os.rename(path, off)
print len(txtfiles)
