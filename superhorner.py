import logging

logging.basicConfig(filename='horner.log',level=logging.DEBUG)

class Jednomian:

    def __init__(self, jednomian: str):

        self.degree = int(jednomian[jednomian.__len__()-1])
        self.sign = jednomian[jednomian.__len__()-3]
        self.number = int(jednomian.split('x')[0])
        self.negative = False

        if 0 - self.number > 0:
            self.negative = True

    def get(self):

        return str(str(self.number) + str(self.sign) + "^" + str(self.degree))

class Dwumian:

    def __init__(self, *args):

        self.firstpiece = args[0]
        self.secondpiece = args[1]

        self.zeroing = (eval(self.secondpiece))*(-1)


class Wielomian:

    def find_highest_degree(self):

        highestdegree = 0

        for piece in self.pieces:
            if piece.degree > highestdegree:
                highestdegree = piece.degree

        return highestdegree

    def __init__(self, *args):

        self.pieces = []

        for piece in args:
            self.pieces.append(Jednomian(piece))

        self.degree = self.find_highest_degree()

    def odejmij(self, dwumian):

        result = 0

        for coefficient in self.pieces:

            result = result * eval(dwumian) + eval(coefficient.get())

        return result

    def podzielprzez(self, dwumian: Dwumian):

        logging.info("Preparing division")

        zeroing = dwumian.zeroing

        array1 = []
        array2 = []

        for i in range (0, self.pieces.__len__()):

            array1.append(self.pieces[i].number)

        logging.info("Entry data: " + str(array1))
        logging.info("Zeroing factor: " + str(zeroing))

        logging.info("Beginning division")

        array2.append(array1[0])

        for i in range(1, array1.__len__()):

            array2.append(array1[i]+(array2[i-1]*zeroing))

            logging.info("Division loop active, iteration: " + str(i) + " got " + str(array2[i]))

        logging.info("Divison resulted in: " + str(array2))
        logging.info("Reconstruction will be necessary.")

        return array2

    def fillholes(self):

        logging.info("Starting filling holes.")

        for i in range(0, self.degree):

            logging.info("executing primary maphorner loop, degree: " + str(i))

            found = False

            for piece in self.pieces:

                logging.info("executing secondary maphorner loop, piece: " + str(piece.get()))

                if piece.degree == i:

                    logging.info("found piece of degree " + str(i) + " ")

                    found = True

            if not found:

                logging.info("piece of degree " + str(i) + " not found, adding to end.")

                self.pieces.append(Jednomian("0x^" + str(i)))

        logging.info("Holes filled.")

    def sortthat(self):

        logging.info("Sorting started.")

        newarray = []

        for i in range(0, self.pieces.__len__()):

            logging.info("executing sorting primary loop, piece: " + str(i))

            highestdegree = self.pieces[0]

            for piece in self.pieces:

                logging.info("executing sorting secondary loop, piece: " + str(piece.get()))

                if piece.degree > highestdegree.degree:

                    logging.info("found new highestdegree at: " + str(piece.degree))

                    highestdegree = piece

            logging.info("appending found highest degree piece (" + highestdegree.get() + ") into new array, and removing from old one.")

            newarray.append(highestdegree)

            self.pieces.pop(self.pieces.index(highestdegree))

        logging.info("Switching arrays")

        self.pieces = newarray

def reconstruct(array):

    logging.info("Beginning reconstruction...")

    tempjednomianarray = []
    j = array.__len__()-1

    for i in range(0, array.__len__()-1):

        if array[j] == 0:

            tempjednomianarray.append(str(array[i]) + "x^" + str(j-i-1))

        else:

            tempjednomianarray.append(str(array[i]) + "x^" + str(j-i))

    logging.info("Reconstruction complete")

    return Wielomian(*tempjednomianarray), Jednomian(str(array[array.__len__()-1]) + "x^0")
