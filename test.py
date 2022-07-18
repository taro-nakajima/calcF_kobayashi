import math


FH=open("atm2.csv","r")

for line in FH:
    templist=(line.strip()).split(",")
    print(templist[0])    