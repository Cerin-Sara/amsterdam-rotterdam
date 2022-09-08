from ast import Try
from bs4 import BeautifulSoup
import requests
from csv import writer
import time
import random
from lxml import etree as et
from datetime import datetime

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36"} #adding user agents to avoid detection
base_url= "https://www.pararius.com/apartments/amsterdam/page-" #base url for the pages
pages_url=[]    #list to store the url of every page
listing_url=[]  #list to store the url of every apartments

def get_dom(the_url):
    response = requests.get(the_url, headers=header)
    soup = BeautifulSoup(response.text,'lxml')
    dom = et.HTML(str(soup))
    return dom

for i in range (1,20): #generate all the pages url
    page_url=base_url + str(i)
    pages_url.append(page_url) #append the page url to the list

def get_listing_url(page_url):  #get the url of the listing
    dom = get_dom(page_url)
    page_link_list=dom.xpath('//a[@class="listing-search-item__link listing-search-item__link--title"]/@href')
    for page_link in page_link_list:
        listing_url.append("https://www.pararius.com"+page_link)

for page_url in pages_url:     #for each page url, get the listing url
    get_listing_url(page_url)
    time.sleep(random.randint(1,3))

def get_title(dom):    #get the title of the listing
    try:                #try to get the title
        title=dom.xpath("//h1[@class='listing-detail-summary__title']/text()")[0][10:-13]  #get the title using xpath
        print(title)
    except Exception as e: #if the title is not found, print the error message
        title = "Title is not available"
        print(title)
    return title

def get_location(dom):  #get the location of the listing
    try:            #try to get the location
        location= dom.xpath("//div[@class='listing-detail-summary__location']/text()")[0]
        print(location)  #print the location
    except Exception as e:      #if the location is not found, print the error message
        location = "Location is not available"
        print(location)
    return location

def get_price(dom):         #get the price of the listing
    try:                    #try to get the price
        price=dom.xpath("//div[@class='listing-detail-summary__price']/text()")[0].replace('€', '').replace(',', '').replace('\n', '').strip() #remove the €, , and \n, retrieving the value
        print(price)       
    except Exception as e:          #if the price is not found, print the error message
        price = "Price is not available"
        print(price)
    return price

def get_area(dom):         #get the area of the listing
    try:                    #try to get the area
        area=dom.xpath("//li[@class='illustrated-features__item illustrated-features__item--surface-area']/text()")[0].replace("m²","").replace(" ","")
        print(area)
    except Exception as e:      #if the area is not found, print the error message
        area="Area is not available"
        print(area)
    return area

def get_rooms(dom):
    try:
        rooms=dom.xpath("//li[@class='illustrated-features__item illustrated-features__item--number-of-rooms']/text()")[0].split(" ")[0]
        print(rooms)
    except Exception as e:
        rooms="Rooms is not available"
        print(rooms)
    return rooms

def get_interior(dom):              #get the interior status of the listing
    try:
        interior = dom.xpath("//li[@class='illustrated-features__item illustrated-features__item--interior']/text()")[0]
        print(interior)
    except  Exception as e:
        interior= "Interior is not available" #if the interior is not found, print the error message
        print(interior)
    return interior

def get_description(dom):           #get the description of the listing
    try:
        description = dom.xpath("//div[@class='listing-detail-description__additional listing-detail-description__additional--collapsed']/p/text()")[0]
        print(description)
    except Exception as e:              #if the description is not found, print the error message
        description= "Description is not available"
        print(description)
    return description

def offered_since(dom):         #get the date since the listing was added
    try:
        offer_since=dom.xpath("//dd[@class='listing-features__description listing-features__description--offered_since']/span/text()")[0]
        print(offer_since)
    except Exception as e:          #if the date is not found, print the error message
        order_since= "Date is not available"
        print(order_since)
    return offer_since

def get_availability(dom):          #get the availability of the listing
    try:
        available_from=dom.xpath("//dd[@class='listing-features__description listing-features__description--acceptance']/span/text()")[0].split(" ")[1]      
        print(available_from)
    except Exception as e:              #if the availability is not found, print the error message
        available_from="Not available to book"
        print(available_from)
    return available_from

def get_specification(dom):          #get the specification of the listing
    try:                                #try to get the specification
        specifics = dom.xpath("//dd[@class='listing-features__description listing-features__description--specifics']/span/text()")[0]
        print(specifics)
    except Exception as e:              #if the specification is not found, print the error message
        specifics="Specifics are not available"
        print(specifics)
    return specifics


def get_upkeep_status(dom):             #get the upkeeping status of the listing
    try:                                #try to get the upkeeping status
        upkeep=dom.xpath("//dd[@class='listing-features__description listing-features__description--upkeep']/span/text()")[0]
        print(upkeep)
    except Exception as e:              #if the upkeeping status is not found, print the error message
        upkeep = "Upkeep is not available"
        print(upkeep)
    return upkeep

