# address book application

# ------------------------------------------
# AddressBook class
# ------------------------------------------
class AddressBook:
    # アドレス帳に登録された人の一覧
    person_list = []

    def add(self, person):
        self.person_list.append(person)
    
    def show_all(self):
        for person in self.person_list:
            print('Addr: {0} {1}'.format(person.firstname, person.lastname))

    def search(self, keyword):
        for person in self.person_list:
            if (keyword in person.lastname) or (keyword in person.firstname):
                print('Search: {0} {1}'.format(person.firstname, person.lastname))
                

# ------------------------------------------
# Persion class
# ------------------------------------------
class Person:
    import datetime

    firstname = ''
    lastname  = ''
    tel = ''
    mail_addr = ''
    birthday  = datetime.datetime(2000,1,1)


# ------------------------------------------
# start section
# ------------------------------------------
# address book
ad = AddressBook()


# person1
p  = Person()
p.lastname = 'Lastname'
p.firstname = 'Firstname'
p.tel = '03-4567-9876'

# person2
p2  = Person()
p2.lastname = 'p2 Lastname'
p2.firstname = 'p2 Firstname'
p2.tel = 'p2 03-4567-9876'

# ------------------------------------------
print('--- 登録 ---')
ad.add(p)
ad.add(p2)

print('number of person : {0}'.format(len(ad.person_list)))

print('--- 一覧 ---')
ad.show_all()

print('--- 検索 ---')
ad.search('p2')
