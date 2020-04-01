import shelve
from init.Person import Person
from init.Manager import Manager

liza = Person('Liza S.', 20, 100000, 'design')
vova = Person('Vladimir S.', 18, 20000, 'python')
tom = Manager('Tom K.', 30, 50000)

db = shelve.open('make/.dbfile/aeData')
db['liza'] = liza
db['vova'] = vova
db['tom'] = tom
db.close()