def get_volume(dom):                       #get the volume of the listing
    try:                                    #try to get the volume
        volume= dom.xpath("//dd[@class='listing-features__description listing-features__description--volume']/span/text()")[0].split(" ")[0]
        print(volume)
    except Exception as e:                  #if the volume is not found, print the error message
        volume="Volume is not available"
        print(volume)
    return volume

def get_type(dom):                          #get the type of the listing
    try:                                    #try to get the type
        type=dom.xpath("//dd[@class='listing-features__description listing-features__description--dwelling_type']/span/text()")[0]
        print(type)
    except Exception as e:                  #if the type is not found, print the error message
        type="Type is not available"
        print(type)
    return type


def get_construction_type(dom):             #get the construction type of the listing
    try:                                    #try to get the construction type
        construction_type=dom.xpath("//dd[@class='listing-features__description listing-features__description--construction_type']/span/text()")[0]
        print(construction_type)
    except Exception as e:                   #if the construction type is not found, print the error message
        construction_type="Construction type is not available"
        print(construction_type)
    return construction_type

def get_constructed_year(dom):               #get the constructed year of the listing
    try:                                     #try to get the constructed year
        constructed_year=dom.xpath("//dd[@class='listing-features__description listing-features__description--construction_period']/span/text()")[0]
        print(constructed_year)
    except Exception as e:                  #if the constructed year is not found, print the error message
        constructed_year="Constructed year is not available"
        print(constructed_year)
    return constructed_year

def get_location_type(dom):                 #get the location type of the listing
    try:                                    #try to get the location type
        location_type=dom.xpath("//dd[@class='listing-features__description listing-features__description--situations']/span/text()")[0]
        print(location_type)
    except Exception as e:                  #if the location type is not found, print the error message
        location_type="Location type is not available"
        print(location_type)
    return location_type

def get_bedrooms(dom):                      #get the number of bedrooms of the listing
    try:                                    #try to get the number of bedrooms
        bedrooms=dom.xpath("//dd[@class='listing-features__description listing-features__description--number_of_bedrooms']/span/text()")[0]
        print(bedrooms)
    except Exception as e:                  #if the number of bedrooms is not found, print the error message
        bedrooms="Number of bedrooms is not available"
        print(bedrooms)
    return bedrooms

def get_bathrooms(dom):                     #get the number of bathrooms of the listing
    try:                                    #try to get the number of bathrooms
        bathrooms=dom.xpath("//dd[@class='listing-features__description listing-features__description--number_of_bathrooms']/span/text()")[0]
        print(bathrooms)
    except Exception as e:                   #if the number of bathrooms is not found, print the error message
        bathrooms="Number of bathrooms is not available"
        print(bathrooms)
    return bathrooms

def get_no_floors(dom):                       #get the number of floors of the listing
    try:                                      #try to get the number of floors
        no_floors=dom.xpath("//dd[@class='listing-features__description listing-features__description--number_of_floors']/span/text()")[0]
        print(no_floors)
    except Exception as e:                      #if the number of floors is not found, print the error message
        no_floors="Number of floors is not available"
        print(no_floors)
    return no_floors

def get_details_of_balcony(dom):                #get the details of the balcony of the listing
    try:                                        #try to get the details of the balcony
        balcony=dom.xpath("//dd[@class='listing-features__description listing-features__description--balcony']/span/text()")[0]
        print(balcony)
    except Exception as e:                      #if the details of the balcony is not found, print the error message
        balcony="Details of balcony is not available"
        print(balcony)
    return balcony

def get_details_of_garden(dom):                 #get the details of the garden of the listing
    try:                                        #try to get the details of the garden
        garden=dom.xpath("//dd[@class='listing-features__description listing-features__description--garden']/span/text()")[0]
        print(garden)
    except Exception as e:                      #if the details of the garden is not found, print the error message
        garden="Details of garden is not available"
        print(garden)
    return garden

def get_details_of_storage(dom):                #get the details of the storage of the listing
    try:                                        #try to get the details of the storage
        storage=dom.xpath("//dd[@class='listing-features__description listing-features__description--storage']/span/text()")[0]
        print(storage)
    except Exception as e:                      #if the details of the storage is not found, print the error message
        storage="Details of storage is not available"
        print(storage)
    return storage

def get_storage_description(dom):               #get the description of the storage of the listing
    try:                                        #try to get the description of the storage
        storage_description=dom.xpath("//dd[@class='listing-features__description listing-features__description--description']/span/text()")[0]
        print(storage_description)
    except Exception as e:                      #if the description of the storage is not found, print the error message
        storage_description="Details of description of the storage is not available"
        print(storage_description)
    return storage_description

