'''
This is just a basic project to familarize myself with Webscraping
Created: 06/22/2022
Last Updated: 
Goal: To create_dict a webpage of open box items from the Yonkers Micro Center Store

HTML hierarchy:
id first, it is always unique to an element
name is not unique, but can be used if no id 
class, issue with it using selenium it returns the first class it finds which is
not unique

'''
from bs4 import BeautifulSoup
import requests 
import pandas as pd 


#The stores dict will be used to assign the store id to the url in the choose_number_results function
stores = {  "Tustin": "101" , "Denver": "181", "Yonkers": "105", "Duluth": "65",
            "Marietta": "041", "Chicago": "151", "Westmont": "025", "Overland Park": "191",
            "Cambridge": "121", "Rockville": "085", "Parkville": "125", "Madison Heights" : "055",
            "St.Louis Park": "045", "Brentwood" : "095","North Jersey": "075", "Westbury": "171",
            "Brooklyn": "115", "Flushing" : "145", "Columbus": "141", "Mayfield Heights": "051",
            "Sharonville": "071", "St.Davids": "061", "Houston" : "155", "Dallas" : "131",
            "Fairfax" : "081"}

space = ' '
# Figure out a way to have user select which store they want results from a drop down


for name, id in stores.items():
    print(name)

def prompt_user():
    user_response = input('Choose a store: ')
    return user_response

def get_store_number():   
    user_response = prompt_user()
    for name, id in stores.items():
            if name == user_response:
                return id
            elif name.upper() == user_response:
                return id
            elif name.lower() == user_response:
                return id
            elif name != user_response:
                quit

def choose_number_results():
    while True:
        try: 
            number_of_results = int(input("Enter either 24, 48, or 96 items per page:"))
        except ValueError:
            print("Please input a number")
            continue
        if number_of_results not in [24, 48, 96]:
            print('You can only choose between 24, 48, or 96 items!')
            continue
        else:
            pass
        print(f"{number_of_results} items will be displayed")
        print(space)
        number_results = f"rpp={number_of_results}&"
        return number_results

def return_results():
    store_id = get_store_number()
    number_results = choose_number_results()
    store_page = f'https://www.microcenter.com/search/search_results.aspx?Ntk=all&sortby=match&{number_results}prt=clearance&N=4294967291&myStore=true&storeid={store_id}'
    print(store_page)
    print(space)
    #html_text = requests.get(store_page).text
    html_text = requests.get(store_page).text
    soup = BeautifulSoup(html_text, 'lxml')
    print(space)
    items_per_page = soup.find("span", class_="itemsPerPage").text
    count = 0
    while count < int(items_per_page):
        i = soup.find(attrs={"id": f"hypProductH2_{count}"}).text
        print(i) 
        print(space)
        count += 1
            
return_results()

