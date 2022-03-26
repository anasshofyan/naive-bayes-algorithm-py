import math
import struct
import numpy as np
import matplotlib.pyplot as plt
from operator import attrgetter
from mpl_toolkits.mplot3d import Axes3D


class Data(object):
    def __init__(self, umur, gaji, status, hutang, beli):
        self.__umur = umur
        self.__gaji = gaji
        self.__status = status
        self.__hutang = hutang
        self.__beli = beli


def printValue(self):
    umur = str(self.__umur)
    gaji = str(self.__gaji)
    status = str(self.__status)
    hutang = str(self.__hutang)
    beli = str(self.__beli)

    return(umur+"\t\t"+gaji+"\t\t"+status+"\t\t"+hutang+"\t\t"+beli)

    def setUmur(self, umur):
        self.__umur = umur

    def getUmur(self):
        return self.__umur

    def setGaji(self, gaji):
        self.__gaji = gaji

    def getGaji(self):
        return self.__gaji

    def setStatus(self, status):
        self.__status = status

    def getStatus(self):
        return self.__status

    def setHutang(self, hutang):
        self.__hutang = hutang

    def getHutang(self):
        return self.__hutang

    def setBeli(self, beli):
        self.__beli = beli

    def getBeli(self):
        return self.__beli


def probability(data, list_data):
    umurYes = 0
    umurNo = 0
    gajiYes = 0
    gajiNo = 0
    statusYes = 0
    statusNo = 0
    hutangYes = 0
    hutangNo = 0
    iya = 0
    tidak = 0

    for i in range(0, len(list_data)):
        if((list_data[i].getUmur() == data.getUmur()) and list_data[i].getBeli() == "Iya"):
            umurYes += 1
        if((list_data[i].getUmur() == data.getUmur()) and list_data[i].getBeli() == "Tidak"):
            umurNo += 1
        if((list_data[i].getGaji() == data.getGaji()) and list_data[i].getBeli() == "Iya"):
            gajiYes += 1
        if((list_data[i].getGaji() == data.getGaji()) and list_data[i].getBeli() == "Tidak"):
            gajiNo += 1
        if((list_data[i].getStatus() == data.getStatus()) and list_data[i].getBeli() == "Iya"):
            statusYes += 1
        if((list_data[i].getStatus() == data.getStatus()) and list_data[i].getBeli() == "Tidak"):
            statusNo += 1
        if((list_data[i].getHutang() == data.getHutang()) and list_data[i].getBeli() == "Iya"):
            hutangYes += 1
        if((list_data[i].getHutang() == data.getHutang()) and list_data[i].getBeli() == "Tidak"):
            hutangNo += 1

        if(list_data[i].getBeli() == "Iya"):
            iya += 1
        else:
            tidak += 1

        probYes = iya / len(list_data)
        probNo = tidak / len(list_data)

        if(not(data.getUmur() == "")):
            probYes = probYes * (umurYes / iya)
            probNo = probNo * (umurNo / tidak)

        if(not(data.getGaji() == "")):
            probYes = probYes * (gajiYes / iya)
            probNo = probNo * (gajiNo / tidak)

        if(not(data.getStatus() == "")):
            probYes = probYes * (statusYes / iya)
            probNo = probNo * (statusNo / tidak)

        if(not(data.getHutang() == "")):
            probYes = probYes * (hutangYes / iya)
            probNo = probNo * (hutangNo / tidak)

        probYes *= 100
        probNo *= 100

        if(probNo == 0 and probYes > 0):
            print("di sarankan untuk membeli \n", probYes, "%")
        elif(probNo > 0 and probYes == 0):
            print("di sarankan untuk tidak membeli \n", probNo, "%")
        elif(probNo == 0 and probYes == 0):
            print("di sarankan tidak membeli 100%")
        else:
            print("di sarankan membeli", probYes,
                  "% dan tidakmembeli", probNo, "%")


def main():
    list_data = []
    list_data.append(Data("<=30", "Tinggi", "Single", "Punya", "Tidak"))
    list_data.append(Data("<=30", "Tinggi", "Single", "tidak", "Tidak"))
    list_data.append(Data("31..40", "Tinggi", "Single", "Punya", "Iya"))
    list_data.append(Data(">40", "Sedang", "Single", "Punya", "Iya"))
    list_data.append(Data(">40", "Rendah", "Menikah", "Punya", "Iya"))
    list_data.append(Data(">40", "Rendah", "Menikah", "Tidak", "Tidak"))
    list_data.append(Data("31..40", "Rendah", "Menikah", "Tidak", "Iya"))
    list_data.append(Data("<=30", "Sedang", "Single", "Punya", "Tidak"))
    list_data.append(Data("<=30", "Rendah", "Menikah", "Punya", "Iya"))
    list_data.append(Data(">40", "Sedang", "Menikah", "Punya", "Iya"))
    list_data.append(Data("<=30", "Sedang", "Menikah", "Tidak", "Iya"))
    list_data.append(Data("31..40", "Sedang", "Single", "Tidak", "Iya"))
    list_data.append(Data("31..40", "Tinggi", "Menikah", "Punya", "Iya"))
    list_data.append(Data(">40", "sedang", "Single", "Tidak", "Tidak"))

    loop = True
    while loop:
        umur = input("masukkan range umur (<=30, 31..40, >40) ? ")
        gaji = input("masukkan standart gaji (Rendah, Sedang, Tinggi) ?")
        status = input("masukkan status sosial (Single, Menikah) ? ")
        hutang = input("masukkan status hutang (Tidak, Punya) ? ")
        data_test = Data(str(umur), str(gaji), str(status), str(hutang), "")
        probability(data_test, list_data)

        if(input("\ninput lagi (y/n)") == "y"):
            loop = True
        else:
            loop = False


if __name__ == '__main__':
    main()
