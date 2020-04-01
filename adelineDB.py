import shelve

db = shelve.open('make/.dbfile/aeData')

for key in db:
    print(key, '=>\n', db[key].name, db[key].pay)