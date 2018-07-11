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
            print('Addr: {0} {1}'.format(person.lastname, person.firstname))

    def search(self, keyword):
        for person in self.person_list:
            if (keyword in person.lastname) or (keyword in person.firstname):
                print('Search: {0} {1}'.format(person.lastname, person.firstname))
            else:
                print('Not found keyword[{0}] person[{1}]'.format(keyword,person.firstname))
    
    def import_data(self,csvfile):
        import csv
        import datetime
        
        try:
            with open(csvfile, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                header = next(reader)  # header
                print(header)

                for row in reader:
                    p = Person()
                    p.lastname  = row[0]
                    p.firstname = row[1]
                    p.mail_addr = row[2]
                    p.birthday  = datetime.datetime.strptime(row[3], "%Y/%m/%d")
                    p.tel       = row[4]

                    # append list
                    self.person_list.append(p)
        except:
            print('error: file not found... {0}'.format(csvfile))
            return -1
        
        return 0




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
addr = AddressBook()
csvfilename = 'sample_addr.csv'
# ------------------------------------------
print('--- csv file import ---')
rc = addr.import_data(csvfilename)
if rc < 0:
    print('fail')
    exit()
else:
    print('Success import_data! go ahead next step!')

print('number of person : {0}'.format(len(addr.person_list)))

print('--- 一覧 ---')
addr.show_all()

print('--- 検索 ---')
search_word = input('please input search word? >>> ')
addr.search(search_word)
