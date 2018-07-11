# class Human
class Human:
    age = 0
    lastname = ''
    firstname = ''
    height = 0.0
    weight = 0.0

#-------------
h = Human()
h.age = 30
h.lastname = 'Tanaka'
h.firstname = 'Ichiro'
h.height = 170.0
h.weight = 60.5

print(h.age)
print(h.lastname + " " + h.firstname)

if (h.age > 10 and h.lastname == 'Tanaka'):
    print('選ばれた人' + h.lastname + ' ' + h.firstname)
    