def is_garage_present(dom):                     #check if the garage is present in the listing
    try:                                        #try to check if the garage is present
        is_garage_present=dom.xpath("//dd[@class='listing-features__description listing-features__description--available']/span/text()")[0]
        print(is_garage_present)
    except Exception as e:                      #if the garage is not present, print the error message
        is_garage_present="Details of garage is not available"
        print(is_garage_present)
    return is_garage_present


def get_contact_details(dom):                   #get the contact details of the listing
    try:                                        #try to get the contact details
        contact_details=dom.xpath("//a[@class='agent-summary__agent-contact-request']/@href")[0]
        contact_details="https://www.pararius.com"+contact_details
        print(contact_details)
    except Exception as e:                      #if the contact details are not found, print the error message
        contact_details="Details of contact is not available"
        print(contact_details)
    return contact_details

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d")

with open('amsterdam_32.csv','w',newline='') as f:
    thewriter=writer(f)
    heading=['URL','TITLE','LOCATION','PRICE PER MONTH','AREA IN m²','NUMBER OF ROOMS','INTERIOR','DESCRIPTION','OFFERED SINCE','AVAILABILITY','SPECIFICATION','UPKEEP STATUS','VOLUME','TYPE','CONSTRUCTION TYPE','CONSTRUCTION YEAR','LOCATION TYPE','NUMBER OF BEDROOMS','NUMBER OF BATHROOMS','NUMBER OF FLOORS','DETAILS OF BALCONY','DETAILS OF GARDEN','DETAILS OF STORAGE','DESCRIPTION OF STORAGE','GARAGE','CONTACT DETAILS','TIMESTAMP']
    thewriter.writerow(heading)
    for list_url in listing_url: #get the each link from the listing_url
        listing_dom=get_dom(list_url)
        title=get_title(listing_dom)  #calling the get_title() to execute the scraping of title
        location=get_location(listing_dom)   #calling the get_location() to execute the scraping of location
        price=get_price(listing_dom)   #calling the get_price() to execute the scraping of price
        area=get_area(listing_dom)   #calling the get_area() to execute the scraping of area
        rooms=get_rooms(listing_dom)   #calling the get_rooms() to execute the scraping of rooms
        interior=get_interior(listing_dom)   #calling the get_interior() to execute the scraping of interior
        description=get_description(listing_dom)   #calling the get_description() to execute the scraping of description
        offer=offered_since(listing_dom)   #calling the ordered_since() to execute the scraping of order_since
        availability=get_availability(listing_dom)   #calling the get_availability() to execute the scraping of availability
        specification=get_specification(listing_dom)   #calling the get_specification() to execute the scraping of specification
        upkeep_status=get_upkeep_status(listing_dom)   #calling the get_upkeep_status() to execute the scraping of upkeeping status
        volume=get_volume(listing_dom)   #calling the get_volume() to execute the scraping of volume
        type=get_type(listing_dom)   #calling the get_type() to execute the scraping of type
        construction_type=get_construction_type(listing_dom)   #calling the get_construction_type() to execute the scraping of construction type
        constructed_year=get_constructed_year(listing_dom)   #calling the get_constructed_year() to execute the scraping of constructed year
        location_type=get_location_type(listing_dom)   #calling the get_location_type() to execute the scraping of location type
        bedrooms=get_bedrooms(listing_dom)   #calling the get_bedrooms() to execute the scraping of number of bedrooms
        bathrooms=get_bathrooms(listing_dom)   #calling the get_bathrooms() to execute the scraping of number of bathrooms
        floors=get_no_floors(listing_dom)   #calling the get_no_floors() to execute the scraping of number of floors
        balcony_details=get_details_of_balcony(listing_dom)   #calling the get_details_of_balcony() to execute the scraping of details of balcony
        garden_details=get_details_of_garden(listing_dom)   #calling the get_details_of_garden() to execute the scraping of details of garden
        storage_details=get_details_of_storage(listing_dom)   #calling the get_details_of_storage() to execute the scraping of details of storage
        storage_description=get_storage_description(listing_dom)   #calling the get_storage_description() to execute the scraping of description of storage
        garage=is_garage_present(listing_dom)   #calling the is_garage_present() to execute the scraping of garage
        contact=get_contact_details(listing_dom)   #calling the get_contact_details() to execute the scraping of contact details
        time_stamp=get_timestamp()   #calling the get_timestamp() to execute the scraping of time stamp
        print("\n\n\n\n")
        information =[list_url,title,location,price,area,rooms,interior,description,offer,availability,specification,upkeep_status,volume,type,construction_type,constructed_year,location_type,bedrooms,bathrooms,floors,balcony_details,garden_details,storage_details,storage_description,garage,contact,time_stamp]
        thewriter.writerow(information)