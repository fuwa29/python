# bmi
# class Human
class Human:
    age = 0
    lastname = ''
    firstname = ''
    height = 0.0  # m
    weight = 0.0  # kg

    def get_bmi(self):
        return (self.weight / (self.height ** 2))

#-------------
nakata = Human()
nakata.lastname = 'NAKATA'
nakata.firstname = 'HIDE'
nakata.height = 1.79
nakata.weight = 68.1

bmi = nakata.get_bmi()
print(bmi)
