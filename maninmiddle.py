import random

print(f'Debanjana Chanda 21BCE0019')
p = int(input('Enter a prime number : \n'))
g = int(input('Enter a number : \n'))
class A:
    def __init__(self):
        self.n =int(input())
    def publish(self):
        return (g**self.n)%p
    def compute_secret(self, gb):
        return (gb**self.n)%p
class B:
    def __init__(self):
        self.a = int(input('Enter selected private number by Eve for Alice(c)\n'))
        self.b = int(input('Enter selected private number by Eve for Bob(d)\n'))
        self.arr = [self.a,self.b]
    def publish(self, i):
        return (g**self.arr[i])%p
    def compute_secret(self, ga, i):
        return (ga**self.arr[i])%p
print(f'Enter private key for Alice (a) :')
alice = A()
print(f'Enter private key for Bob (b) :')
bob = A()
eve = B()
print(f'Alice selected (a) : {alice.n}')
print(f'Bob selected (b) : {bob.n}')
print(f'Eve selected private number for Alice (c) : {eve.a}')
print(f'Eve selected private number for Bob (d) : {eve.b}')
ga = alice.publish()
gb = bob.publish()
gea = eve.publish(0)
geb = eve.publish(1)
print(f'Alice published (ga): {ga}')
print(f'Bob published (gb): {gb}')
print(f'Eve published value for Alice (gc): {gea}')
print(f'Eve published value for Bob (gd): {geb}')
sa = alice.compute_secret(gea)
sea = eve.compute_secret(ga,0)
sb = bob.compute_secret(geb)
seb = eve.compute_secret(gb,1)
print(f'Alice computed (S1) : {sa}')
print(f'Eve computed key for Alice (S1) : {sea}')
print(f'Bob computed (S2) : {sb}')
print(f'Eve computed key for Bob (S2) : {seb}')