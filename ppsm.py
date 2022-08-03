from csv import writer
import csv
def day_1_r():
    with open("rotterdam_1.csv") as fprice:
        fprice.readline()
        price = sum(int(r[3]) for r in csv.reader(fprice))
    with open("rotterdam_1.csv") as farea:
        farea.readline()
        area = sum(int(r[4]) for r in csv.reader(farea))  
    return price/area

def day_1_a():
    with open("amsterdam_1.csv") as fprice:
        fprice.readline()
        price = sum(int(r[3]) for r in csv.reader(fprice))
    with open("amsterdam_1.csv") as farea:
        farea.readline()
        area = sum(int(r[4]) for r in csv.reader(farea))  
    return price/area

with open('graph.csv','w',newline='') as fw:
    thewriter=writer(fw)
    heading=['DAY1',]
    thewriter.writerow(heading)
    thewriter.writerow([day_1_r()])
    thewriter.writerow([day_1_a()])