from superhorner import *

print("Podaj wielomian, w formacie jednomianu ax^n, jednomiany oddziel przecinkami bez spacji.")
primarray = input().split(",")
print("Podaj dwumian, przez który chcesz go podzielić, w formacie 'x,+/-a'")
secarray = input().split(",")

wielomian1 = Wielomian(*primarray)
dwumian1 = Dwumian(*secarray)

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