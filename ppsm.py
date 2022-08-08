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

def day_2_r():
    with open("rotterdam_2.csv") as fprice:
        fprice.readline()
        price = sum(int(r[3]) for r in csv.reader(fprice))
    with open("rotterdam_2.csv") as farea:
        farea.readline()
        area = sum(int(r[4]) for r in csv.reader(farea))  
    return price/area

def day_2_a():
    with open("amsterdam_2.csv") as fprice:
        fprice.readline()
        price = sum(int(r[3]) for r in csv.reader(fprice))
    with open("amsterdam_2.csv") as farea:
        farea.readline()
        area = sum(int(r[4]) for r in csv.reader(farea))  
    return price/area

def day_3_a():
    with open("amsterdam_3.csv") as fprice:
        fprice.readline()
        price = sum(int(r[3]) for r in csv.reader(fprice))
    with open("amsterdam_3.csv") as farea:
        farea.readline()
        area = sum(int(r[4]) for r in csv.reader(farea))  
    return price/area

def day_3_r():
    with open("rotterdam_3.csv") as fprice:
        fprice.readline()
        price = sum(int(r[3]) for r in csv.reader(fprice) if r[3].isdigit() )
    with open("rotterdam_3.csv") as farea:
        farea.readline()
        area = sum(int(r[4]) for r in csv.reader(farea))  
    return price/area

def day_4_a():
    with open("amsterdam_4.csv") as fprice:
        fprice.readline()
        price = sum(int(r[3]) for r in csv.reader(fprice))
    with open("amsterdam_4.csv") as farea:
        farea.readline()
        area = sum(int(r[4]) for r in csv.reader(farea))  
    return price/area

def day_4_r():
    with open("rotterdam_4.csv") as fprice:
        fprice.readline()
        price = sum(int(r[3]) for r in csv.reader(fprice))
    with open("rotterdam_4.csv") as farea:
        farea.readline()
        area = sum(int(r[4]) for r in csv.reader(farea))  
    return price/area

with open('daily_graph.csv','w',newline='') as fw:
    thewriter=writer(fw)
    heading=['DAY1','DAY2','DAY3','DAY4']
    thewriter.writerow(heading)
    thewriter.writerow([day_1_a(),day_2_a(),day_3_a(),day_4_a()])
    thewriter.writerow([day_1_r(),day_2_r(),day_3_r(),day_4_r()])
    