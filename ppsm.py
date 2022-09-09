from calendar import c
from csv import writer
import csv
import pandas as pd
def day_1_r():
    with open("rotterdam_1.csv") as f:
        count_apartment=0
        count_house=0
        count_others=0
        price=0
        area=0
        rooms_1=0
        rooms_2=0
        rooms_3=0
        rooms_4=0
        balconyPresent=0
        balconyNotPresent=0
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others = count_others +1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_1_a():
    count_apartment=0
    count_house=0
    count_others=0
    price=0
    area=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("amsterdam_1.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others+=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_2_r():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("rotterdam_2.csv") as f:
        f.readline()    
        for r in csv.reader(f):
            price+=int(r[3])
            area+=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others+=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_2_a():
    count_apartment=0
    count_house=0
    count_others=0
    price=0
    area=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0   
    balconyNotPresent=0
    with open("amsterdam_2.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1 
            else:
                count_others+=1 
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_3_a():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("amsterdam_3.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others+=1 
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_3_r():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("rotterdam_3.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1  
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_4_a():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("amsterdam_4.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_4_r():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("rotterdam_4.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_5_r():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("rotterdam_5.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_5_a():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("amsterdam_5.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[14]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_6_r():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("rotterdam_6.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_6_a():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0    
    balconyNotPresent=0
    with open("amsterdam_6.csv") as f:
        f.readline() 
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_7_r():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("rotterdam_7.csv") as f:
        f.readline() 
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1 
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_7_a():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("amsterdam_7.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_8_r():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("rotterdam_8.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1 
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_8_a():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0    
    balconyNotPresent=0
    with open("amsterdam_8.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1 
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_9_r():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("rotterdam_9.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_9_a():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("amsterdam_9.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_10_r():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("rotterdam_10.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1 
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_10_a():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("amsterdam_10.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_11_r():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("rotterdam_11.csv") as f:
        f.readline() 
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_11_a():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("amsterdam_11.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_12_r():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("rotterdam_12.csv") as f:
        f.readline() 
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_12_a():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("amsterdam_12.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_13_r():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("rotterdam_13.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_13_a():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("amsterdam_13.csv") as f:
        f.readline() 
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_14_r():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("rotterdam_14.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_14_a():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("amsterdam_14.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_15_r():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("rotterdam_15.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1 
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_15_a():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("amsterdam_15.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_16_r():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("rotterdam_16.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_16_a():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("amsterdam_16.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1 
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_17_r():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("rotterdam_17.csv") as f:
        f.readline() 
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1 
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_17_a():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("amsterdam_17.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_18_r():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0    
    balconyNotPresent=0
    with open("rotterdam_18.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_18_a():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("amsterdam_18.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_19_r():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("rotterdam_19.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1 
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_19_a():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("amsterdam_19.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_20_r():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("rotterdam_20.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1 
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_20_a():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("amsterdam_20.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_21_r():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("rotterdam_21.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_21_a():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("amsterdam_21.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1  
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_22_r():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("rotterdam_22.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'): 
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_22_a():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("amsterdam_22.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_23_r():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("rotterdam_23.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_23_a():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("amsterdam_23.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_24_r():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("rotterdam_24.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_24_a():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("amsterdam_24.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_25_r():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("rotterdam_25.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1 
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_25_a():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("amsterdam_25.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_26_r():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("rotterdam_26.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_26_a():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("amsterdam_26.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1 
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_27_r():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("rotterdam_27.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_27_a():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("amsterdam_27.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1 
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_28_r():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("rotterdam_28.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_28_a():
    price=0
    area=0
    count_apartment=0
    count_house=0
    count_others=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("amsterdam_28.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_29_r():
    count_apartment=0
    count_house=0
    count_others=0
    price=0
    area=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("rotterdam_29.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_29_a():
    count_apartment=0
    count_house=0
    count_others=0
    price=0
    area=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("amsterdam_29.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_30_r():
    count_apartment=0
    count_house=0
    count_others=0
    price=0
    area=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("rotterdam_30.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_30_a():
    count_apartment=0
    count_house=0
    count_others=0
    price=0
    area=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("amsterdam_30.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1 
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_31_r():
    count_apartment=0
    count_house=0
    count_others=0
    price=0
    area=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("rotterdam_31.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1 
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_31_a():
    count_apartment=0
    count_house=0
    count_others=0
    price=0
    area=0
    rooms_1=0
    rooms_2=0
    rooms_3=0
    rooms_4=0
    balconyPresent=0
    balconyNotPresent=0
    with open("amsterdam_31.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1 
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
            elif(r[17]=='2'):
                rooms_2+=1
            elif(r[17]=='3'):
                rooms_3+=1
            elif(r[17]=='4'):
                rooms_4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent]

def day_32_r():
    with open("rotterdam_32.csv") as fprice:
        fprice.readline()
        price = sum(int(r[3]) for r in csv.reader(fprice))
    with open("rotterdam_32.csv") as farea:
        farea.readline()
        area = sum(int(r[4]) for r in csv.reader(farea))  
    return price/area

def day_32_a():
    with open("amsterdam_32.csv") as fprice:
        fprice.readline()
        price = sum(int(r[3]) for r in csv.reader(fprice))
    with open("amsterdam_32.csv") as farea:
        farea.readline()
        area = sum(int(r[4]) for r in csv.reader(farea))  
    return price/area



total_house_ams=0
total_house_rot=0
total_apartment_ams=0
total_apartment_rot=0
total_others_ams=0
total_others_rot=0
total_rooms_1_ams=0
total_rooms_2_ams=0
total_rooms_3_ams=0
total_rooms_4_ams=0
total_rooms_1_rot=0
total_rooms_2_rot=0
total_rooms_3_rot=0
total_rooms_4_rot=0
total_balconyPresent_ams=0
total_balconyPresent_rot=0
total_balconyNotPresent_ams=0
total_balconyNotPresent_rot=0
with open('daily_graph.csv','w',newline='') as fw:
    thewriter=writer(fw)
    heading=['DAY1','DAY2','DAY3','DAY4','DAY5','DAY6','DAY7','DAY8','DAY9','DAY10','DAY11','DAY12','DAY13','DAY14','DAY15','DAY16','DAY17','DAY18','DAY19','DAY20','DAY21','DAY22','DAY23','DAY24','DAY25','DAY26','DAY27','DAY28','DAY29','DAY30','DAY31']
    thewriter.writerow(heading)
    a1 = day_1_a()
    r1 = day_1_r()
    a2 = day_2_a()
    r2 = day_2_r()
    a3 = day_3_a()
    r3 = day_3_r()
    a4 = day_4_a()
    r4 = day_4_r()
    a5 = day_5_a()
    r5 = day_5_r()
    a6 = day_6_a()
    r6 = day_6_r()
    a7 = day_7_a()
    r7 = day_7_r()
    a8 = day_8_a()
    r8 = day_8_r()
    a9 = day_9_a()
    r9 = day_9_r()
    a10 = day_10_a()
    r10 = day_10_r()
    a11 = day_11_a()
    r11 = day_11_r()
    a12 = day_12_a()
    r12 = day_12_r()
    a13 = day_13_a()
    r13 = day_13_r()
    a14 = day_14_a()
    r14 = day_14_r()
    a15 = day_15_a()
    r15 = day_15_r()
    a16 = day_16_a()
    r16 = day_16_r()
    a17 = day_17_a()
    r17 = day_17_r()
    a18 = day_18_a()
    r18 = day_18_r()
    a19 = day_19_a()
    r19 = day_19_r()
    a20 = day_20_a()
    r20 = day_20_r()
    a21 = day_21_a()
    r21 = day_21_r()
    a22 = day_22_a()
    r22 = day_22_r()
    a23 = day_23_a()
    r23 = day_23_r()
    a24 = day_24_a()
    r24 = day_24_r()
    a25 = day_25_a()
    r25 = day_25_r()
    a26 = day_26_a()
    r26 = day_26_r()
    a27 = day_27_a()
    r27 = day_27_r()
    a28 = day_28_a()
    r28 = day_28_r()
    a29 = day_29_a()
    r29 = day_29_r()
    a30 = day_30_a()
    r30 = day_30_r()
    a31 = day_31_a()
    r31 = day_31_r()
    thewriter.writerow([a1[0], a2[0], a3[0], a4[0], a5[0], a6[0], a7[0], a8[0], a9[0], a10[0], a11[0], a12[0], a13[0], a14[0], a15[0], a16[0], a17[0], a18[0], a19[0], a20[0], a21[0], a22[0], a23[0], a24[0], a25[0], a26[0], a27[0], a28[0], a29[0], a30[0], a31[0]])
    thewriter.writerow([r1[0], r2[0], r3[0], r4[0], r5[0], r6[0], r7[0], r8[0], r9[0], r10[0], r11[0], r12[0], r13[0], r14[0], r15[0], r16[0], r17[0], r18[0], r19[0], r20[0], r21[0], r22[0], r23[0], r24[0], r25[0], r26[0], r27[0], r28[0], r29[0], r30[0], r31[0]])
    # thewriter.writerow([a1[1], a2[1], a3[1], a4[1], a5[1], a6[1], a7[1], a8[1], a9[1], a10[1], a11[1], a12[1], a13[1], a14[1], a15[1], a16[1], a17[1], a18[1], a19[1], a20[1], a21[1], a22[1], a23[1], a24[1], a25[1], a26[1], a27[1], a28[1], a29[1], a30[1], a31[1]])
    # thewriter.writerow([r1[1], r2[1], r3[1], r4[1], r5[1], r6[1], r7[1], r8[1], r9[1], r10[1], r11[1], r12[1], r13[1], r14[1], r15[1], r16[1], r17[1], r18[1], r19[1], r20[1], r21[1], r22[1], r23[1], r24[1], r25[1], r26[1], r27[1], r28[1], r29[1], r30[1], r31[1]])
    alist=[a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26, a27, a28, a29, a30, a31]
    rlist=[r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21, r22, r23, r24, r25, r26, r27, r28, r29, r30, r31]
    for i in range(len(alist)):
        total_apartment_ams+= alist[i][1]
        total_house_ams+= alist[i][2]
        total_others_ams+= alist[i][3]
        total_apartment_rot+= rlist[i][1]
        total_house_rot+= rlist[i][2]
        total_others_rot+= rlist[i][3]
        total_rooms_1_ams+= alist[i][4]
        total_rooms_2_ams+= alist[i][5]
        total_rooms_3_ams+= alist[i][6]
        total_rooms_4_ams+= alist[i][7]
        total_rooms_1_rot+= rlist[i][4]
        total_rooms_2_rot+= rlist[i][5]
        total_rooms_3_rot+= rlist[i][6]
        total_rooms_4_rot+= rlist[i][7]
        total_balconyPresent_ams+= alist[i][8]
        total_balconyPresent_rot+= rlist[i][8]
        total_balconyNotPresent_ams+= alist[i][9]
        total_balconyNotPresent_rot+= rlist[i][9]
    avg_houses_ams= total_house_ams//31
    avg_apartments_ams= total_apartment_ams//31
    avg_others_ams= total_others_ams//31
    avg_houses_rot= total_house_rot//31
    avg_apartments_rot= total_apartment_rot//31
    avg_others_rot= total_others_rot//31
    avg_rooms_1_ams= total_rooms_1_ams//31
    avg_rooms_2_ams= total_rooms_2_ams//31
    avg_rooms_3_ams= total_rooms_3_ams//31
    avg_rooms_4_ams= total_rooms_4_ams//31
    avg_rooms_1_rot= total_rooms_1_rot//31
    avg_rooms_2_rot= total_rooms_2_rot//31
    avg_rooms_3_rot= total_rooms_3_rot//31
    avg_rooms_4_rot= total_rooms_4_rot//31
    avg_balconyPresent_ams= total_balconyPresent_ams//31
    avg_balconyPresent_rot= total_balconyPresent_rot//31
    avg_balconyNotPresent_ams= total_balconyNotPresent_ams//31
    avg_balconyNotPresent_rot= total_balconyNotPresent_rot//31
    buildingDetails = pd.DataFrame({'Location':['Amsterdam', 'Rotterdam'], 'Apartments':[avg_apartments_ams, avg_apartments_rot], 'Houses':[avg_houses_ams, avg_houses_rot], 'Others':[avg_others_ams, avg_others_rot]})
    buildingDetails.to_csv('buildingDetails.csv', index=False)
    bedroomDetails = pd.DataFrame({'Location': ['Amsterdam', 'Rotterdam'], '1 ROOM': [avg_rooms_1_ams, avg_rooms_1_rot], '2 ROOMS': [avg_rooms_2_ams, avg_rooms_2_rot],'3 ROOMS': [avg_rooms_3_ams, avg_rooms_3_rot],'4 ROOM': [avg_rooms_4_ams, avg_rooms_4_rot],})
    bedroomDetails.to_csv('bedroomDetails.csv', index=False)
    balconyDetails = pd.DataFrame({'Location': ['Amsterdam', 'Rotterdam'], 'Present': [avg_balconyPresent_ams, avg_balconyPresent_rot], 'Not Present': [avg_balconyNotPresent_ams, avg_balconyNotPresent_rot]})
    balconyDetails.to_csv('balcony.csv', index=False)