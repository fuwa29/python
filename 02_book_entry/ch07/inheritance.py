# クラスの継承
#
class A:
    name = 'Class A'

class B(A):
    pass

b = B()
print('class=B ', b.name)

a = A()
print('class=a ', a.name)