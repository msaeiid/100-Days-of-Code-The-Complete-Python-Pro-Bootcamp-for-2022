# inheritance
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print('Inhale , Exhale.')


class Fish(Animal):
    def __init__(self):
        super(Fish, self).__init__()

    def swim(self):
        print('moving in water.')

    def breathe(self):
        super(Fish, self).breathe()
        print('doing this underwater.')


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)

list_temp = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(list_temp[2:5])
print(list_temp[2:])
print(list_temp[:5])
print(list_temp[2:5:2])
print(list_temp[::2])
print(list_temp[::-1])
