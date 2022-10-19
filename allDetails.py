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
        notFurnished=0
        furnished=0
        constructionYear=[]
        room1_price=0
        room2_price=0
        room3_price=0
        room4_price=0
        count1=0
        count2=0
        count3=0
        count4=0
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others = count_others +1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("amsterdam_1.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others+=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("rotterdam_2.csv") as f:
        f.readline()    
        for r in csv.reader(f):
            price+=int(r[3])
            area+=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others+=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("amsterdam_2.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1 
            else:
                count_others+=1 
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("amsterdam_3.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others+=1 
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("rotterdam_3.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1  
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("amsterdam_4.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("rotterdam_4.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("rotterdam_5.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("amsterdam_5.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[14]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("rotterdam_6.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("amsterdam_6.csv") as f:
        f.readline() 
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("rotterdam_7.csv") as f:
        f.readline() 
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1 
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("amsterdam_7.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, room1_price/count1, room2_price/count2, room3_price/count3, room4_price/count4]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("rotterdam_8.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1 
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("amsterdam_8.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1 
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("rotterdam_9.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("amsterdam_9.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("rotterdam_10.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1 
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("amsterdam_10.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("rotterdam_11.csv") as f:
        f.readline() 
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("amsterdam_11.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("rotterdam_12.csv") as f:
        f.readline() 
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("amsterdam_12.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("rotterdam_13.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("amsterdam_13.csv") as f:
        f.readline() 
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("rotterdam_14.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("amsterdam_14.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("rotterdam_15.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1 
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("amsterdam_15.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("rotterdam_16.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("amsterdam_16.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1 
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("rotterdam_17.csv") as f:
        f.readline() 
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1 
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("amsterdam_17.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("rotterdam_18.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("amsterdam_18.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"): 
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("rotterdam_19.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1 
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("amsterdam_19.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("rotterdam_20.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1 
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("amsterdam_20.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            else:
                count_others +=1
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("rotterdam_21.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("amsterdam_21.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1 
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:])) 
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("rotterdam_22.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'): 
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("amsterdam_22.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("rotterdam_23.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("amsterdam_23.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("rotterdam_24.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("amsterdam_24.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("rotterdam_25.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1 
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("amsterdam_25.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("rotterdam_26.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("amsterdam_26.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1 
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("rotterdam_27.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("amsterdam_27.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1 
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("rotterdam_28.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("amsterdam_28.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("rotterdam_29.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("amsterdam_29.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0  
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("rotterdam_30.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("amsterdam_30.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1 
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("rotterdam_31.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1  
            else:
                count_others +=1 
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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
    notFurnished=0
    furnished=0
    constructionYear=[]
    room1_price=0
    room2_price=0
    room3_price=0
    room4_price=0
    count1=0
    count2=0
    count3=0
    count4=0
    with open("amsterdam_31.csv") as f:
        f.readline()
        for r in csv.reader(f):
            price +=int(r[3])
            area +=int(r[4])
            if(r[6]=="Shell"):
                notFurnished+=1
            elif (r[6]=="Furnished" or r[6]=="Upholstered" or r[6]=="Upholstered or furnished"):
                furnished+=1
            if(r[13]=='Apartment' or r[13]=='Studio'):
                    count_apartment = count_apartment + 1
            elif (r[13]=='House'):
                count_house = count_house + 1 
            else:
                count_others +=1
            if(r[15]!="Constructed year is not available"):
                constructionYear.append(int(r[15][-4:]))
            if(r[17]=='1'):
                rooms_1+=1
                room1_price+=int(r[3])
                count1+=1
            elif(r[17]=='2'):
                rooms_2+=1
                room2_price+=int(r[3])
                count2+=1
            elif(r[17]=='3'):
                rooms_3+=1
                room3_price+=int(r[3])
                count3+=1
            elif(r[17]=='4'):
                rooms_4+=1
                room4_price+=int(r[3])
                count4+=1
            if(r[20]=='Present'):
                balconyPresent+=1
            elif(r[20]=='Not present'):
                balconyNotPresent+=1
    avg_room1_price=room1_price/count1
    avg_room2_price=room2_price/count2
    avg_room3_price=room3_price/count3
    avg_room4_price=room4_price/count4
    return [price/area, count_apartment, count_house, count_others, rooms_1, rooms_2, rooms_3, rooms_4, balconyPresent, balconyNotPresent, notFurnished, furnished, constructionYear, avg_room1_price, avg_room2_price, avg_room3_price, avg_room4_price]

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

def get_data():
    keyword ="nila"
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
    total_notFurnished_ams=0
    total_notFurnished_rot=0
    total_furnished_ams=0
    total_furnished_rot=0
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
    a16_17=[]
    r16_17=[]
    a17_18=[]
    r17_18=[]
    a18_19=[]
    r18_19=[]
    a19_20=[]
    r19_20=[]
    a20_21=[]
    r20_21=[]
    if (keyword == "price"):
        price_per_sq_m = pd.DataFrame({"Day":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],"Amsterdam":[a1[0],a2[0],a3[0],a4[0],a5[0],a6[0],a7[0],a8[0],a9[0],a10[0],a11[0],a12[0],a13[0],a14[0],a15[0],a16[0],a17[0],a18[0],a19[0],a20[0],a21[0],a22[0],a23[0],a24[0],a25[0],a26[0],a27[0],a28[0],a29[0],a30[0],a31[0]],"Rotterdam":[r1[0],r2[0],r3[0],r4[0],r5[0],r6[0],r7[0],r8[0],r9[0],r10[0],r11[0],r12[0],r13[0],r14[0],r15[0],r16[0],r17[0],r18[0],r19[0],r20[0],r21[0],r22[0],r23[0],r24[0],r25[0],r26[0],r27[0],r28[0],r29[0],r30[0],r31[0]]})
        return price_per_sq_m
    # print(price_per_sq_m)
    # thewriter.writerow([a1[0], a2[0], a3[0], a4[0], a5[0], a6[0], a7[0], a8[0], a9[0], a10[0], a11[0], a12[0], a13[0], a14[0], a15[0], a16[0], a17[0], a18[0], a19[0], a20[0], a21[0], a22[0], a23[0], a24[0], a25[0], a26[0], a27[0], a28[0], a29[0], a30[0], a31[0]])
    # thewriter.writerow([r1[0], r2[0], r3[0], r4[0], r5[0], r6[0], r7[0], r8[0], r9[0], r10[0], r11[0], r12[0], r13[0], r14[0], r15[0], r16[0], r17[0], r18[0], r19[0], r20[0], r21[0], r22[0], r23[0], r24[0], r25[0], r26[0], r27[0], r28[0], r29[0], r30[0], r31[0]])
    avg_room_price_ams = pd.DataFrame({ 
        "1 ROOM":[a1[13], a2[13], a3[13], a4[13], a5[13], a6[13], a7[13], a8[13], a9[13], a10[13], a11[13], a12[13], a13[13], a14[13], a15[13], a16[13], a17[13], a18[13], a19[13], a20[13], a21[13], a22[13], a23[13], a24[13], a25[13], a26[13], a27[13], a28[13], a29[13], a30[13], a31[13]],
        "2 ROOMS":[a1[14], a2[14], a3[14], a4[14], a5[14], a6[14], a7[14], a8[14], a9[14], a10[14], a11[14], a12[14], a13[14], a14[14], a15[14], a16[14], a17[14], a18[14], a19[14], a20[14], a21[14], a22[14], a23[14], a24[14], a25[14], a26[14], a27[14], a28[14], a29[14], a30[14], a31[14]],
        "3 ROOMS":[a1[15], a2[15], a3[15], a4[15], a5[15], a6[15], a7[15], a8[15], a9[15], a10[15], a11[15], a12[15], a13[15], a14[15], a15[15], a16[15], a17[15], a18[15], a19[15], a20[15], a21[15], a22[15], a23[15], a24[15], a25[15], a26[15], a27[15], a28[15], a29[15], a30[15], a31[15]],
        "4 ROOMS":[a1[16], a2[16], a3[16], a4[16], a5[16], a6[16], a7[16], a8[16], a9[16], a10[16], a11[16], a12[16], a13[16], a14[16], a15[16], a16[16], a17[16], a18[16], a19[16], a20[16], a21[16], a22[16], a23[16], a24[16], a25[16], a26[16], a27[16], a28[16], a29[16], a30[16], a31[16]],
        })
    avg_room_price_ams.to_csv("avg_room_price_ams.csv", index=False)
    avg_room_price_rot = pd.DataFrame({
        "1 ROOM": [r1[13], r2[13], r3[13], r4[13], r5[13], r6[13], r7[13], r8[13], r9[13], r10[13], r11[13], r12[13], r13[13], r14[13], r15[13], r16[13], r17[13], r18[13], r19[13], r20[13], r21[13], r22[13], r23[13], r24[13], r25[13], r26[13], r27[13], r28[13], r29[13], r30[13], r31[13]],
        "2 ROOMS": [r1[14], r2[14], r3[14], r4[14], r5[14], r6[14], r7[14], r8[14], r9[14], r10[14], r11[14], r12[14], r13[14], r14[14], r15[14], r16[14], r17[14], r18[14], r19[14], r20[14], r21[14], r22[14], r23[14], r24[14], r25[14], r26[14], r27[14], r28[14], r29[14], r30[14], r31[14]],
        "3 ROOMS": [r1[15], r2[15], r3[15], r4[15], r5[15], r6[15], r7[15], r8[15], r9[15], r10[15], r11[15], r12[15], r13[15], r14[15], r15[15], r16[15], r17[15], r18[15], r19[15], r20[15], r21[15], r22[15], r23[15], r24[15], r25[15], r26[15], r27[15], r28[15], r29[15], r30[15], r31[15]],
        "4 ROOMS": [r1[16], r2[16], r3[16], r4[16], r5[16], r6[16], r7[16], r8[16], r9[16], r10[16], r11[16], r12[16], r13[16], r14[16], r15[16], r16[16], r17[16], r18[16], r19[16], r20[16], r21[16], r22[16], r23[16], r24[16], r25[16], r26[16], r27[16], r28[16], r29[16], r30[16], r31[16]],
    })
    avg_room_price_rot.to_csv("avg_room_price_rot.csv", index=False)
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
        total_notFurnished_ams+= alist[i][10]
        total_notFurnished_rot+= rlist[i][10]
        total_furnished_ams+= alist[i][11]
        total_furnished_rot+= rlist[i][11]
    #     if(alist[i][12]<1800):
    #         a16_17.append(alist[i][12])
    #     elif(int(alist[i][12]>=1800) and int(alist[i][12]<1900)):
    #         a17_18.append(alist[i][12])
    #     elif(alist[i][12]>=1900 and alist[i][12]<2000):
    #         a18_19.append(alist[i][12])
    #     elif(alist[i][12]>=2000 and alist[i][12]<2100):
    #         a19_20.append(alist[i][12])
    #     if(rlist[i][12]<1800):
    #         r16_17.append(rlist[i][12])
    #     elif(rlist[i][12]>=1800 and rlist[i][12]<1900):
    #         r17_18.append(rlist[i][12])
    #     elif(rlist[i][12]>=1900 and rlist[i][12]<2000):
    #         r18_19.append(rlist[i][12])
    #     elif(rlist[i][12]>=2000 and rlist[i][12]<2100):
    #         r19_20.append(rlist[i][12])
    # print(len(a16_17))
    # print(len(a17_18))
    # print(len(a18_19))
    # print(len(a19_20))
    # print(len(a20_21))
    # print(len(r16_17))
    # print(len(r17_18))
    # print(len(r18_19))
    # print(len(r19_20))
    # print(len(r20_21))
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
    avg_notFurnished_ams= total_notFurnished_ams//31
    avg_notFurnished_rot= total_notFurnished_rot//31
    avg_furnished_ams= total_furnished_ams//31
    avg_furnished_rot= total_furnished_rot//31
    
    if (keyword == "buildingDetails"):        
        buildingDetails = pd.DataFrame({'LOCATION':['AMSTERDAM', 'ROTTERDAM'], 'APARTMENTS':[avg_apartments_ams, avg_apartments_rot], 'HOUSES':[avg_houses_ams, avg_houses_rot], 'OTHERS':[avg_others_ams, avg_others_rot]})
        return buildingDetails
    # buildingDetails.to_csv('buildingDetails.csv', index=False)
    if (keyword == "bedRoomDetails"):
        bedroomDetails = pd.DataFrame({'LOCATION': ['AMSTERDAM', 'ROTTERDAM'], '1 ROOM': [avg_rooms_1_ams, avg_rooms_1_rot], '2 ROOMS': [avg_rooms_2_ams, avg_rooms_2_rot],'3 ROOMS': [avg_rooms_3_ams, avg_rooms_3_rot],'4 ROOMS': [avg_rooms_4_ams, avg_rooms_4_rot],})
        # print(bedroomDetails)
        return bedroomDetails
    # bedroomDetails.to_csv('bedroomDetails.csv', index=False)
    if(keyword == "balconyDetails"):
        balconyDetails = pd.DataFrame({'LOCATION': ['AMSTERDAM', 'ROTTERDAM'], 'PRESENT': [avg_balconyPresent_ams, avg_balconyPresent_rot], 'NOT PRESENT': [avg_balconyNotPresent_ams, avg_balconyNotPresent_rot]})
        # print(balconyDetails)
        return balconyDetails
    # balconyDetails.to_csv('balcony.csv', index=False)
    if (keyword == "interiorDetails"):
        interiorDetails = pd.DataFrame({'LOCATION': ['AMSTERDAM', 'ROTTERDAM'], 'FURNISHED': [avg_furnished_ams, avg_furnished_rot], 'NOT FURNISHED': [avg_notFurnished_ams, avg_notFurnished_rot]})
        # print(interiorDetails)
        return interiorDetails
    # interiorDetails.to_csv('interior.csv', index=False)
val=get_data()