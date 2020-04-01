import shelve

db = shelve.open('make/.dbfile/aeData')

fieldnames = ('name', 'age', 'job', 'pay') 
maxfield = max(len(f) for f in fieldnames)

for key in db:
    print(key, '=>\n', db[key].name, db[key].pay)

#db = shelve.open('make/.dbfile/aeData')

while True:
    key = input('\nEnter a key => ') 

    if not key: break

    try:
        record = db[key]

    except:
        print('No such key "%s"!' % key)

    else:
        for field in fieldnames:
            print(field.ljust(maxfield), '=>', getattr(record, field))