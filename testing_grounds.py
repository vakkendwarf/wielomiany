from superhorner import *

wielomian1 = Wielomian("3x^4","2x^3","7x^1","1x^0")
dwumian1 = Dwumian("x","+1")

wielomian1.fillholes()
wielomian1.sortthat()

print("Wielomian początkowy: ")

for piece in wielomian1.pieces:
    print(piece.get())

wielomian2 = wielomian1.podzielprzez(dwumian1)

wielomian2 = reconstruct(wielomian2)

print("Wielomian podzielony: ")

for piece in wielomian2[0].pieces:

    print(piece.get())

print("Reszta: " + str(wielomian2[1].get()))